#################### WHILE LOOPS ####################
import time                                                                                 # Import necessary libraries
import random

def is_redlight():                                                                          # Function: Determine if a light is red or green
    is_red = random.choices(population=[True, False],                                       # Make a weigthed random choice of if the light is red (True) or green (False)
                            weights=[0.25, 0.75],
                            k=1)
    return is_red[0]                                                                        # Return: True/False boolean choice 

def travel_distance():                                                                      # Function: Determine the distance a car traveled before reaching their first red light
    total_distance = 0                                                                      # Intialize total_distance moved as 0
    lights = 0                                                                              # Intialize total number of lights the car has passed as 0
    while not is_redlight():                                                                # While the light is not red:
        driven_distance = round(random.randint(25,200))                                         # Simulate a distance driven between lights
        time.sleep(0.5)
        print(f"The car drove {driven_distance} meters.")                                       # Print distance driven to the terminal
        total_distance += driven_distance                                                       # Add distance driven to the total distance
        lights += 1                                                                             # Increase the number of light passed by 1

    print("The car reached a red light.")                                                   # Print that the car has reached a red light
    print(f"The car passed through {lights} lights before reaching the first red light.")   # Print the number of lights passed before reaching the red light
    print(f"The car drove {total_distance} meters.")                                        # Print total distanced traveled before the red light

travel_distance()                                                                           # Example using the travel_distance function

#################### FOR LOOPS ####################
for c in "mushroom":                                                                        # Example: Iterate through the characters in a string
    print(c)

words = ["economist", "roll", "island", "quality", "goat"]                                  # Example: Iterate through the items in a list
for word in words:
    print(word.count("i"))

for idx in range(len(words)):                                                               # Example: Use the range function to set the number of iterations
    print(words[idx], idx, words[idx].count("e"))

for num in range(13, 25):                                                                   # Example: Use the range function to iterate through a range of number values
    print(num**2)

#################### NESTED LOOPS ####################

words = ["economist", "roll", "island", "quality", "goat"]                                  # Initialize list of words
vowels = ["a", "e", "i", "o", "u"]                                                          # Initialize list of vowels
for word in words:                                                                          # For each word in the word list:
    print(word.upper())                                                                         # Print the word in uppercase
    for vowel in vowels:                                                                        # For each vowel in the vowel list:
        print(f"{vowel}: {word.count(vowel)}")                                                      # Count the number of times the vowel appears in the word