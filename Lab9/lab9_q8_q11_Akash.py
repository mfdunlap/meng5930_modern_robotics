####AKASH VIDYA - Lab 9 _ Questions 8-11#########

#############8###############

import numpy as np

def extract_components(T):
    """
    Extracts the rotation matrix and position vector from a given 4x4 homogeneous transformation matrix.
    
    Args:
    - T (numpy array): 4x4 homogeneous transformation matrix
    
    Returns:
    - R (numpy array): 3x3 rotation matrix
    - p (numpy array): 3x1 position vector
    """
    
    # Extracting the rotation matrix
    R = T[:3, :3]
    
    # Extracting the position vector
    p = T[:3, 3].reshape(-1, 1)
    
    return R, p



##########9##############

def compute_inverse(T):
    """
    Computes the inverse of a 4x4 homogeneous transformation matrix.
    
    Args:
    - T (numpy array): 4x4 homogeneous transformation matrix
    
    Returns:
    - T_inv (numpy array): 4x4 inverse of the homogeneous transformation matrix
    """
    
    # Extracting the rotation matrix and position vector
    R, p = extract_components(T)
    
    # Computing the inverse of the rotation matrix
    R_inv = R.T
    
    # Computing the inverse translation
    p_inv = -np.dot(R_inv, p)
    
    # Constructing the inverse transformation matrix
    T_inv = np.eye(4)
    T_inv[:3, :3] = R_inv
    T_inv[:3, 3] = p_inv.squeeze()
    
    return T_inv



##########10##############

def to_homogeneous_coordinates(v):
    """
    Converts a 3-vector to its homogeneous coordinates.
    
    Args:
    - v (numpy array): 3x1 vector
    
    Returns:
    - v_homogeneous (numpy array): 4x1 vector in homogeneous coordinates
    """
    
    v_homogeneous = np.append(v, 1).reshape(-1, 1)
    return v_homogeneous



##########11##############

def adjoint_representation(T):
    """
    Computes the 6x6 adjoint representation [Ad_T] of a given 4x4 homogeneous transformation matrix T.
    
    Args:
    - T (numpy array): 4x4 homogeneous transformation matrix
    
    Returns:
    - Ad_T (numpy array): 6x6 adjoint representation matrix
    """
    
    # Extracting the rotation matrix and position vector
    R, p = extract_components(T)
    
    # Constructing the skew-symmetric matrix for p
    p_skew = np.array([
        [0, -p[2, 0], p[1, 0]],
        [p[2, 0], 0, -p[0, 0]],
        [-p[1, 0], p[0, 0], 0]
    ])
    
    # Constructing the adjoint representation matrix
    Ad_T_top = np.hstack((R, np.zeros((3, 3))))
    Ad_T_bottom = np.hstack((np.dot(p_skew, R), R))
    Ad_T = np.vstack((Ad_T_top, Ad_T_bottom))
    
    return Ad_T



# #####TESTING#######

# # Test_Q8

# T = np.array([
#     [1, 0, 0, 2],
#     [0, 1, 0, 3],
#     [0, 0, 1, 4],
#     [0, 0, 0, 1]
# ])

# R, p = extract_components(T)

# print(T)
# print(R)
# print(p)

# #Testing Q9

# # Compute the inverse
# T_inv = compute_inverse(T)
# print(T_inv)

# #Proof of successful inverse calculation

# product = np.dot(T, T_inv)
# print(product)


# ######Testing Q10#######

# # Test
# v = np.array([[1], [2], [3]])
# v_homogeneous = to_homogeneous_coordinates(v)
# print(v_homogeneous)


# ######Testing Q11#######

# # Compute the adjoint representation
# Ad_T = adjoint_representation(T)
# print(Ad_T)
