programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# Will print the value of the key
print(programming_dictionary["Bug"])

# creating an empty dictionary
colors: dict = {}

# Populating it with something
# Dictionary[Key] = Value
colors["peach"]: str = "pink"
colors["Pear"]: str ="green"

print(colors)

# Changing the value of an item in the dictionary
colors["peach"]: str = "orange"
print(colors)

# Looping through and printing the keys
for key in colors:
    print(key)

# printing out the values
for key in colors:
    print(colors[key])

# This is a another way of getting a specific piece of data
print(f"Printing out using 'colors.get()':  {colors.get('peach')}")


# wiping out existing dictionary
colors = {}
colors.clear()
print(colors)

# removing a specific entry by Key
programming_dictionary.pop('Bug')
print(programming_dictionary)