############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Homework 4: Orientation in Robotics (Exponential
#             Coordinates, and Euler Angles)
############################################################

import matplotlib.pyplot as plt
import numpy as np

def solve_matrix_exp(w_theta):
    # Solve for unit vector and theta
    t = np.sqrt(w_theta[0] ** 2 + w_theta[1] ** 2 + w_theta[2] ** 2)
    w = np.array(w_theta) / t

    w_hat_mat = np.array([[     0, -w[2],  w[1]],
                          [  w[2],     0, -w[0]],
                          [ -w[1],  w[0],     0]])
    
    e_wt = np.eye(3) + np.sin(t) * w_hat_mat + (1 - np.cos(t)) * (w_hat_mat @ w_hat_mat)
    display_rot_frame(e_wt, w)
    return (w[0], t * 180 / np.pi, e_wt)

def display_rot_frame(frame, w_hat):
    # Define origin
    origin = np.zeros(3)

    # Define rotated frame
    x_axis = frame[:, 0]
    y_axis = frame[:, 1]
    z_axis = frame[:, 2]

    # Visualize the frame and axis of rotation
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Draw rotated frame axes
    ax.quiver(*origin, *x_axis, color='r', label='X-axis')
    ax.quiver(*origin, *y_axis, color='g', label='Y-axis')
    ax.quiver(*origin, *z_axis, color='b', label='Z-axis')

    # Draw axis of rotation
    ax.quiver(*origin, *w_hat, color="k", label='w_hat')

    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()

    plt.show(block=False)
    return

if __name__ == "__main__":
    ans = solve_matrix_exp([1, 2, 0])
    print(ans)
    print("w_hat:", ans[0])
    print("theta:", ans[1])
    print("e_wt:", ans[2])
    input("Press [enter] to close graphs and end code.")