import random


# rand_integer = random.randint(1,10)
# print(rand_integer)
#
# random_number_0_to_1 = random.random() * 100
# print(random_number_0_to_1)
#
# rand_floating_point = random.uniform(1, 10)

rand_int: int = random.randint(0,1)
if rand_int == 0:
    print("Heads")
else:
    print("Tails")