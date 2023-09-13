#################### USER INPUT ####################
print("Hi! My name is CMPTR1 and I'm trying to learn more about you.")                  # Example: Use the input function to get information about a user
name = input("What is your name: ")                                                         # User's name
print(f"Hello {name}! Nice to meet you!")

ice_cream = input("What is your favorite flavor of ice cream: ")                            # User's favorite ice cream flavor
if ice_cream.lower() == "mint chocolate chip":
    print("I think mint chocolate chip is a terrible flavor. More for you I guess.")
else:
    print(f"{ice_cream.capitalize()} is a pretty good flavor.")

color = input("Last Question.\nWhat is your favorite color: ")                              # User's favorite color
print("Thank you for the info. Goodbye!")