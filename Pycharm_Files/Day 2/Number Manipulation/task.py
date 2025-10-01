
weight: int = 84
height: float = 1.65
bmi:float = weight/(height**2)

print(bmi)

# converting to an int will floor the number
print(int(bmi))

# rounding the number in the trad. math sense
print(round(bmi))
print(round(bmi, 2)) # round to the 2nd decimal place
print(round(bmi, 5)) # round to the 5th decimal place

# assignment operators
score: int = 0
score += 1
score -= 1
score *= 1
score /= 1

# f string mixing strings with diff. data types
age: int = 28

print(f"I am {age} years old")


