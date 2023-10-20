import numpy as np

def skew_to_vector(skew_matrix):

    omega_1 = skew_matrix[2, 1]
    omega_2 = skew_matrix[0, 2]
    omega_3 = skew_matrix[1, 0]
    
    return np.array([omega_1, omega_2, omega_3])

# Test the function
skew_matrix = np.array([
    [0, -3, 2],
    [3, 0, -1],
    [-2, 1, 0]
])

omega = skew_to_vector(skew_matrix)
print("The 3-vector corresponding to the skew-symmetric matrix is:")
print(omega)
