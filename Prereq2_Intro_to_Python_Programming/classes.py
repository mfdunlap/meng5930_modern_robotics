############################################################
# Maya Dunlap
# MENG 5930 - Modern Robotics
# Prerequisite 2: Introduction to Python Programming
#                 with Emphasis on Robotics Applications
############################################################

#################### BASIC CLASSES ####################
class Dog:                                                                          # DOG CLASS
    def __init__(self, name, breed, age):                                           # Function: Initialize instance of Dog class
        self.name = name                                                            # Initialize attributes (name, breed, age)
        self.breed = breed
        self.age = age

    def change_name(self, name):                                                    # Function: Change name attribute
        old_name = self.name                                                        # Saveold name in temp var
        self.name = name                                                            # Update name attribute
        print(f"The dog's name has been changed from {old_name} to {self.name}.")   # Print name change to terminal
    
    def get_name(self):                                                             # Function: Get name attribute
        return self.name                                                            # Return: name attrinute
    
    def display_info(self):                                                         # Function: Print attributes to the terminal
        print(f"Name: {self.name}")                                                 # Print each attribute to terminal
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years")

new_dog = Dog("Marvin", "Pug", 3)                                                   # Create instance of dog class
new_dog.change_name("Doug")                                                         # Use name change function

#################### INHERITED CLASSES ####################
class Dalmation(Dog):                                                               # DALMATION CLASS (Inherited from Dog class)
    def __init__(self, name, age, height):                                          # Function: Initialize instance Dalmation class
        super().__init__(name, "Dalmation", age)                                    # Inherit behavior of the Dog __init__ function
        self.height = height                                                        # Initialize height attribute

    def size_comparison(self):                                                      # Function: Compare instance's height to the avg Dalmation height
        if self.height < 70:                                                        # Print short message if instance is shorter than avg
            print("I am short for a dalmation.")
        elif self.height > 76:                                                      # Print tall message if instance if taller than avg
            print("I am tall for a dalmation.")
        else:                                                                       # Print average message if instance is avg
            print("I am average size for a dalmation.")

    def get_name(self):                                                             # Funvtion: Get name attribute
        print(f"I am a dalmation named {self.name}.")                               # Print message about name
        return super().get_name()                                                   # Inherit behavior of the Dog get_name function
    
    def display_info(self):                                                         # Function: Print attributes to the terminal
        super().display_info()                                                      # Inherit behavior of the Dog display_info function
        print(f"Height: {self.height} cm")                                          # Print height attribute to the terminal
    
dalmation_dog = Dalmation("Shadow", 6, 68)                                          # Create instance of Dalmation class
print(dalmation_dog.get_name())                                                     # Use get name function
dalmation_dog.size_comparison()                                                     # Use size_comparison function