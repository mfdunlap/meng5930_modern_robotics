import numpy as np
import math as m
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)

# Define joint angles in radians
theta_1 = m.radians(90)
theta_2 = m.radians(-45)
theta_3 = m.radians(0)
theta_4 = m.radians(45)

print(theta_1, theta_2, theta_3, theta_4)

rot_z_theta1 = np.array([[ np.cos(theta_1), -np.sin(theta_1), 0],
                         [ np.sin(theta_1),  np.cos(theta_1), 0],
                         [               0,                0, 1]])

rot_y_theta2 = np.array([[  np.cos(theta_2), 0, np.sin(theta_2)],
                         [                0, 1,              0],
                         [ -np.sin(theta_2), 0, np.cos(theta_2)]])

rot_y_theta3 = np.array([[  np.cos(theta_3), 0, np.sin(theta_3)],
                         [                0, 1,              0],
                         [ -np.sin(theta_3), 0, np.cos(theta_3)]])

rot_y_theta4 = np.array([[  np.cos(theta_4), 0, np.sin(theta_4)],
                         [               0,  1,              0],
                         [ -np.sin(theta_4), 0, np.cos(theta_4)]])

eye = np.eye(3)

rot_0_2 = np.matmul(rot_z_theta1, rot_y_theta2)
rot_0_3 = np.matmul(rot_0_2, rot_y_theta3)
rot_0_4 = np.matmul(rot_0_3, rot_y_theta4)
rot_0_5 = np.matmul(rot_0_4, eye)

print(rot_0_5)

# Create vectors for the coordinate frame
origin = np.zeros(3)
x_axis = rot_0_5[:, 0]
y_axis = rot_0_5[:, 1]
z_axis = rot_0_5[:, 2]

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



