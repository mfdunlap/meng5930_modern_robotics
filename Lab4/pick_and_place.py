from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
import numpy as np
import time

def main():
    bot = InterbotixManipulatorXS(robot_model='px100',
                                  group_name='arm',
                                  gripper_name='gripper')
    
    bot.arm.go_to_home_pose()

    # Open gripper
    bot.gripper.release(1.0)

    # Move px100 to position to pick up block
    bot.arm.set_single_joint_position(joint_name='waist',
                                      position=-np.pi/2.0)
    bot.arm.set_ee_cartesian_trajectory(x=0.05, z=-0.15)

    # Set gripper pressure and pick up object
    bot.gripper.set_pressure(0.75)
    bot.gripper.grasp(2.0)

    # Lift object
    bot.arm.set_ee_cartesian_trajectory(x=-0.1)
    bot.arm.set_ee_cartesian_trajectory(z=0.2)

    # Rotate object
    bot.arm.set_single_joint_position(joint_name='elbow',
                                      position=-np.pi/3.0)
    
    # Move object to place position
    bot.arm.set_single_joint_position(joint_name='waist',
                                      position=np.pi/3)
    bot.arm.set_single_joint_position(joint_name='elbow',
                                      position=0.0)
    bot.arm.set_ee_cartesian_trajectory(x=0.06)
    bot.arm.set_ee_cartesian_trajectory(z=-0.2)

    # Release object
    bot.gripper.release(2.0)

    # Move arm away from object and close gripper
    bot.arm.set_ee_cartesian_trajectory(z=0.2)
    bot.gripper.grasp(1.0)

    # Return bot to home position
    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()

    # Shutdown px100
    bot.shutdown()


#################### TEST/RUN CODE ####################
if __name__=='__main__':
    main()