############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Lab 10: PincherX 100 Robot Arm's Forward Kinematics Using
#         Screw Theory
############################################################

import numpy as np
np.set_printoptions(precision=3, suppress=True)

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
        
        #print("Sv:", Sv)
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
    t1 = np.deg2rad(-39)
    t2 = np.deg2rad(-31)
    t3 = np.deg2rad(-41)
    t4 = np.deg2rad(180)
    t5 = np.deg2rad(-55)
    t6 = np.deg2rad(85)
    q  = [t1, t2, t3, t4, t5, t6]

    a   = np.array([[ 0, 0,      0],
                    [ 0, 0,  284.8],
                    [ 0, 0,  694.8],
                    [ 0, 1,      0],
                    [ 0, 0, 1009.1],
                    [ 0, 1,      0]])
    rot = np.array([[0,  0,  1],
                    [0,  1,  0],
                    [0, -1,  0],
                    [0,  0, -1],
                    [0, -1,  0],
                    [0,  0, -1]])
    jt  = ["R", "R", "R", "R", "R", "R"]
    M   = np.array([[-1, 0, 0,      0],
                    [0, -1, 0,      1],
                    [0, 0,  1, 1176.5],
                    [0, 0,  0,      1]])
    
    ans = fk_poe(q, a, rot, jt, M)
    print("Transformation Matrix:")
    print(ans[0])
    print("Rotation Matrix:")
    print(ans[1])
    print("Translation Vector:")
    print(ans[2])
    