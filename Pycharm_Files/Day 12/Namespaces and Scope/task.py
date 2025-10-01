enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


def my_function():
    my_local_var: int = 2
# Will return a NameError because the variable does not exist in this scop just locally in the function.
print(my_local_var)


# This will print because the var being called is global. Meaning that it is available anywhere in the file
 my_global_var: int = 3
def my_other_function():
    print(my_global_var)