############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Lab 7: Tool Orientation of PincherX 100 Robot Arm Using
#        Exponential Coordinates and Euler Angles Exercise
#        Question
# Copyright 2022 Trossen Robotics
############################################################

import numpy as np
from math import radians

np.set_printoptions(suppress=True)

# Angles in radians
theta_1 = radians(90)
theta_2 = radians(-45)
theta_3 = radians(0)
theta_4 = radians(45)

# Skew-symmetric matrices
z_hat_bracket = np.array([[ 0, -1, 0],
                          [ 1,  0, 0],
                          [ 0,  0, 0]])
y_hat_bracket = np.array([[  0, 0, 1],
                          [  0, 0, 0],
                          [ -1, 0, 0]])

# Calculate the rotation matrices using Rodrigue's formula
e_z_hat_bracket_theta_1 = np.eye(3) + np.sin(theta_1) * z_hat_bracket + (1 - np.cos(theta_1)) * (z_hat_bracket @ z_hat_bracket)
e_y_hat_bracket_theta_2 = np.eye(3) + np.sin(theta_2) * y_hat_bracket + (1 - np.cos(theta_2)) * (y_hat_bracket @ y_hat_bracket)
e_y_hat_bracket_theta_3 = np.eye(3) + np.sin(theta_3) * y_hat_bracket + (1 - np.cos(theta_3)) * (y_hat_bracket @ y_hat_bracket)
e_y_hat_bracket_theta_4 = np.eye(3) + np.sin(theta_4) * y_hat_bracket + (1 - np.cos(theta_4)) * (y_hat_bracket @ y_hat_bracket)

# Calculate the final rotation matrix product of exponentials 

R = e_z_hat_bracket_theta_1 @ e_y_hat_bracket_theta_2 @ e_y_hat_bracket_theta_3 @ e_y_hat_bracket_theta_4

# Print the final rotation matrix
print(R)

# Question: Is this familiar to you?