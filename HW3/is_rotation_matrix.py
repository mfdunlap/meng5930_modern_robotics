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
    #print(mat_eye)
    eye = np.around(np.eye(mat_shape[0], dtype=float), decimals=5)
    #print(eye)
    if not np.array_equal(mat_eye, eye):
        return False

    # Check 3: det(R) = 1
    det = round(np.linalg.det(matrix), ndigits=5)
    if det != 1:
        return False
    
    return True

if __name__ == "__main__":
    ans = list()
    # Should return False (Ex. 1-6)
    mat = np.array([[1]])
    ans.append(is_rotation_matrix(mat))

    mat = np.array([[ 1, 0],
                   [ 0, 1]])
    ans.append(is_rotation_matrix(mat))

    mat = np.array([[1, 2]])
    ans.append(is_rotation_matrix(mat))

    mat = np.array([[ 2, 0, 0],
                    [ 0, 1, 0],
                    [ 0, 0, 1]])
    ans.append(is_rotation_matrix(mat))

    mat = np.array([[     2,     -1, 17],
                    [ 0.667,    200, 145],
                    [ -0.84, 0.9084, -1001]])
    ans.append(is_rotation_matrix(mat))

    mat = np.array([[    0.5, 0.765, 0.171],
                    [  0.204, 0.200, 0.145],
                    [ -0.121, 0.342, -0.325]])
    ans.append(is_rotation_matrix(mat))

    # Should return True (Ex. 7-20)
    t = m.radians(40)
    mat = np.array([[ 1,          0,           0],
                    [ 0, np.cos(t), -np.sin(t)],
                    [ 0, np.sin(t),  np.cos(t)]])
    ans.append(is_rotation_matrix(mat))

    mat = np.array([[ np.cos(t), -np.sin(t), 0],
                    [ np.sin(t),  np.cos(t), 0],
                    [         0,          0, 1]])
    ans.append(is_rotation_matrix(mat))

    mat = np.array([[  np.cos(t), 0, np.sin(t)],
                    [          0, 1,         0],
                    [ -np.sin(t), 0, np.cos(t)]])
    ans.append(is_rotation_matrix(mat))

    t = m.radians(163)
    mat = np.array([[ 1,          0,           0],
                    [ 0, np.cos(t), -np.sin(t)],
                    [ 0, np.sin(t),  np.cos(t)]])
    ans.append(is_rotation_matrix(mat))

    mat = np.array([[ np.cos(t), -np.sin(t), 0],
                    [ np.sin(t),  np.cos(t), 0],
                    [         0,          0, 1]])
    ans.append(is_rotation_matrix(mat))

    mat = np.array([[  np.cos(t), 0, np.sin(t)],
                    [          0, 1,         0],
                    [ -np.sin(t), 0, np.cos(t)]])
    ans.append(is_rotation_matrix(mat))

    t = m.radians(-15)
    mat = np.array([[ 1,          0,           0],
                   [ 0, np.cos(t), -np.sin(t)],
                   [ 0, np.sin(t),  np.cos(t)]])
    ans.append(is_rotation_matrix(mat))

    mat = np.array([[ np.cos(t), -np.sin(t), 0],
                    [ np.sin(t),  np.cos(t), 0],
                    [         0,          0, 1]])
    ans.append(is_rotation_matrix(mat))

    mat = np.array([[  np.cos(t), 0, np.sin(t)],
                    [          0, 1,         0],
                    [ -np.sin(t), 0, np.cos(t)]])
    ans.append(is_rotation_matrix(mat))

    t = m.radians(-111)
    mat = np.array([[ 1,          0,           0],
                    [ 0, np.cos(t), -np.sin(t)],
                    [ 0, np.sin(t),  np.cos(t)]])
    ans.append(is_rotation_matrix(mat))

    mat = np.array([[ np.cos(t), -np.sin(t), 0],
                    [ np.sin(t),  np.cos(t), 0],
                    [         0,          0, 1]])
    ans.append(is_rotation_matrix(mat))

    mat = np.array([[  np.cos(t), 0, np.sin(t)],
                    [          0, 1,         0],
                    [ -np.sin(t), 0, np.cos(t)]])
    ans.append(is_rotation_matrix(mat))

    t1 = m.radians(302)
    t2 = m.radians(30)
    t3 = m.radians(51)
    m1 = np.array([[ 1,          0,           0],
                   [ 0, np.cos(t1), -np.sin(t1)],
                   [ 0, np.sin(t1),  np.cos(t1)]])
    m2 = np.array([[ np.cos(t2), -np.sin(t2), 0],
                   [ np.sin(t2),  np.cos(t2), 0],
                   [          0,           0, 1]])
    m3 = np.array([[  np.cos(t3), 0, np.sin(t3)],
                   [           0, 1,          0],
                   [ -np.sin(t3), 0, np.cos(t3)]])
    mat = m1 @ m2 @ m3
    ans.append(is_rotation_matrix(mat))

    mat = np.array([[ 1, 0, 0],
                    [ 0, 1, 0],
                    [ 0, 0, 1]])
    ans.append(is_rotation_matrix(mat))

    mat = np.array([[  0, -1, 0],
                    [  0,  0, 1],
                    [ -1,  0, 0]])
    ans.append(is_rotation_matrix(mat))

    for i, answer in enumerate(ans):
        print(f"Matrix {i:>2}: {answer}")