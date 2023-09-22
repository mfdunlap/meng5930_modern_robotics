############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Lab 5: Exploring DOFs and Joint Types in the PincherX 100
#        Robot Arm plus DOFs Practice Questions
# Copyright 2022 Trossen Robotics
############################################################

from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
from math import radians
import time

def main():
    # Define the joint angles in radians considering the joint limits
    waist_joint = radians(-157.26)                          # Limit: -180 to 180
    shoulder_joint = radians(0)                         # Limit: -111 to 107
    elbow_joint = radians(0)                             # Limit: -121 to 92
    wrist_joint = radians(42.34)                            # Limit: -100 to 123
    
    # Create instance of px100 robot    
    bot = InterbotixManipulatorXS(robot_model='px100',
                                  group_name='arm',
                                  gripper_name='gripper')
    
    # Put arm in home pose
    bot.arm.go_to_home_pose()

    # Display 1st DoF
    start = time.time()
    while time.time() - start < 10000.0:
        bot.arm.set_single_joint_position(joint_name='waist',
                                      position=radians(-179))
        bot.arm.set_single_joint_position(joint_name='waist',
                                      position=radians(179))
    bot.arm.go_to_home_pose()

    # Display 2nd DoF
    start = time.time()
    while time.time() - start < 10000.0:
        bot.arm.set_single_joint_position(joint_name='shoulder',
                                      position=radians(-110))
        bot.arm.set_single_joint_position(joint_name='shoulder',
                                      position=radians(106))
    bot.arm.go_to_home_pose()

    # Display 3rd DoF
    start = time.time()
    while time.time() - start < 10000.0:
        bot.arm.set_single_joint_position(joint_name='elbow',
                                      position=radians(-120))
        bot.arm.set_single_joint_position(joint_name='elbow',
                                      position=radians(91))
    bot.arm.go_to_home_pose()

    # Display 4th DoF
    start = time.time()
    while time.time() - start < 10000.0:
        bot.arm.set_single_joint_position(joint_name='wrist',
                                      position=radians(-179))
        bot.arm.set_single_joint_position(joint_name='wrist',
                                      position=radians(179))
    bot.arm.go_to_home_pose()

    # Shut down robot    
    bot.arm.go_to_sleep_pose()
    bot.shutdown()


#################### TEST/RUN CODE ####################
if __name__=='__main__':
    main()