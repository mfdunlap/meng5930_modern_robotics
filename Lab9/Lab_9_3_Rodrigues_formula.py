import numpy as np
import math

def vector_to_skew(omega):
    """Convert a 3-vector to its 3x3 skew-symmetric matrix."""
    return np.array([
        [0, -omega[2], omega[1]],
        [omega[2], 0, -omega[0]],
        [-omega[1], omega[0], 0]
    ])

def rodrigues_rotation(theta, omega):

    I = np.identity(3)
    skew_omega = vector_to_skew(omega)
    R = I + np.sin(theta) * skew_omega + (1 - np.cos(theta)) * np.dot(skew_omega, skew_omega)
    return R

if __name__ == "__main__":
    # Test the function
    theta = math.pi / 4  # 45 degrees in radians
    omega = np.array([0, 0, 1])  # Rotation about the z-axis

    R = rodrigues_rotation(theta, omega)
    print("The rotation matrix R is:")
    print(R)

    # Test the function
    theta = math.pi  # 90 degrees in radians
    omega = np.array([0, 0, 1])  # Rotation about the z-axis

    R = rodrigues_rotation(theta, omega)
    print("The rotation matrix R is:")
    print(R)

    # Test the function
    theta = 2*math.pi  # 180 degrees in radians
    omega = np.array([0, 0, 1])  # Rotation about the z-axis

    R = rodrigues_rotation(theta, omega)
    print("The rotation matrix R is:")
    print(R)
