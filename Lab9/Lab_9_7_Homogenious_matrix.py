import numpy as np

def construct_homogeneous_matrix(R, p):

    # Check if R is a 3x3 matrix and p is a 3x1 vector
    if R.shape != (3, 3) or p.shape != (3, ):
        raise ValueError("Input dimensions are incorrect.")
        
    # Construct the 4x4 homogeneous transformation matrix T
    T = np.zeros((4, 4))
    T[0:3, 0:3] = R
    T[0:3, 3] = p
    T[3, 3] = 1
    
    return T

# Test the function
R = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

p = np.array([1, 2, 3])

T = construct_homogeneous_matrix(R, p)
print("The 4x4 homogeneous transformation matrix T is:")
print(T)
