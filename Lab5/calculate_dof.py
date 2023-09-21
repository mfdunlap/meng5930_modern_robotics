def main():
    # Initialize variables
    quit_prog = False
    m      = None
    N      = None
    J      = None
    j_1dof = None
    j_2dof = None
    j_3dof = None

    # Make program runnable for multiple calculations
    while not quit_prog:
        # Get m (number of DoF for a single body)
        while not m:
            m = get_dimensions()
        
        # Get N (number of links)
        while not N:
            N = get_links()

        # Get J (number of joints) and number of joints w/ 1, 2, and 3 DoF
        while not any([J, j_1dof, j_2dof, j_3dof]):
            J, j_1dof, j_2dof, j_3dof = get_joints()

        # Calculate mechanism DoF
        mech_dof = m * (N - 1 - J) + j_1dof + 2 * (j_2dof) + 3 * (j_3dof)
        print(f"This is a {mech_dof} DOF mechanism.")

        # Ask if user wants to make another DoF calculation
        cont = input("To calculate another mechanism's DOF press enter. To quit the program type 'q' or 'quit'. ").lower()
        if cont in ["q", "quit"]:
            quit_prog = True
        else:
            m = None
            N = None
            J = None
            j_1dof = None
            j_2dof = None
            j_3dof = None


def get_dimensions():
    try:
        dimensions = int(input("How many DoFs does a single body have: "))
        if dimensions not in [3, 6]:
            raise ValueError()
        else:
            return dimensions
        
    except ValueError:
        print("Error: Single bodies can only have 3 (2D space) or 6 (3D space) DoF.")
        return

    

def get_links():
    try:
        n_links = int(input("How many links does this mechanism have: "))
        return n_links

    except ValueError:
        print("Error: All values must be integers.")
        return None


def get_joints():
    try:
        joints_valid = False
        while not joints_valid:
            n_joints = int(input("How many joints does this mechanism have: "))
            n_1dof   = int(input("How many joints have 1 DoF: "))
            n_2dof   = int(input("How many joints have 2 DoF: "))
            n_3dof   = int(input("How many joints have 3 DoF: "))
            
            if n_1dof + n_2dof + n_3dof != n_joints:
                print("Error: The meachanism's total number of joints must equal the sum of 1, 2, and 3 DoF joints")
            else:
                joints_valid = True
    
    except ValueError:
        print("Error: All values must be integers.")
        return None, None, None, None
    

    return n_joints, n_1dof, n_2dof, n_3dof


#################### TEST/RUN CODE ####################
if __name__=='__main__':
    main()