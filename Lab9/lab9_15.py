############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Lab 9: Python Code for All the Math from Lesson 3 up to
#        Lesson 6
############################################################

import numpy as np
import Lab_9_2_skew_symmetric_matrix as L9_2
import Lab_9_6_Axis_and_angle_representation as L9_6
import lab9_q8_q11_Akash as L9_8to11
import lab9_12 as L9_12

def calc_exp_rep(T_mat):
    """
    Computes the screw axis (S) and distance traveled along the screw (q) from a transformation matrix.
    
    Parameters:
        - T_mat: a homogenous transformation matrix
                 4x4 numpy array of floats or ints
    
    Return:
        - S: screw axis
             1x6 numpy array of floats
        - q: distance traveled along the screw
             float
    """

    # Separate transformation matrix into rotational and translational components
    R, p_vert = L9_8to11.extract_components(T_mat)
    p = p_vert.T

    # Solve for Sw (w_hat) and theta
    Sw, theta  = L9_6.extract_axis_angle_from_matrix(R)
    w_hat_bracket = L9_2.vector_to_skew(Sw)
    
    # Solve for Sv
    if (theta != 0.0):
        Sv = (((1/theta) * np.eye(3)) - 
            (0.5 * w_hat_bracket) + 
            (((1/theta) - 0.5 * (1/np.tan(theta/2))) * (w_hat_bracket @ w_hat_bracket))) * p
        
        Sv = Sv[:,0]
        # Create S
        S = np.concatenate((Sw, Sv), axis=None)
        q = theta
    
    else:
        Sq = np.concatenate((np.array([[0.0, 0.0, 0.0]]), p), axis=1)[0]
        S, q = L9_12.calc_norm_Sq(Sq)
    
    return S, q
        
    
if __name__ == "__main__":
    T_mat = np.array([[ 0, -1,  0, 3],
                      [ 0,  0, -1, 0],
                      [ 1,  0,  0, 0],
                      [ 0,  0,  0, 1]])
    
    ans = calc_exp_rep(T_mat)
    print("S:", ans[0])
    print("q:", ans[1])

    T_mat = np.array([[  0.3536,  0.5732, -0.7392, 0],
                      [  0.6124, -0.7392, -0.2803, 0],
                      [ -0.7071, -0.3536, -0.6124, 0],
                      [       0,       0,       0, 1]])
    
    ans = calc_exp_rep(T_mat)
    print("S:", ans[0])
    print("q:", ans[1])

    T_mat = np.array([[ 1, 0, 0, 10],
                      [ 0, 1, 0,  5],
                      [ 0, 0, 1,  5],
                      [ 0, 0, 0,  1]])
    
    ans = calc_exp_rep(T_mat)
    print("S:", ans[0])
    print("q:", ans[1])