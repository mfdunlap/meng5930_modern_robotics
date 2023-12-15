from interbotix_perception_modules.armtag import InterbotixArmTagInterface
from interbotix_perception_modules.pointcloud import InterbotixPointCloudInterface
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
from px100_IK_ex import ourAPI
import time
import numpy as np
from math import atan2, sin, cos, pi

# Define constants
ROBOT_MODEL = 'px100'
ROBOT_NAME = ROBOT_MODEL
REF_FRAME = 'camera_color_optical_frame'
ARM_TAG_FRAME = f'{ROBOT_NAME}/ar_tag_link'
ARM_BASE_FRAME = f'{ROBOT_NAME}/base_link'
Td_release = np.array([[],
                    [],
                    [],
                    []])

# Define bounds for each color (lower, upper)
red    = ((138,   0,   0), (255,  75,  75))
orange = ((144,  50,  23), (255, 116,  73))
yellow = ((157, 132,  45), (197, 172,  73))
green  = ((  0,  30,  20), ( 90, 255,  100))
blue   = ((  0,   0,  15), ( 55,  75, 255))
purple = (( 65,  34,  55), (105,  74,  94))

def is_red(cluster_color): 
    ans = all(red[0][i] <= cluster_color[i] <= red[1][i] for i in range(3)) and not \
          all(orange[0][i] <= cluster_color[i] <= orange[1][i] for i in range(3)) and not \
          all(purple[0][i] <= cluster_color[i] <= purple[1][i] for i in range(3))
    return ans

def is_orange(cluster_color): 
    ans = all(orange[0][i] <= cluster_color[i] <= orange[1][i] for i in range(3))
    return ans

def is_yellow(cluster_color): 
    ans = all(yellow[0][i] <= cluster_color[i] <= yellow[1][i] for i in range(3)) and not \
          all(orange[0][i] <= cluster_color[i] <= orange[1][i] for i in range(3)) and not \
          all(green[0][i] <= cluster_color[i] <= green[1][i] for i in range(3))
    return ans

def is_green(cluster_color): 
    ans = all(green[0][i] <= cluster_color[i] <= green[1][i] for i in range(3))
    return ans

def is_blue(cluster_color): 
    ans = all(blue[0][i] <= cluster_color[i] <= blue[1][i] for i in range(3)) and not \
          all(purple[0][i] <= cluster_color[i] <= purple[1][i] for i in range(3)) and not \
          all(green[0][i] <= cluster_color[i] <= green[1][i] for i in range(3))
    return ans

def is_purple(cluster_color): 
    ans = all(purple[0][i] <= cluster_color[i] <= purple[1][i] for i in range(3))
    return ans

def main():
    # Initialize the arm module along with the point cloud, armtag modules and px100_IK_ex custom API
    bot = InterbotixManipulatorXS(robot_model=ROBOT_MODEL,
                                  robot_name=ROBOT_NAME,
                                  group_name='arm',
                                  gripper_name='gripper')
    pcl = InterbotixPointCloudInterface(node_inf=bot.core)
    armtag = InterbotixArmTagInterface(ref_frame=REF_FRAME,
                                       arm_tag_frame=ARM_TAG_FRAME,
                                       arm_base_frame=ARM_BASE_FRAME,
                                       node_inf=bot.core)
    my_api = ourAPI()

    # Initialize arm and gripper pose
    bot.arm.go_to_sleep_pose()
    bot.gripper.release()

    # Get ArmTag pose
    armtag.find_ref_to_arm_base_transform()

    # Get initial cluster positions
    success, clusters = pcl.get_cluster_positions(ref_frame=ARM_BASE_FRAME,
                                                  sort_axis='x',
                                                  reverse=True)
    if success:
        bot.arm.go_to_home_pose()
        # Pick up purple object and place it as the base
        i = 0
        Td_drop = np.array([[ 0,          1,          0,          0         ],
                            [-0,          0,         -1,         -0.08528977],
                            [-1,          0,          0,          0.12778997],
                            [ 0,          0,          0,          1.        ]])
        
        for cluster in clusters:
            if i >= 6:
                break
            i += 1
            print(cluster['color'])
            if is_purple(cluster['color']):
                print("PURPLE FOUND...")

                # Get the cube location
                x, y, z = cluster['position']
                print(f"(x: {x}\ny: {y}\nz: {z}\n)")

                # Create z offset
                z = z + 0.01
                print(x, y, z)

                # Go on top of the selected cube
                theta_base = atan2(y,x) + 0.0349066
                new_x = x/cos(theta_base)

                # Set desired pose
                Td_grasp = np.array([[ 0.70710678, 0, 0.70710678, new_x],
                                     [          0, 1,          0,     0],
                                     [-0.70710678, 0, 0.70710678,     z],
                                     [          0, 0,          0,     1]])
                
                # Find joint positions
                jp_grasp = my_api.num_IK(Td_grasp, np.array([0,0,0,0])) # Numerical inverse kinematics
                
                # Set joint positions
                bot.arm.set_joint_positions(np.array([theta_base,0,0,0]))
                bot.arm.set_joint_positions(np.append(theta_base,jp_grasp[1:]))
                bot.gripper.grasp(2.0)

                # Set down block at base position
                jp_drop = my_api.num_IK(Td_drop, np.array([0,0,0,0]))
                bot.arm.set_joint_positions(np.array([0,0,0,0]))
                bot.arm.set_joint_positions(jp_drop)
                bot.gripper.release(5.0)
                
                break

        # Pick up blue object
        i = 0
        for cluster in clusters:
            if i >= 6:
                break
            i += 1

            if is_blue(cluster['color']):
                print("BLUE FOUND...")

                # Get the cube location
                x, y, z = cluster['position']
                print(f"(x: {x}\ny: {y}\nz: {z}\n)")

                # Create z offset
                z = z + 0.01
                print(x, y, z)

                # Go on top of the selected cube
                theta_base = atan2(y,x) + 0.0349066
                new_x = x/cos(theta_base)
                
                # Set desired pose
                Td_grasp = np.array([[ 0.70710678, 0, 0.70710678, new_x],
                                     [          0, 1,          0,     0],
                                     [-0.70710678, 0, 0.70710678,     z],
                                     [          0, 0,          0,     1]])
                
                # Find joint positions
                jp_grasp = my_api.num_IK(Td_grasp, np.array([0,0,0,0])) # Numerical inverse kinematics
                
                # Set joint positions
                bot.arm.set_joint_positions(np.array([theta_base,0,0,0]))
                bot.arm.set_joint_positions(np.append(theta_base,jp_grasp[1:]))
                bot.gripper.grasp(2.0)

                # Set down block at base position
                bot.arm.set_joint_positions(np.array([0,0,0,0]))
                bot.arm.set_joint_positions(jp_drop)
                bot.gripper.release(5.0)
                
                break

        # Pick up green object
        i = 0
        for cluster in clusters:
            if i >= 6:
                break
            i += 1

            if is_green(cluster['color']):
                print("GREEN FOUND...")

                # Get the cube location
                x, y, z = cluster['position']
                print(f"(x: {x}\ny: {y}\nz: {z}\n)")

                # Create z offset
                z = z + 0.01
                print(x, y, z)

                # Go on top of the selected cube
                theta_base = atan2(y,x) + ( 0.0349066 * 2 )
                new_x = x/cos(theta_base)
                
                # Set desired pose
                Td_grasp = np.array([[ 0.70710678, 0, 0.70710678, new_x],
                                     [          0, 1,          0,     0],
                                     [-0.70710678, 0, 0.70710678,     z],
                                     [          0, 0,          0,     1]])
                
                # Find joint positions
                jp_grasp = my_api.num_IK(Td_grasp, np.array([0,0,0,0])) # Numerical inverse kinematics
                
                # Set joint positions
                bot.arm.set_joint_positions(np.array([theta_base,0,0,0]))
                bot.arm.set_joint_positions(np.append(theta_base,jp_grasp[1:]))
                bot.gripper.grasp(2.0)

                # Set down block at base position
                bot.arm.set_joint_positions(np.array([0,0,0,0]))
                bot.arm.set_joint_positions(jp_drop)
                bot.gripper.release(5.0)

                break

        # Pick up yellow object
        i = 0
        Td_drop = np.array([[ 0,         -1,          0,          0.        ],
                            [ 0,          0,          1,          0.08528977],
                            [-1,          0,          0,          0.12778997],
                            [ 0,          0,          0,          1.        ]])
        
        for cluster in clusters:
            if i >= 6:
                break
            i += 1

            if is_yellow(cluster['color']):
                print("YELLOW FOUND...")

                # Get the cube location
                x, y, z = cluster['position']
                print(f"(x: {x}\ny: {y}\nz: {z}\n)")

                # Create z offset
                z = z + 0.01
                print(x, y, z)

                # Go on top of the selected cube
                theta_base = atan2(y,x) + 0.0349066
                new_x = x/cos(theta_base)

                # Set desired pose
                Td_grasp = np.array([[ 0.70710678, 0, 0.70710678, new_x],
                                     [          0, 1,          0,     0],
                                     [-0.70710678, 0, 0.70710678,     z],
                                     [          0, 0,          0,     1]])

                # Find joint positions
                jp_grasp = my_api.num_IK(Td_grasp, np.array([0,0,0,0])) # Numerical inverse kinematics
                
                # Set joint positions
                bot.arm.set_joint_positions(np.array([theta_base,0,0,0]))
                bot.arm.set_joint_positions(np.append(theta_base,jp_grasp[1:]))
                bot.gripper.grasp(2.0)

                # Set down block at base position
                jp_drop = my_api.num_IK(Td_drop, np.array([0,0,0,0]))
                bot.arm.set_joint_positions(np.array([0,0,0,0]))
                bot.arm.set_joint_positions(jp_drop)
                bot.gripper.release(5.0)

                break

        # Pick up orange object
        i = 0
        for cluster in clusters:
            if i >= 6:
                break
            i += 1

            if is_orange(cluster['color']):
                print("ORANGE FOUND...")

                # Get the cube location
                x, y, z = cluster['position']
                print(f"(x: {x}\ny: {y}\nz: {z}\n)")

                # Create z offset
                z = z + 0.01
                print(x, y, z)

                # Go on top of the selected cube
                theta_base = atan2(y,x) + (0.0349066 * 2)
                new_x = x/cos(theta_base)
                
                # Set desired pose
                Td_grasp = np.array([[ 0.70710678, 0, 0.70710678, new_x],
                                     [          0, 1,          0,     0],
                                     [-0.70710678, 0, 0.70710678,     z],
                                     [          0, 0,          0,     1]])
                
                # Find joint positions
                jp_grasp = my_api.num_IK(Td_grasp, np.array([0,0.523599,0.523599,0])) # Numerical inverse kinematics
                
                # Set joint positions
                bot.arm.set_joint_positions(np.array([theta_base,0,0,0]))
                bot.arm.set_joint_positions(np.append(theta_base,jp_grasp[1:]))
                bot.gripper.grasp(2.0)

                # Set down block at base position
                bot.arm.set_joint_positions(np.array([0,0,0,0]))
                bot.arm.set_joint_positions(jp_drop)
                bot.gripper.release(5.0)
                
                break

        # Pick up red object
        i = 0
        for cluster in clusters:
            if i >= 6:
                break
            i += 1

            if is_red(cluster['color']):
                print("RED FOUND...")

                # Get the cube location
                x, y, z = cluster['position']
                print(f"(x: {x}\ny: {y}\nz: {z}\n)")

                # Create z offset
                z = z + 0.01
                print(x, y, z)

                # Go on top of the selected cube
                theta_base = atan2(y,x) + (0.0349066 *2)
                new_x = x/cos(theta_base)
                
                # Set desired pose
                Td_grasp = np.array([[ 0.70710678, 0, 0.70710678, new_x],
                                     [          0, 1,          0,     0],
                                     [-0.70710678, 0, 0.70710678,     z],
                                     [          0, 0,          0,     1]])
                
                # Find joint positions
                jp_grasp = my_api.num_IK(Td_grasp, np.array([0,0.585398,0.523599,0])) # Numerical inverse kinematics
                
                # Set joint positions
                bot.arm.set_joint_positions(np.array([theta_base,0,0,0]))
                bot.arm.set_joint_positions(np.append(theta_base,jp_grasp[1:]))
                bot.gripper.grasp(2.0)

                # Set down block at base position
                bot.arm.set_joint_positions(np.array([0,0,0,0]))
                bot.arm.set_joint_positions(jp_drop)
                bot.gripper.release(5.0)

    else:
        print('Could not get cluster positions.')

    # Go to sleep
    bot.arm.go_to_sleep_pose()
    bot.shutdown()

if __name__ == "__main__":
    main()