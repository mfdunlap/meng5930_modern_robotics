# Copyright 2022 Trossen Robotics

from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
from math import radians
import time

def main():
    # Define the joint angles in radians considering the joint limits
    waist_joint    = radians(-157.26)                       # Limit: -180 to 180
    shoulder_joint = radians(20.03)                         # Limit: -111 to 107
    elbow_joint    = radians(-29.6)                         # Limit: -121 to 92
    wrist_joint    = radians(42.34)                         # Limit: -100 to 123
    joint_positions = [waist_joint,
                       shoulder_joint,
                       elbow_joint,
                       wrist_joint]
    
    # Create instance of px100 robot  
    bot = InterbotixManipulatorXS(robot_model='px100',
                                  group_name='arm',
                                  gripper_name='gripper')
    
    # Command px100 to different positions
    bot.arm.go_to_home_pose()
    bot.arm.set_joint_positions(joint_positions)
    time.sleep(5)
    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()

    # Shutdown px100
    bot.shutdown()


#################### TEST/RUN CODE ####################
if __name__=='__main__':
    main()