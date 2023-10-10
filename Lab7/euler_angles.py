############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Lab 7: Tool Orientation of PincherX 100 Robot Arm Using
#        Exponential Coordinates and Euler Angles Exercise
#        Question
# Copyright 2022 Trossen Robotics
############################################################

import numpy as np
import math as m
# Define rotation matrix
rot_mat = np.array([[ 0.866,  -0.5, 0],
                    [   0.5, 0.866, 0],
                    [     0,     0, 1]])
rot_mat_round = np.around(rot_mat, decimals=3)

euler_angles = [[np.pi/6, 0, 0], [7*np.pi/6, np.pi, np.pi]]

for angles in euler_angles:
    # Define joint angles in radians
    theta_1 = angles[0]
    theta_2 = angles[1]
    theta_3 = angles[2]

    rot_x_theta3 = np.array([[ 1,               0,                0],
                             [ 0, np.cos(theta_3), -np.sin(theta_3)],
                             [ 0, np.sin(theta_3),  np.cos(theta_3)]])

    rot_y_theta2 = np.array([[  np.cos(theta_2), 0, np.sin(theta_2)],
                             [                0, 1,              0],
                             [ -np.sin(theta_2), 0, np.cos(theta_2)]])

    rot_z_theta1 = np.array([[ np.cos(theta_1), -np.sin(theta_1), 0],
                             [ np.sin(theta_1),  np.cos(theta_1), 0],
                             [               0,                0, 1]])

    rot = rot_z_theta1 @ rot_y_theta2 @ rot_x_theta3
    rot_round = np.around(rot, decimals=3)
    print(rot_round)

    print(f"Equal to rotation matrix: {np.array_equal(rot_mat_round, rot_round)}")