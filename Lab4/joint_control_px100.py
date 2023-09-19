# Copyright 2022 Trossen Robotics

from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
from math import radians

def main():
    # TODO: Define the joint angles in radians considering the joint limits
    waist_joint = radians(-157.26)
    shoulder_joint = radians(20.03)
    elbow_joint = radians(69.2)
    wrist_joint = radians(42.34)
    joint_positions = [waist_joint,
                       shoulder_joint,
                       elbow_joint,
                       wrist_joint]
    
    bot = InterbotixManipulatorXS(robot_model='px100',
                                  group_name='arm',
                                  gripper_name='gripper')
    
    bot.arm.go_to_home_pose()
    bot.arm.set_joint_positions(joint_positions)
    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()
    bot.shutdown()


#################### TEST/RUN CODE ####################
if __name__=='__main__':
    main()