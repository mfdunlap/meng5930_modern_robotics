#################### NATIVE PYTHON MATH ####################

num_int = 47                                                                        # Initialize int var
num_float = 5.7                                                                     # Initialize float var

print(num_int ** (num_int - num_float))                                             # Basic arithmetic example
print(num_int % 3)                                                                  # Modulus example
print(max(num_int, 1000))                                                           # Find largest number example
print(min(num_int, 16, 90, 5))                                                      # Find smallest number example
print(abs(-num_int))                                                                # Absolute value example
print(pow(num_int, 3))                                                              # Power example
print(round(num_float))                                                             # Rounding example

#################### MATH LIBRARY ####################

from math import *                                                                  # Import all functions/classes math library

print(floor(num_float))                                                             # Round down example
print(ceil(num_float))                                                              # Round up example
print(sqrt(num_int))                                                                # Sqaure root example
print(exp(num_int))                                                                 # Exponential example

import math as m                                                                    # Import math library with an alias

print(m.exp(num_int))                                                               # Exponential example using math import
print("If there are " + str(num_int) + " robots in the room. Then on average "\
      + str(num_float) + " of them will be named Ro-Bob!")                          # Printing numbers/variables in a string example

#################### STRINGS ####################

robot_name = "Ro-Bobert 2.0"                                                        # Initialize string var

print("All new version of this robot will be named " + robot_name + ".")            # Inserting string variable into a string
print("The new robot's first initial is " + robot_name[0] + ".")                    # Printing a substring
print(robot_name.lower())                                                           # Printing a lowercase version of a string
print("Lowercase Robot Name: " + str(robot_name.islower()))                         # Checking if a string is completely lowercase
print("Uppercase Robot Name: " + str((robot_name.upper()).isupper()))               # Checking if a string is completely uppercase
print("Robot Name Length: " + str(len(robot_name)))                                 # Finding the length of a string
print(robot_name.index("t"))                                                        # Finding the first instance of a character in a string
print(robot_name.replace("Ro-Bobert", "Robotony"))                                  # Replacing a substring in a string
