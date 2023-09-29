import numpy as np
import math as m
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)

# Define rotation matrix
rot_mat = np.array([[ 0.866,  -0.5, 0],
                    [   0.5, 0.866, 0],
                    [     0,     0, 1]])

# Create vectors for the coordinate frame
origin = np.zeros(3)
x_axis = rot_mat[:, 0]
y_axis = rot_mat[:, 1]
z_axis = rot_mat[:, 2]

# Visualize the coordinate frame
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(*origin, *x_axis, color='r', label='X-axis')
ax.quiver(*origin, *y_axis, color='g', label='Y-axis')
ax.quiver(*origin, *z_axis, color='b', label='Z-axis')

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()

