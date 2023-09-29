import numpy as np
import math as m
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)

# Define joint angles in radians
theta_1 = m.radians(-90)
theta_2 = m.radians(-135)

print(theta_1, theta_2)

rot_x_theta2 = np.array([[ 1,               0,                0],
                         [ 0, np.cos(theta_2), -np.sin(theta_2)],
                         [ 0, np.sin(theta_2),  np.cos(theta_2)]])
print(rot_x_theta2)

rot_z_theta1 = np.array([[ np.cos(theta_1), -np.sin(theta_1), 0],
                         [ np.sin(theta_1),  np.cos(theta_1), 0],
                         [               0,                0, 1]])
print(rot_z_theta1)

rot1 = np.array([[  0,  0, 1],
                 [ -1,  0, 0],
                 [  0, -1, 0]])

eye = np.eye(3)

rot_0_1 = np.matmul(rot_z_theta1, rot_x_theta2)


print(f"Rotation Matrix: {rot_0_1}")


# Create vectors for the coordinate frame
origin = np.zeros(3)
x_axis = rot_0_1[:, 0]
y_axis = rot_0_1[:, 1]
z_axis = rot_0_1[:, 2]

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
