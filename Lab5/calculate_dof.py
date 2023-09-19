def main():
    quit_prog = False
    m = None
    N = None
    J = None
    joint_dofs = list()

    while not quit_prog:
        while not m:
            m = get_dimensions()
        
        while not N:
            N = get_links()

        while not J or not joint_dofs:
            J, joint_dofs = get_joints()

        mech_dof = m * (N - 1 - J) + sum(joint_dofs)
        print(f"This is a {mech_dof} DOF mechanism.")
        
        cont = input("To calculate another mechanism's DOF press enter. To quit the program type 'q' or 'quit'. ").lower()
        if cont in ["q", "quit"]:
            quit_prog = True
        else:
            m = None
            N = None
            J = None
            joint_dofs = list()


def get_dimensions():
    dimensions = input("Is this mechanism operating in 2D or 3D space: ").lower()
    if dimensions == "2d":
        return 3
    elif dimensions == "3d":
        return 6
    else:
        print("ValueError: Please answer with either '2D' or '3D'.")
        return
    

def get_links():
    try:
        n_links = int(input("How many links does this mechanism have: "))
        return n_links

    except ValueError:
        print("ValueError: All values must be integers.")
        return None


def get_joints():
    try:
        n_joints = int(input("How many joints does this mechanism have: "))
        # TODO: MAKE JOINTS_DOFS A LIST OF ZEROS THAT HAS 
        joint_dofs = [0 for i in range(n_joints)]
        
        for n in range(n_joints):
            while joint_dofs[n] == 0:
                joint_dof = input(f"How many DOFs does joint {n+1} have: ")
                if joint_dof not in ["1", "2", "3"]:
                    print("ValueError: Individual joints must have DOF values of 1, 2, or 3.")
                else:
                    joint_dofs[n] = int(joint_dof)
    
    except ValueError:
        print("ValueError: All values must be integers.")
        return None, None
    

    return n_joints, joint_dofs


#################### TEST/RUN CODE ####################
if __name__=='__main__':
    main()