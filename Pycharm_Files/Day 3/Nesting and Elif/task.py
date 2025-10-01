print("Welcome to the rollercoaster!")
height: int = int(input("What is your height in cm? "))
min_height: int = 120

if height >= 120:
    print("You can ride the rollercoaster")
    age: int = int(input("How old are you? "))
    if age <= 12:
        print("Your ticket is $5")
    elif age >= 18:
        print("Your ticket is $7")
    else:
        print("Your ticket is $12")

else:
    print("Sorry you have to grow taller before you can ride.")
