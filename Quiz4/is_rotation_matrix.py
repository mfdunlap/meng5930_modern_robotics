import math as m
import numpy as np

def is_rotation_matrix(matrix):
    return is_so3(matrix)

def is_so3(matrix):
    # Check 1: Matrix (R) is a 3x3 (for this particular case)
    mat_shape = matrix.shape
    if len(mat_shape) != 2:
        return False
    elif mat_shape[0] != 3 or mat_shape[1] != 3:
        return False
    
    # Check 2: RR^T = I
    mat_eye = np.around(matrix @ np.transpose(matrix), decimals=5)
    print(mat_eye)
    eye = np.around(np.eye(mat_shape[0], dtype=float), decimals=5)
    #print(eye)
    if not np.array_equal(mat_eye, eye):
        return False

    # Check 3: det(R) = 1
    det = round(np.linalg.det(matrix), ndigits=5)
    print(det)
    if det != 1:
        return False
    
    return True

if __name__ == "__main__":
    ans = list()

    mat = np.array([[ -1/m.sqrt(2), 1/m.sqrt(2),           0],
                    [         -1/2,        -1/2, 1/m.sqrt(2)],
                    [          1/2,         1/2, 1/m.sqrt(2)]])
    det = np.linalg.det(mat)
    print(det)
    ans.append(is_rotation_matrix(mat))

    mat = np.array([[ 0, 0, 0],
                    [ 1, 0, 1],
                    [ 1, 0, 1]])
    det = np.linalg.det(mat)
    print(det)
    ans.append(is_rotation_matrix(mat))

    for i, answer in enumerate(ans):
        print(f"Matrix {i:>2}: {answer}")