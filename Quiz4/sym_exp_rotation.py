############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Lab 7: Tool Orientation of PincherX 100 Robot Arm Using
#        Exponential Coordinates and Euler Angles Exercise
#        Question
# Copyright 2022 Trossen Robotics
############################################################

import sympy as sp

# Define symbolic variables
t1, t2, t3 = sp.symbols('a b g')

# Define the skew-symmetric matrices
z_hat_bracket = sp.Matrix(3, 3, [0, -1, 0, 1, 0, 0, 0, 0, 0])
x_hat_bracket = sp.Matrix(3, 3, [0, 0, 0, 0, 0, -1, 0, 1, 0])

# Calculate e_bracket_z_t1
e_bracket_z_t1 = sp.eye(3) + sp.sin(t1) * z_hat_bracket + (1 - sp.cos(t1)) * (z_hat_bracket @ z_hat_bracket)

# Calculate e_bracket_y_t2
e_bracket_y_t2 = sp.eye(3) + sp.sin(t2) * x_hat_bracket + (1 - sp.cos(t2)) * (x_hat_bracket @ x_hat_bracket)

# Calculate e_bracket_y_t3
e_bracket_y_t3 = sp.eye(3) + sp.sin(t3) * z_hat_bracket + (1 - sp.cos(t3)) * (z_hat_bracket @ z_hat_bracket)

# Calculate the final result
result = e_bracket_z_t1 @ e_bracket_y_t2 @ e_bracket_y_t3

# Simplify the result
simplified_result = sp.simplify(result)

# Display the simplified result
print(simplified_result)