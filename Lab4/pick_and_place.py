from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
import numpy as np

def main():
    bot = InterbotixManipulatorXS(robot_model='px100',
                                  group_name='arm',
                                  gripper_name='gripper')
    
    bot.arm.go_to_home_pose()

    """
    Here we give the desired orientation to the waist.
    The joint position is in radians. 
    We use the the mathematical constant π.
    NOTE: You can substitute the waist with any of the joints of the robot.
    """
    bot.arm.set_single_joint_position(joint_name='waist',
                                      position=np.pi/2.0)
    
    """
    Using the set_ee_cartesian_trajectory() function from the arm.py library,
    you can define waypoints that the end-effector should follow as it travels
    from its current pose to the...
    """
    bot.arm.set_ee_cartesian_trajectory(z=-0.1)
    bot.arm.set_ee_cartesian_trajectory(x=-0.2)

    """
    grasp() and release() functions from gripper.py library control the gripper.
    TODO: go to the gripper.py library and figure out what 2.0 represents.
    """
    bot.gripper.grasp(2.0)
    bot.arm.set_ee_cartesian_trajectory(z=0.1)

    """
    TODO: Go to the gripper.py library and figure out why the bot object uses 
    the set_press...InterbotixGripperXSInterface class
    """
    bot.gripper.set_pressure(1.0)
    
    bot.gripper.release(2.0)
    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()


#################### TEST/RUN CODE ####################
if __name__=='__main__':
    main()