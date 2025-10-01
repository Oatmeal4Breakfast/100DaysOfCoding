import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Generate random number
# rand_int = random.randint(0,len(friends) -1)
#
# print(friends[rand_int])

# This was my original solution, but you run into errors with indexing if you are not careful


# New Solution
print(random.choice(friends))