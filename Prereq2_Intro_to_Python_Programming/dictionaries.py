#################### CREATING DICTIONARIES ####################
main_ingredients = {"chocolate" : "cocoa",                                                  # Initialize dictionary with items
                    "hummus" : "chickpeas",
                    "lemonade" : "lemons",
                    "caesar dressing" : "anchovies"}

print("The main ingredient in chocolate is " + main_ingredients["chocolate"])               # Example: Access the value of a key
print("The main ingredient in caesar dressing is " + main_ingredients["caesar dressing"])   # Example: Access the value of a different key

print(main_ingredients.get("lime", "not in dictionary"))                                    # Example: Try to access key that is not in the dictionary w/ a failure message

#################### NESTED DICTIONARIES ####################

person_list = {                                                                             # Initialize a dictionary that has dictonary items
    "matt" : {
        "height" : 61,
        "age" : 36,
        "hometown" : "Lexington. KY"
    },

    "sarah" : {
        "height" : 68,
        "age" : 25,
        "hometown" : "Denver. CO"
    },

    "lucas" : {
        "height" : 77,
        "age" : 18,
        "hometown" : "Fort Wayne, IN"
    },

    "taylor" : {
        "height" : 72,
        "age" : 74,
        "hometown" : "Henderson, NV"
    },
}

print(person_list["taylor"])                                                                # Example: Access a value in the dictionary
print(person_list["matt"]["age"])                                                           # Example: Access the age value from the nested dictionary
print(person_list["sarah"]["height"])                                                       # Example: Access the height value from the nested dictonary
print(person_list["lucas"]["hometown"])                                                     # Example: Access the hometown value from the nested dictionary