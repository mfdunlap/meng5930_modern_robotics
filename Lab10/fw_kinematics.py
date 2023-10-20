############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Lab 10: PincherX 100 Robot Arm's Forward Kinematics Using
#         Screw Theory
############################################################

import numpy as np
np.set_printoptions(suppress=True)

def poe(q, a, rot, joint_type):
    T = np.eye(4)
    for i in range(len(q)):
        j = len(q) - i - 1
        if joint_type[j] == "R":
            rot_i = np.array([[         0, -rot[j][2],  rot[j][1]],
                              [ rot[j][2],          0, -rot[j][0]],
                              [-rot[j][1],  rot[j][0],          0]])
            rot_mat_i = np.eye(3) + np.sin(q[j]) * rot_i + (1 - np.cos(q[j])) * (rot_i @ rot_i)
        elif joint_type[j] == "P":
            rot_i = np.zeros(3)
            rot_mat_i = np.eye(3)

        if joint_type[j] == "R" and j > 0:
            Sv = -np.cross(rot[j], a[j])
        elif joint_type[j] == "R" and j == 0:
            Sv = np.array([0, 0, 0])
        elif joint_type[j] == "P":
            Sv = a[j]
        
        lin_vec_i = ((np.eye(3) * q[j]) + ((1 - np.cos(q[j])) * rot_i) + ((q[j] - np.sin(q[j])) * (rot_i @ rot_i))) @ Sv
        trans_mat_i = np.column_stack([rot_mat_i, lin_vec_i.T])
        trans_mat_i = np.vstack((trans_mat_i, np.array([0, 0, 0, 1])))

        T = trans_mat_i @ T
    
    return T

def fk_poe(q, a, rot, joint_type, M):
    T = poe(q, a, rot, joint_type)
    trans_mat = T @ M
    R = trans_mat[:3,:3]
    p = trans_mat[:3, 3]
    return trans_mat, R, p

if __name__ == "__main__":
    t1 = 0.0
    t2 = 0.0
    t3 = -np.pi/2
    t4 = np.pi/2
    q  = [t1, t2, t3, t4]
    H1 = 89.45
    H2 = 100
    L1 = 35
    L2 = 100
    L3 = (86.05 + 129.15)/2

    a   = np.array([[    0, 0,     0],
                    [    0, 0,    H1],
                    [   L1, 0, H1+H2],
                    [L1+L2, 0, H1+H2]])
    rot = np.array([[0, 0, 1],
                    [0, 1, 0],
                    [0, 1, 0],
                    [0, 1, 0]])
    jt  = ["R", "R", "R", "R"]
    M   = np.array([[1, 0, 0, L1+L2+L3],
                    [0, 1, 0,        0],
                    [0, 0, 1,    H1+H2],
                    [0, 0, 0,        1]])
    
    ans = fk_poe(q, a, rot, jt, M)
    print("Transformation Matrix:")
    print(ans[0])
    print("Rotation Matrix:")
    print(ans[1])
    print("Translation Vector:")
    print(ans[2])
    