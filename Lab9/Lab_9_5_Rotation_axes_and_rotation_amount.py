import numpy as np

def extract_axis_and_angle(omega_theta):

    theta = np.linalg.norm(omega_theta)
    if theta == 0:
        raise ValueError("The rotation amount theta cannot be zero.")
        
    omega_hat = omega_theta / theta
    
    return omega_hat, theta

# Test the function
omega_theta = np.array([1, 2, 3])
omega_hat, theta = extract_axis_and_angle(omega_theta)

print("The rotation axis (omega_hat) is:", omega_hat)
print("The rotation amount (theta) is:", theta)
