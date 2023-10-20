import numpy as np

def inverse_rotation_matrix(R): #    The inverse of a rotation matrix is simply its transpose.
    return R.T

if __name__ == "__main__":
    # function of R
    R = np.array([[0, -1, 0],
                [1, 0, 0],
                [0, 0, 1]])

    R_inverse = inverse_rotation_matrix(R)
    print("Inverse of R is:")
    print(R_inverse)
