############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Lab 7: Tool Orientation of PincherX 100 Robot Arm Using
#        Exponential Coordinates and Euler Angles Exercise
#        Question
# Copyright 2022 Trossen Robotics
############################################################

import numpy as np

np.set_printoptions(suppress=True)

# Angles in radians
t1 = np.pi
t2 = 3*np.pi/2

# Skew-symmetric matrices
w1 = np.array([[ 0, -1, 0],
               [ 1,  0, 0],
               [ 0,  0, 0]])
w2 = np.array([[             0, 1/np.sqrt(2), 1/np.sqrt(2)],
               [ -1/np.sqrt(2),            0,            0],
               [ -1/np.sqrt(2),            0,            0]])

# Calculate the rotation matrices using Rodrigue's formula
e_w1_t1 = np.eye(3) + np.sin(t1) * w1 + (1 - np.cos(t1)) * (w1 @ w1)
e_w2_t2 = np.eye(3) + np.sin(t2) * w2 + (1 - np.cos(t2)) * (w2 @ w2)

# Calculate the final rotation matrix product of exponentials 

R = e_w1_t1 @ e_w2_t2

# Print the final rotation matrix
print(R)

# Question: Is this familiar to you?