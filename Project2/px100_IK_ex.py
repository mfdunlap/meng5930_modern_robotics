from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
from math import atan2, sqrt, pi, acos, sin, cos, asin
from scipy.linalg import logm, expm
import numpy as np

class ourAPI:
    def __init__(self):
        # Robot parameters
        self.L1 = 0.08945
        self.L2 = 0.100
        self.Lm = 0.035
        self.L3 = 0.100
        self.L4 = 0.1076
        self.S = np.array([[0, 0, 1, 0,       0,     0],
                           [0, 1, 0, 0, -0.0895,     0],
                           [0, 1, 0, 0, -0.1895, 0.035],
                           [0, 1, 0, -0.1895, 0, 0.135]]) # Screw axes
        self.M = np.array([[1, 0, 0,  0.2426],
                           [0, 1, 0,       0],
                           [0, 0, 1, 0.18945],
                           [0, 0, 0,       1]]) # End-effector M matrix
        
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

        w = np.array([[twist_matrix[2,1], twist_matrix[0,2], twist_matrix[1,0]]])
        v = np.array([twist_matrix[:3,-1]])

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
        Tbs     = np.linalg.inv(Tsb)
        R       = Tbs[:3, :3]
        p       = Tbs[:3, -1]
        p_brack = np.array([[   0, -p[2],  p[1]],
                           [ p[2],     0, -p[0]],
                           [-p[1],  p[0],     0]])
        
        adj_Tbs_top = np.hstack((R, np.zeros((3, 3))))
        adj_Tbs_bottom = np.hstack((np.dot(p_brack, R), R))
        adj_Tbs = np.vstack((adj_Tbs_top, adj_Tbs_bottom))

        # Convert space jacobian into body jacobian
        J = adj_Tbs @ J
        return J
    
    def poe(self, angles):
        T = np.eye(4)
        for i in range(len(angles)):
            Ti = self.screw_axis_to_transformation_matrix(self.S[i], angles[i])
            T  = T @ Ti
        return T
    
    def fk_poe(self, angles):
        T = self.poe(angles)
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
        q2 =  np.pi/2 - beta - alpha - gamma        # Shoulder angle
        q3 =  np.pi - psi - phi                     # Elbow angle
        q4 =  theta_a - q2 - q3 - np.pi/2           # Wrist angle

        # Return angles
        return [q1, q2, q3, q4]
    
    def num_IK(self, Tsd, InitGuess):
        """
        Gives joint angles using numerical method.
        """
        for i in range(100):
            # Calculate the end-effector transform (Tsb) evaluated at the InitGuess using the helper functions that you wrote at the beginning.
            Tsb = self.fk_poe(InitGuess)

            # Compute the body twist
            matrix_Vb = logm(np.linalg.inv(Tsb) @ Tsd)
            print(matrix_Vb)
            Vb = self.twist_vector_from_twist_matrix(matrix_Vb)     # use the helper function at the beginning to extract the vector
            print(Vb)

            # Compute new angles
            Jb = self.body_jacobian(InitGuess)
            NewGuess = InitGuess + np.linalg.pinv(Jb) @ Vb
            print(f"Iteration number: {i} \n")

            # Check if you're done and update initial guess
            if(np.linalg.norm(abs(NewGuess-InitGuess)) <= 0.001):
                return [NewGuess[0], NewGuess[1], NewGuess[2], NewGuess[3]] 
            else:
                InitGuess = NewGuess
        print('Numerical solution failed!!')

def main():
    # Determine the desired end-effector transform
    Td_grasp = np.array([[1, 0, 0,  0],
                         [0, 1, 0,  0],
                         [0, 0, 1, 0.10],
                         [0, 0, 0,  1]]) # Gripping location
    Td_release = np.array([[1, 0, 0, 0.05],
                           [0, 1, 0, 0.05],
                           [0, 0, 1, 0.2],
                           [0, 0, 0,  1]]) # Throwing location

    # Create experiment objects (use robot API + our custom API)
    bot = InterbotixManipulatorXS(
        robot_model='px100',
        group_name='arm',
        gripper_name='gripper'
    )
    my_api = ourAPI()

    # Start with home positiongeom_IK
    bot.arm.go_to_home_pose()

    # toggle between the geometric method and the numerical method below
    # record the answers that you get in both cases. report your observations. 

    # Go to gripping position and grip
    #joint_positions = my_api.geom_IK(Td_grasp) # Geometric inverse kinematics
    joint_positions = my_api.num_IK(Td_grasp, np.array([0.0, 0.0, 0.0, 0.0])) # Numeric inverse kinematics
    bot.arm.set_joint_positions(joint_positions) # Set positions
    bot.gripper.grasp(2.0) # Grip
    
    # Go to throwing position and throw
    #joint_positions = my_api.geom_IK(Td_release) # Geometric inverse kinematics
    joint_positions = my_api.num_IK(Td_release, np.array([0.0, 0.0, 0.0, 0.0])) # Numeric inverse kinematics
    bot.arm.set_joint_positions(joint_positions) # Set positions
    bot.gripper.release(2.0) # Release
    
    # End mission
    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()
    bot.shutdown()

if __name__ == "__main__":
    main()