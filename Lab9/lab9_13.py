############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Lab 9: Python Code for All the Math from Lesson 3 up to
#        Lesson 6
############################################################

import numpy as np
import Lab_9_2_skew_symmetric_matrix as L9_2

def calc_matrix_rep(S):
    """
    Computes the matrix representation (mat_rep) of a screw axis (S).
    
    Parameters:
        - S: normalized screw axis
             1x6 numpy array of floats or ints
    
    Return:
        - mat_rep: a homogenous transformation matrix
                   4x4 numpy array of floats
    """

    Sw         = S[:3]
    Sw_bracket = L9_2.vector_to_skew(Sw)
    Sv         = S[3:]

    # Compute transformation matrix
    mat_rep = np.column_stack([Sw_bracket, Sv.T])
    mat_rep = np.vstack((mat_rep, np.array([0, 0, 0, 0])))
    return mat_rep

if __name__ == "__main__":
    vector = np.array([0, 1/np.sqrt(5), 2/np.sqrt(5), 3/np.sqrt(5), 0, 0])
    ans = calc_matrix_rep(vector)
    print("Matrix Rep of S:")
    print(ans)

    vector = np.array([0, 0, 0, 1/np.sqrt(2), 1/np.sqrt(2), 0])
    ans = calc_matrix_rep(vector)
    print("Matrix Rep of S:")
    print(ans)

    vector = np.array([0, 1/np.sqrt(2), 1/np.sqrt(2), 0, 0, 0])
    ans = calc_matrix_rep(vector)
    print("Matrix Rep of S:")
    print(ans)

    vector = np.array([1/np.sqrt(3), 1/np.sqrt(3), 1/np.sqrt(3), 5/np.sqrt(3), 10/np.sqrt(3), 5/np.sqrt(3)])
    ans = calc_matrix_rep(vector)
    print("Matrix Rep of S:")
    print(ans)