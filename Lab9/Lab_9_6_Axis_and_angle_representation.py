import numpy as np
import math

def extract_axis_angle_from_matrix(R):

    # Check if R is a 3x3 matrix
    if R.shape != (3, 3):
        raise ValueError("Input must be a 3x3 matrix.")
        
    # Calculate the trace of R
    trace_R = np.trace(R)
    
    # Calculate the rotation angle theta
    theta = math.acos((trace_R - 1) / 2)
    
    # Calculate the rotation axis omega_hat
    omega_hat = np.array([
        R[2, 1] - R[1, 2],
        R[0, 2] - R[2, 0],
        R[1, 0] - R[0, 1]
    ]) / (2 * math.sin(theta))
    
    return omega_hat, theta

if __name__ == "__main__":
    # Test the function
    R = np.array([
        [-1, 0, 0],
        [0, 0, -1],
        [0, -1, 0]
    ])

    omega_hat, theta = extract_axis_angle_from_matrix(R)
    print("The rotation axis (omega_hat) is:", omega_hat)
    print("The rotation amount (theta) is:", theta)

    # # Test the function
    # R = np.array([
    #     [0.8660254, -0.5, 0],
    #     [0.5, 0.8660254, 0],
    #     [0, 0, 1]
    # ])

    # omega_hat, theta = extract_axis_angle_from_matrix(R)
    # print("The rotation axis (omega_hat) is:", omega_hat)
    # print("The rotation amount (theta) is:", theta)

    # # Test the function
    # R = np.array([
    #     [0,  0, 1],
    #     [1,  0, 0],
    #     [0, -1, 0]
    # ])

    # omega_hat, theta = extract_axis_angle_from_matrix(R)
    # print("The rotation axis (omega_hat) is:", omega_hat)
    # print("The rotation amount (theta) is:", theta)

    # # Test the function
    # R = np.array([
    #     [0, -1, 0],
    #     [1,  0, 0],
    #     [0,  0, 1]
    # ])

    # omega_hat, theta = extract_axis_angle_from_matrix(R)
    # print("The rotation axis (omega_hat) is:", omega_hat)
    # print("The rotation amount (theta) is:", theta)

    # # Test the function
    # R = np.array([
    #     [1, 0, 0],
    #     [0, 1, 0],
    #     [0, 0, 1]
    # ])

    # omega_hat, theta = extract_axis_angle_from_matrix(R)
    # print("The rotation axis (omega_hat) is:", omega_hat)
    # print("The rotation amount (theta) is:", theta)