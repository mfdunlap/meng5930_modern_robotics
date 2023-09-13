#################### IF-ELSE ####################
def is_recyclable(material):                                            # Function: Check if material is recyclable
    if material.lower() in ["glass", "plastic", "aluminum", "paper"]:   # If material is recyclable:
        return "This material is recyclable."                               # Return: Recyclable message
    else:                                                               # If material is not recyclable:
        return "This material is not recyclable."                           # Return: Non-recyclable message

print("Paper:", is_recyclable("Paper"))                                 # Example of recyclable material
print("Ceramic:", is_recyclable("Ceramic"))                             # Example of non-recyclable material

#################### IF-ELIF-ELSE ####################
def max_num(num1, num2, num3):                                          # Return the largest number out of a group of three
    if num1 > num2 and num1 > num3:                                     # IF the first number is the largest:
        return "The largest number is " + str(num1)                         # Return: First number is the largest message
    
    elif num2 > num1 and num2 > num3:                                   # IF the second number is the largest:
        return "The largest number is " + str(num2)                         # Return: Second number is the largest message
    
    elif num3 > num1 and num3 > num2:                                   # IF the third number is the largest:
        return "The largest number is " + str(num3)                         # Return: Third number is the largest message
    
    else:                                                               
        return "All three numbers are equal"                            # Return: All numbers are equal message
    
print(max_num(33, 10, 62))                                              # Example of third number being the largest
print(max_num(19, 30, 2))                                               # Example of second number being the largest
print(max_num(85, 13, 82))                                              # Example of first number being the largest
print(max_num(71, 71, 71))                                              # Example of equal numbers