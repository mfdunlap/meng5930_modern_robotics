import numpy as np

def vector_to_skew(omega):

    skew_matrix = np.array([
        [0, -omega[2], omega[1]],
        [omega[2], 0, -omega[0]],
        [-omega[1], omega[0], 0]
    ])
    return skew_matrix

if __name__ == "__main__":
    # Test the function
    omega = np.array([1, 2, 3])
    skew_matrix = vector_to_skew(omega)
    print("The 3x3 skew-symmetric matrix representation is:")
    print(skew_matrix)
