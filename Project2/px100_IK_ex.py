from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
from math import atan2, sqrt, pi, acos, sin, cos, asin
from scipy.linalg import logm, expm
import numpy as np
from time import sleep

class ourAPI:
    def __init__(self):
        # Robot parameters
        self.L1 = 0.08945
        self.L2 = 0.100
        self.Lm = 0.035
        self.L3 = 0.100
        self.L4 = 0.1076
        self.S = np.array([[0, 0, 1,                  0, 0,               0],
                           [0, 1, 0,           -self.L1, 0,               0],
                           [0, 1, 0, -(self.L1+self.L2), 0,         self.Lm],
                           [0, 1, 0, -(self.L1+self.L2), 0, self.Lm+self.L3]]) # Screw axes
        self.M = np.array([[1, 0, 0, self.Lm+self.L3+self.L4],
                           [0, 1, 0,                       0],
                           [0, 0, 1,         self.L1+self.L2],
                           [0, 0, 0,                       1]]) # End-effector M matrix
        
    def screw_axis_to_transformation_matrix(self, screw_axis, angle):
        """
        Convert a screw axis and angle to a homogeneous transformation matrix.

        Parameters:
        - screw_axis: A 6D screw axis [Sw, Sv], where Sw is the rotational component
                    and Sv is the translational component.
        - angle: The angle of rotation in radians.

        Returns:
        - transformation_matrix: The 4x4 homogeneous transformation matrix
                                corresponding to the input screw axis and angle.
        """
        assert len(screw_axis) == 6, "Input screw axis must have six components"

        # Extract rotational and translational components from the screw axis
        Sw = screw_axis[:3]
        Sv = screw_axis[-3:]

        # Matrix form of the screw axis
        screw_matrix = np.zeros((4, 4))
        screw_matrix[:3, :3] = np.array([[     0, -Sw[2],  Sw[1]],
                                         [ Sw[2],      0, -Sw[0]],
                                         [-Sw[1],  Sw[0],      0]])
        screw_matrix[:3, 3] = Sv

        # Exponential map to get the transformation matrix
        exponential_map = expm(angle * screw_matrix)
        
        return exponential_map
    
    def twist_vector_from_twist_matrix(self, twist_matrix):
        """
        Compute the original 6D twist vector from a 4x4 twist matrix.

        Parameters:
        - twist_matrix: A 4x4 matrix representing the matrix form of the twist 

        Returns:
        - twist_vector: The 6D twist vector [w, v] corresponding to the input
                        twist matrix.
        """
        assert twist_matrix.shape == (4, 4), "Input matrix must be 4x4"

        w = np.array([twist_matrix[2,1], twist_matrix[0,2], twist_matrix[1,0]])
        v = np.array(twist_matrix[:3,-1])

        return np.concatenate((w, v), axis=None)
    
    def body_jacobian(self, angles):
        # Calculate the space jacobian
        J = np.array([[0.0,         -np.sin(angles[0]),                                                   0.0,                           0.0],
                      [0.0,          np.cos(angles[0]),                                                   1.0,                           1.0],
                      [1.0,                        0.0,                                                   0.0,                           0.0],
                      [0.0, -0.08945*np.cos(angles[0]), 0.035*np.sin(angles[1])-0.1*np.cos(angles[1])-0.08945, 0.1*np.sin(angles[2])-0.18945],
                      [0.0, -0.08945*np.sin(angles[0]),                                                   0.0,                           0.0],
                      [0.0,                        0.0,         0.035*np.cos(angles[1])+0.1*np.sin(angles[1]),   0.1*np.cos(angles[2])+0.035]])
        
        # Calculate adjoint of Tbs
        Tsb     = self.fk_poe(angles)
        # print("Tsb:")
        # print(Tsb)
        Tbs     = np.linalg.inv(Tsb)
        R       = Tbs[:3, :3]
        p       = Tbs[:3, -1]
        p_brack = np.array([[   0, -p[2],  p[1]],
                           [ p[2],     0, -p[0]],
                           [-p[1],  p[0],     0]])
        
        adj_Tbs_top = np.hstack((R, np.zeros((3, 3))))
        adj_Tbs_bottom = np.hstack((p_brack @ R, R))
        adj_Tbs = np.vstack((adj_Tbs_top, adj_Tbs_bottom))

        # Convert space jacobian into body jacobian
        Jb = adj_Tbs @ J
        return Tbs, Jb

    def fk_poe(self, angles):
        T = np.eye(4)
        for i in range(len(angles)):
            Ti = self.screw_axis_to_transformation_matrix(self.S[i], angles[i])
            T  = T @ Ti
        T = T @ self.M
        return T

    def geom_IK(self, Td):
        """
        Gives joint angles using the geometric method.
        """ 
        # Get the end-effector coordinates
        Xt = Td[0,3]
        Yt = Td[1,3]
        Zt = Td[2,3]

        # Get the end-effector approach vector
        ax = Td[0,0]
        ay = Td[1,0]
        az = Td[2,0]

        # Get the wrist vector
        wx = Xt - self.L4 * ax
        wy = Yt - self.L4 * ay
        wz = Zt - self.L4 * az
        
        # Calculate some intermediate variables
        r       = np.sqrt(wx**2 + wy**2)
        h       = wz - self.L1
        c       = np.sqrt(r**2 + h**2)
        beta    = np.arctan2(self.Lm, self.L2)
        psi     = np.pi/2 - beta
        Lr      = np.sqrt(self.Lm**2 + self.L2**2)
        phi     = np.arccos((c**2-self.L3**2-Lr**2)/(-2*Lr*self.L3))
        gamma   = np.arctan2(h,r)
        alpha   = np.arccos((self.L3**2-Lr**2-c**2)/(-2*Lr*c))
        theta_a = np.arctan2(np.sqrt(ax**2 + ay**2), az)

        # Get corresponding joint angles using geometry (elbow-up solution)
        q1 =  np.arctan2(Yt, Xt)                    # Waist angle

        try:                                        # ELBOW UP SOLUTION
            q2 =  np.pi/2 - beta - alpha - gamma    # Shoulder angle
            q3 =  np.pi - psi - phi                 # Elbow angle
        
        except:                                     # ELBOW DOWN SOLUTION
            q2 =  np.pi/2 - (gamma - alpha + beta)  # Shoulder angle
            q3 =  -np.pi + (phi - psi)              # Elbow angle

        q4 =  theta_a - q2 - q3 - np.pi/2           # Wrist angle

        # Return angles
        return [q1, q2, q3, q4]
    
    def num_IK(self, Tsd, InitGuess):
        """
        Gives joint angles using numerical method.
        """
        for i in range(10000):
            # Calculate the end-effector transform (Tsb) evaluated at the InitGuess using the helper functions that you wrote at the beginning.
            Tbs, Jb = self.body_jacobian(InitGuess)

            # Compute the body twist
            matrix_Vb = logm(Tbs @ Tsd)
            Vb = self.twist_vector_from_twist_matrix(matrix_Vb)     # use the helper function at the beginning to extract the vector
            
            # Compute new angles
            NewGuess = InitGuess + np.linalg.pinv(Jb) @ Vb
            print(f"Iteration number: {i} \n")

            # Check if you're done and update initial guess
            if(np.linalg.norm(abs(NewGuess-InitGuess)) <= 0.1):
                print("NEW GUESS:")
                print(NewGuess % (2*np.pi))
                print((NewGuess * 180/np.pi) % 360)
                return [NewGuess[0], NewGuess[1], NewGuess[2], NewGuess[3]]
            else:
                InitGuess = NewGuess
        print('Numerical solution failed!!')
        print("Tbs:")
        print(Tbs)
        print("Jb:")
        print(Jb)
        print("NEW GUESS:")
        print(NewGuess)

def main():
    # Rotate waist
    Td_1 = np.array([[ 0.0, 1.0, 0.0,     0.0],
                     [-1.0, 0.0, 0.0, -0.2426],
                     [ 0.0, 0.0, 1.0, 0.18945],
                     [ 0.0, 0.0, 0.0,     1.0]])

    # Bend down to item
    Td_2 = np.array([[ 0.0, 1.0, 0.0,    0.05],
                     [-1.0, 0.0, 0.0, -0.2426],
                     [ 0.0, 0.0, 1.0, 0.03945],
                     [ 0.0, 0.0, 0.0,     1.0]])

    # Lift item up
    Td_3 = np.array([[ 0.0, 1.0, 0.0,   -0.05],
                     [-1.0, 0.0, 0.0, -0.2426],
                     [ 0.0, 0.0, 1.0, 0.23945],
                     [ 0.0, 0.0, 0.0,     1.0]])

    # Bend elbow back
    Td_4 = np.array([[      0.0, 1.0,       0.0,        0.0],
                     [     -0.5, 0.0, 0.8660254,    -0.1388],
                     [0.8660254, 0.0,       0.5, 0.36923687],
                     [      0.0, 0.0,       0.0,        1.0]])

    # Rotate waist
    Td_5 = np.array([[     0.25, -0.8660254, -0.4330127,     0.0694],
                     [0.4330127,        0.5,      -0.75, 0.12020433],
                     [0.8660254,        0.0,        0.5, 0.36923687],
                     [      0.0,        0.0,        0.0,        1.0]])

    # Put elbow to netural position
    Td_6 = np.array([[      0.5, -0.8660254, 0.0,     0.1213],
                     [0.8660254,        0.5, 0.0, 0.21009776],
                     [      0.0,        0.0, 1.0,    0.18945],
                     [      0.0,        0.0, 0.0,        1.0]])

    # Set item down
    Td_7 = np.array([[ 0.49678593, -0.8660254, 0.05660161, 0.14959432],
                     [ 0.86045847,        0.5, 0.09803686, 0.25910497],
                     [-0.11320321,        0.0, 0.99357186, 0.11684392],
                     [        0.0,        0.0,        0.0,        1.0]])

    # Move away from item
    Td_8 = np.array([[ 0.488148, -0.8660254, -0.10821981, 0.14296386],
                     [0.84549714,       0.5,  -0.1874422, 0.24762066],
                     [0.21643961,       0.0,  0.97629601, 0.19991652],
                     [       0.0,       0.0,         0.0,        1.0]])

    # Create experiment objects (use robot API + our custom API)
    bot = InterbotixManipulatorXS(
        robot_model='px100',
        group_name='arm',
        gripper_name='gripper'
    )
    my_api = ourAPI()

    # Start with home positiongeom_IK
    bot.arm.go_to_home_pose()

    # Choose geometric or numerical IK solver
    method = ""
    while not method:
        method = input("Geometric (g) or Numerical (n): ").lower()
        method = method.strip()
        if method not in ["g", "n"]:
            method = ""
        elif method == "g":
            print("Geometric method selected...")
        elif method == "n":
            print("Numerical method selected...")

    # Move robot with IK
    if method == "g":
        # Move to grasp position
        print(f"Finding position 1...")
        joint_positions = my_api.geom_IK(Td_1)
        bot.arm.set_joint_positions(joint_positions)

        # Open gripper
        bot.gripper.release(2.0)
        input()

        print(f"Finding position 2...")
        joint_positions = my_api.geom_IK(Td_2)
        bot.arm.set_joint_positions(joint_positions)
        input()

        # Grip item
        bot.gripper.set_pressure(0.75)
        bot.gripper.grasp(2.0)

        # Lift item
        print(f"Finding position 3...")
        joint_positions = my_api.geom_IK(Td_3)
        bot.arm.set_joint_positions(joint_positions)
        input()

        # Rotate item
        print(f"Finding position 5...")
        joint_positions = my_api.geom_IK(Td_4)
        bot.arm.set_joint_positions(joint_positions)
        input()

        print(f"Finding position 6...")
        joint_positions = my_api.geom_IK(Td_5)
        bot.arm.set_joint_positions(joint_positions)
        input()

        # Set down item
        print(f"Finding position 7...")
        joint_positions = my_api.geom_IK(Td_6)
        bot.arm.set_joint_positions(joint_positions)
        input()

        print(f"Finding position 8...")
        joint_positions = my_api.geom_IK(Td_7)
        bot.arm.set_joint_positions(joint_positions)
        input()

        bot.gripper.release(2.0)

        # Move away from item
        print(f"Finding position 9...")
        joint_positions = my_api.geom_IK(Td_8)
        bot.arm.set_joint_positions(joint_positions)
        input()

        bot.gripper.grasp(2.0)

    else:
        # Move to grasp position
        print(f"Finding position 1...")
        joint_positions = my_api.num_IK(Td_1, np.array([0.0, 0.0, 0.0, 0.0]))
        bot.arm.set_joint_positions(joint_positions)

        # Open gripper
        bot.gripper.release(2.0)        

        print(f"Finding position 2...")
        joint_positions = my_api.num_IK(Td_2, np.array([0.0, 0.0, 0.0, 0.0]))
        bot.arm.set_joint_positions(joint_positions)

        # Grip item
        bot.gripper.set_pressure(0.75)
        bot.gripper.grasp(2.0)

        # Lift item
        print(f"Finding position 3...")
        joint_positions = my_api.num_IK(Td_3, np.array([0.0, 0.0, 0.0, 0.0]))
        bot.arm.set_joint_positions(joint_positions)

        # Rotate item
        print(f"Finding position 4...")
        joint_positions = my_api.num_IK(Td_4, np.array([0.0, 0.0, 0.0, 0.0]))
        bot.arm.set_joint_positions(joint_positions)

        print(f"Finding position 5...")
        joint_positions = my_api.num_IK(Td_5, np.array([0.0, 0.0, 0.0, 0.0]))
        bot.arm.set_joint_positions(joint_positions)

        # Set down item
        print(f"Finding position 6...")
        joint_positions = my_api.num_IK(Td_6, np.array([0.0, 0.0, 0.0, 0.0]))
        bot.arm.set_joint_positions(joint_positions)

        print(f"Finding position 7...")
        joint_positions = my_api.num_IK(Td_7, np.array([np.pi/4, np.pi/6, 0.0, -np.pi/6]))
        bot.arm.set_joint_positions(joint_positions)

        # Release item
        bot.gripper.release(2.0)

        # Move away from item
        print(f"Finding position 8...")
        joint_positions = my_api.num_IK(Td_8, np.array([np.pi/4, 0.0, -np.pi/6, 0.0]))
        bot.arm.set_joint_positions(joint_positions)

        # Close gripper
        bot.gripper.grasp(2.0)
    
    # End mission
    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()
    bot.shutdown()

if __name__ == "__main__":
    main()