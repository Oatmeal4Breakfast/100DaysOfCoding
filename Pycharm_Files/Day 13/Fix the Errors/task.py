
try:
    age = int(input("How old are you?"))
except ValueError as e:
    print(e)
    raise ValueError

if age > 18:
    print(f"You can drive at age {age}.")
