import math as m
import numpy as np

def is_rotation_matrix(matrix):
    mat_rounded = np.around(matrix, decimals=5)
    return is_so3(mat_rounded)

def is_so3(matrix):
    # Check 1: Matrix (R) is SQUARE
    mat_shape = matrix.shape
    if len(mat_shape) != 2:
        return False
    elif mat_shape[0] != mat_shape[1]:
        return False
    
    # Check 2: RR^T = I
    mat_mat_t = np.around(matrix @ np.transpose(matrix), decimals=5)
    eye = np.around(np.eye(mat_shape[0], dtype=float), decimals=5)
    if not np.array_equal(mat_mat_t, eye):
        return False

    # Check 3: det(R) = 1
    det = round(np.linalg.det(matrix), ndigits=5)
    if det != 1:
        return False
    
    return True

if __name__ == "__main__":
    m1 = np.array([[ 1, 0],
                   [ 0, 1]])
    print(f"Matrix 1: {is_rotation_matrix(m1)}")

    m2 = np.array([[ 1, 0, 0],
                   [ 0, 1, 0],
                   [ 0, 0, 1]])
    print(f"Matrix 2: {is_rotation_matrix(m2)}")

    m3 = np.array([[ 2, 0, 0],
                   [ 0, 1, 0],
                   [ 0, 0, 1]])
    print(f"Matrix 3: {is_rotation_matrix(m3)}")

    t1 = m.radians(40)
    m4 = np.array([[ 1,          0,           0],
                   [ 0, np.cos(t1), -np.sin(t1)],
                   [ 0, np.sin(t1),  np.cos(t1)]])
    print(f"Matrix 4: {is_rotation_matrix(m4)}")

    m5 = np.array([[1, 2]])
    print(f"Matrix 5: {is_rotation_matrix(m5)}")