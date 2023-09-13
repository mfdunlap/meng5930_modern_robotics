############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Prerequisite 2: Introduction to Python Programming
#                 with Emphasis on Robotics Applications
############################################################

#################### NUMPY ####################

import numpy as np                                                  # Import numpy library
np.set_printoptions(precision=1)                                    # Set numpy print decimal place precision to one decimal place
np.random.seed(5930)                                                # Set seed for repeatability

vec1 = np.array(np.random.uniform(size=5, low=0, high=10))          # Create an numpy array of five random floats
print(vec1)                                                         # Print the numpy array
print(vec1.shape)                                                   # Print the size of the numpy array

vec2 = np.array(np.random.uniform(size=5, low=10, high=100))        # Create another numpy array of five random floats
print(vec2)                                                         # Print the numpy array
print(vec2.shape)                                                   # Print the size of the numpy array
print(vec2.T.shape)                                                 # Print the size of the transpose of the numpy array

print(vec2 - vec1)                                                  # Example: Subtraction of the two arrays
print(vec1 * vec2)                                                  # Example: Element-wise multiplication of the two arrays

print(np.matmul(vec1, vec2.T))                                      # Example: Matrix multiplication of vec1 and the transpose of vec2 - Method 1
print(np.matmul(vec1, np.transpose(vec2)))                          # Example: Matrix multiplication of vec1 and the transpose of vec2 - Method 2
print(vec1.T @ vec2)                                                # Example: Matrix multiplication of vec1 and the transpose of vec2 - Method 3

array_2d = np.array([np.random.uniform(size=5, low=0, high=10),     # Create a 2D-numpy array with three rows of five random floats
                     np.random.uniform(size=5, low=0, high=10),
                     np.random.uniform(size=5, low=0, high=10)])    
print(array_2d)                                                     # Print the 2D-numpy array
print(array_2d.shape)                                               # Print the shape of the 2D-numpy array