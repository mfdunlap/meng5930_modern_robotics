#################### TRY-EXCEPT ####################
def find_color(color_name):                                                                         # Function: Find a color's position in the rainbow
    rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]                      # Initialize list of rainbow colors in order
    try:                                                                                            # Try to find the color's name in the list of rainbow colors
        rainbow_idx = rainbow.index(color_name.lower())                                                 # Find the color's index in the list of rainbow colors
        print(f"{color_name.capitalize()} is color number {rainbow_idx + 1} of the rainbow.")           # Print the color's position in the rainbow to the terminal by adding 1 to the index

    except ValueError:                                                                              # If the color's name is not found in the rainbow colors list
        print(f"{color_name.capitalize()} could not be found because it is not in the rainbow.")        # Print that color is not a rainbow color

find_color("Purple")                                                                                # Example: Color is in the rainbow
find_color("pink")                                                                                  # Example: Color is not in the rainbow