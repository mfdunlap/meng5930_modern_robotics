############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Lab 9: Python Code for All the Math from Lesson 3 up to
#        Lesson 6
############################################################

import numpy as np
import Lab_9_2_skew_symmetric_matrix as L9_2

def calc_trans_matrix(S, q):
    """
    Computes the homogenous transformation matrix (trans_mat) from the screw axis (S) and distance traveled along the screw (q).
    
    Parameters:
        - S: normalized screw axis
             1x6 numpy array of floats or ints
        - q: distance traveled along the screw
             float or int
    
    Return:
        - trans_mat: a homogenous transformation matrix
                     4x4 numpy array of floats
    """

    # Split S into Sw and Sv
    Sw         = S[:3]
    Sw_bracket = L9_2.vector_to_skew(Sw)
    Sv         = S[3:]

    # Compute rotation matrix and linear vector
    rot_mat   = np.eye(3) + np.sin(q) * Sw_bracket + (1 - np.cos(q)) * (Sw_bracket @ Sw_bracket)
    lin_vec   = ((np.eye(3) * q) + ((1 - np.cos(q)) * Sw_bracket) + ((q - np.sin(q)) * (Sw_bracket @ Sw_bracket))) @ Sv

    # Compute transformation matrix
    trans_mat = np.column_stack([rot_mat, lin_vec.T])
    trans_mat = np.vstack((trans_mat, np.array([0, 0, 0, 1])))
    return trans_mat

if __name__ == "__main__":
    vector = np.array([0, 1/np.sqrt(5), 2/np.sqrt(5), 3/np.sqrt(5), 0, 0])
    ans = calc_trans_matrix(vector, np.sqrt(5))
    print("Transformation Matrix:")
    print(ans)

    vector = np.array([0, 0, 0, 1/np.sqrt(2), 1/np.sqrt(2), 0])
    ans = calc_trans_matrix(vector, np.sqrt(5))
    print("Transformation Matrix:")
    print(ans)

    vector = np.array([0, 1/np.sqrt(2), 1/np.sqrt(2), 0, 0, 0])
    ans = calc_trans_matrix(vector, np.sqrt(2))
    print("Transformation Matrix:")
    print(ans)