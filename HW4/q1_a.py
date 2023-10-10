############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Homework 4: Orientation in Robotics (Exponential
#             Coordinates, and Euler Angles)
############################################################

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def solve_matrix_log(matrix):
    # Solve for the sine of theta
    r_11 = matrix[0, 0]
    r_22 = matrix[1, 1]
    r_33 = matrix[2, 2]

    theta1 = np.arccos((r_11 + r_22 + r_33 - 1)/2)

    # Check for special cases
    ## Special case 1: k is even integer --> theta = 0, 2pi; w = undefined
    if (theta1/np.pi) % 2 == 0.0:
        ans = set()
        ans.add((0.0, None, None, None))
        ans.add((360.0, None, None, None))

    ## Special case 2: k is odd integer --> theta = pi
    elif (theta1/np.pi) % 2 == 1.0:
        ans = solve_case1(matrix)

    # Solve for regular case
    else:
        theta = [theta1, -theta1]
        ans = solve_regular(matrix, theta)

    display_axis(ans)
    return ans


def solve_regular(matrix, theta):
    ans = set()
    
    # Define symbolic variables
    w_1, w_2, w_3, = sp.symbols('w1 w2 w3')

    # Define constants
    r_12 = matrix[0, 1]
    r_13 = matrix[0, 2]
    r_21 = matrix[1, 0]
    r_23 = matrix[1, 2]
    r_31 = matrix[2, 0]
    r_32 = matrix[2, 1]

    # Solve 
    for t in theta:
        # Define system of equations
        eq1 = sp.Eq((r_32 - r_23) / (2 * np.sin(t)), w_1)
        eq2 = sp.Eq((r_13 - r_31) / (2 * np.sin(t)), w_2)
        eq3 = sp.Eq((r_21 - r_12) / (2 * np.sin(t)), w_3)

        # Solve system of equations
        solution = sp.solvers.solve([eq1, eq2, eq3], dict=True)
        for s in solution:
            t_round = np.round(t * 180 / np.pi, 3)
            ans.add((t_round, s[w_1], s[w_2], s[w_3]))
    return ans


def solve_case1(matrix):
    ans = set()

    # Define symbolic variables
    w_1, w_2, w_3, = sp.symbols('w1 w2 w3')
   
    # Define constants
    r_12 = matrix[0, 1]
    r_13 = matrix[0, 2]
    r_23 = matrix[1, 2]
    r_11 = matrix[0, 0]
    r_22 = matrix[1, 1]
    r_33 = matrix[2, 2]

    eq1 = sp.Eq(2 * (w_1 ** 2) - 1, r_11)
    eq2 = sp.Eq(2 * (w_2 ** 2) - 1, r_22)
    eq3 = sp.Eq(2 * (w_3 ** 2) - 1, r_33)
    eq4 = sp.Eq(2 * w_1 * w_2, r_12)
    eq5 = sp.Eq(2 * w_1 * w_3, r_13)
    eq6 = sp.Eq(2 * w_2 * w_3, r_23)

    solution = sp.solvers.solve([eq1, eq2, eq3, eq4, eq5, eq6], dict=True)
    for s in solution:
            t_round = np.round(np.pi * 180 / np.pi, 3)
            ans.add((t_round, float(s[w_1]), float(s[w_2]), float(s[w_3])))
    return ans


def display_axis(sol_set):
    # Create origin and fixed frame axis
    origin = np.zeros(3)
    x_axis = [1, 0, 0]
    y_axis = [0, 1, 0]
    z_axis = [0, 0, 1]

    # Create plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Draw fixed frame axes
    ax.quiver(*origin, *x_axis, color='r', label='X-axis')
    ax.quiver(*origin, *y_axis, color='g', label='Y-axis')
    ax.quiver(*origin, *z_axis, color='b', label='Z-axis')

    # Draw each solution
    colors = ["k", "c", "m", "y"]
    for i, sol in enumerate(sol_set):
        if not any(w is None for w in sol):
            sol_vect = sol[1:]
            ax.quiver(*origin, *sol_vect, color=colors[i], label='Sol'+str(i))
        else:
            ax.text(0.0, -1.0, -0.75, "No solutions found.")

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
    # Solve Q1a
    mat = np.array([[ 0, -1,  0],
                    [ 0,  0, -1],
                    [ 1,  0,  0]])
    ans = solve_matrix_log(mat)
    print("Solutions:")
    for a in ans:
        print(a)

    # Solve Q2a
    mat = np.array([[ 0,  0, 1],
                    [ 0, -1, 0],
                    [ 1,  0, 0]])
    ans = solve_matrix_log(mat)
    print("Solutions:")
    for a in ans:
        print(a)

    input("Press [enter] to close graphs and end code.")