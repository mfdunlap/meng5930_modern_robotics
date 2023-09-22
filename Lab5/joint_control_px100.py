############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Lab 5: Exploring DOFs and Joint Types in the PincherX 100
#        Robot Arm plus DOFs Practice Questions
# Copyright 2022 Trossen Robotics
############################################################

from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
from math import radians

def main():    
    # Create instance of px100 robot    
    bot = InterbotixManipulatorXS(robot_model='px100',
                                  group_name='arm',
                                  gripper_name='gripper')
    
    # Put arm in home pose
    bot.arm.go_to_home_pose()

    # Display 1st DoF
    for i in range(2):
        bot.arm.set_single_joint_position(joint_name='waist',
                                      position=radians(-179))
        bot.arm.set_single_joint_position(joint_name='waist',
                                      position=radians(179))
    bot.arm.go_to_home_pose()

    # Display 2nd DoF
    for i in range(2):
        bot.arm.set_single_joint_position(joint_name='shoulder',
                                      position=radians(-110))
        bot.arm.set_single_joint_position(joint_name='shoulder',
                                      position=radians(30))
    bot.arm.go_to_home_pose()

    # Display 3rd DoF
    for i in range(2):
        bot.arm.set_single_joint_position(joint_name='elbow',
                                      position=radians(-120))
        bot.arm.set_single_joint_position(joint_name='elbow',
                                      position=radians(45))
    bot.arm.go_to_home_pose()

    # Display 4th DoF
    for i in range(2):
        bot.arm.set_joint_positions([0.0, 0.0, 0.0, radians(-99)])
        bot.arm.set_joint_positions([0.0, 0.0, 0.0, radians(122)])
    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()

    # Shut down robot    
    bot.arm.go_to_sleep_pose()
    bot.shutdown()


#################### TEST/RUN CODE ####################
if __name__=='__main__':
    main()