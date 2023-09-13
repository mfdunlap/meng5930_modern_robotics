#################### WRITING FUNCTIONS ####################

def multipy(num1, num2):                        # Function: Multiply two numbers
    return num1 * num2                          # Return: Product of the two numbers

print(multipy(-36, 0.75))                       # Example: Multiply two numbers and print the returned value

import math as m                                # Import necessary libraries
def cylinder_volume(radius, height):            # Function: Calculate the volume of a cylinder with a given radius and height
    return m.pi * (radius ** 2) * height        # Return: The volume of the cylinder

volume = cylinder_volume(6, 15.25)              # Example: Calculate the volume of a cylinder and print it to the terminal
print("The volume of the cylinder is", volume)  
