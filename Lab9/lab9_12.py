############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Lab 9: Python Code for All the Math from Lesson 3 up to
#        Lesson 6
############################################################

import math as m
import numpy as np

def calc_norm_Sq(Sq):
    """
    Computes the normalized screw axis (S) and distance traveled along the screw (q) from the exponential coordinates of motion (Sq).
    
    Parameters:
        - Sq: exponential coordinates of motion
              1x6 numpy array of floats or ints
    
    Return:
        - S: normalized screw axis
             1x6 numpy array of floats
        - q: distance traveled along the screw
             float
    """

    if np.count_nonzero(Sq[:3]) != 0:
        q = np.linalg.norm(Sq[:3])
    else:
        q = np.linalg.norm(Sq[3:])
    
    S = np.divide(Sq, q)
    return S, q


if __name__ == "__main__":
    vector = np.array([0, 1, 2, 3, 0, 0])
    ans = calc_norm_Sq(vector)
    print("S:", ans[0])
    print("q:", ans[1])

    vector = np.array([0, 0, 0, 1.5, 1.5, 1.5])
    ans = calc_norm_Sq(vector)
    print("S:", ans[0])
    print("q:", ans[1])