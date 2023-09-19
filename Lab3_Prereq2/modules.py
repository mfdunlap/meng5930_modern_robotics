############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Prerequisite 2: Introduction to Python Programming
#                 with Emphasis on Robotics Applications
############################################################

#################### IMPORTING MODULES ####################
import functions as fun         # Import the function.py module with an alias
print(fun.multipy(5, 2.5))      # Use the multiply function from the function module

#################### ACCESSING MODULE OBJECTS ####################
import classes as my_class      # Import the classes.py function with an alias
d_dog = my_class.dalmation_dog  # Acess the dalmation dog object from the classes module
d_dog.display_info()            # Use the display info function from the dalmation dog class
