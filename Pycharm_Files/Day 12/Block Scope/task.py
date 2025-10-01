# There is no block scope in Python

# This means that variables created nested in other blocks of code
# e.g. for loops, if statements, while loops etc. don't get local scope.
# They are given function scope if they are within a function or global scope
# if they are not

# Accessible anywhere
my_global_var = 1

def my_function():
    # Only accessible within my_function()
    my_local_var = 2

for _ in range(10):
    # Accessible anywhere
    my_block_var = 3


