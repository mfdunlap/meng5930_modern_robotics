#################### LISTS ####################

computer_parts = ["CPU", "GPU", "Motherboard", "Fan"]       # Initialize a list

print(computer_parts[3])                                    # Get element in a list
print(computer_parts[:2])                                   # Get a range of elements in a list

computer_parts.append("SSD")                                # Add an element to the end of a list
print(computer_parts)

computer_parts.remove("GPU")                                # Remove an element from  a list
print(computer_parts)

computer_parts.insert(0, "GPU")                             # Add an element to a certain position in a list
print(computer_parts)

computer_parts.sort()                                       # Organize a list alphabetically
print(computer_parts)

computer_parts.reverse()                                    # Reverse the order of a list
print(computer_parts)

print(len(computer_parts))                                  # Get the length of a list

fruits1 = ["apple", "orange", "kiwi"]                       # Initialize two lists
fruits2 = ["mango", "papaya", "lemon", "lime"]

fruits1.extend(fruits2)                                     # Concatenate two lists
print(fruits1)

fruits1.pop()                                               # Remove the last element of a list
print(fruits1)

print(fruits1.index("mango"))                               # Find the index of an element in a list

print(fruits1.count("lime"))                                # Count the number of times an element appears in a list

fruits1_copy = fruits1.copy()                               # Make a copy of a list
print(fruits1)
print(fruits1_copy)
print(fruits1==fruits1_copy)                                # Determine if two lists are equivalent

for fruit in fruits1:                                       # Iterate through a list
    print(fruit)

fruits1_copy.clear()                                        # Clear all elements from a list
print(fruits1)
print(fruits1_copy)

#################### 2D LISTS ####################

colors = [["red", "yellow", "blue"],                        # Initialize a 2D-list
          ["orange", "green", "purple"],
          ["white", "gray", "black"]]

print(colors)                                               # Print the list to the terminal
print(colors[0])                                            # Access a row of the 2D-list (1st row)
print(colors[1][2])                                         # Access a particular element of the 2d-list (2nd row, 3rd column)

#################### TUPLES ####################

transport = ("car", "train", "plane", "walk")               # Initialize a tuple

print(transport)                                            # Print the tuple to the terminal
print(transport[1])                                         # Access a particular element of the tuple (2nd element)

t1, t2, t3, t4 = transport                                  # Assign each element of the tuple to a variable
print(t1, t2, t3, t4)                                       # Print all element from their variable names
print(t4)                                                   # Print a single element from its variable name

try:
    transport[3] = "motorcycle"                             # Try to add a new element to a tuple
except:
    print("Error: You cannot change an immutable object!")  # Print error message for immutable object

transport_speed = [("car", "medium"),                       # Initialize a list w/ tuple elements
                   ("train", "medium"),
                   ("plane", "fast"),
                   ("walk", "slow")]
print(transport_speed)                                      # Print list to the terminal
print(transport_speed[2])                                   # Access a tuple item