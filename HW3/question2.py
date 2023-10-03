############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Homework 3: Orientation in Robotics (Rotation Matrices)
############################################################

import numpy as np
import math as m
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)

# Define joint angles in radians
t1 = m.radians(  30)
t2 = m.radians( 135)
t3 = m.radians(-120)

rotx_t1 = np.array([[ 1,          0,           0],
                    [ 0, np.cos(t1), -np.sin(t1)],
                    [ 0, np.sin(t1),  np.cos(t1)]])
#print(rotx_t1)

roty_t2 = np.array([[  np.cos(t2), 0, np.sin(t2)],
                    [           0, 1,          0],
                    [ -np.sin(t2), 0, np.cos(t2)]])
#print(roty_t2)

rotz_t3 = np.array([[ np.cos(t3), -np.sin(t3), 0],
                    [ np.sin(t3),  np.cos(t3), 0],
                    [          0,           0, 1],])
#print(rotz_t3)

p = np.array([[ 1/m.sqrt(3)],
              [-1/m.sqrt(6)],
              [ 1/m.sqrt(2)]])

rot_mat = rotz_t3 @ roty_t2 @ rotx_t1
print(rot_mat)

rot_p = rot_mat @ p
print(rot_p)
