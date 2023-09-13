#################### READING FILES ####################

with open("Prereq2_Intro_to_Python_Programming/sensor_data.txt", "r") as file:  # Open listed file w/ read-only permission
    for line in file:                                                           # For each line in the file:
        timestamp, temperature = line.strip().split(", ")                           # Split the text on the ", " delimiter
        print(f"Timestamp: {timestamp}")                                            # Print the timestamp
        print(f"Temperature:  {temperature} °C")                                    # Print the temperature with units 