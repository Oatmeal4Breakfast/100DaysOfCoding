print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill: int = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("children tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Teenage tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo: str = input("Do you want o have a photo taken? Type y for Yes and n for No.")
    if wants_photo == "y":
        # add $3 to bill
        bill += 3
        print(f"Your total bill is ${bill}")
    print(f"Your total bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
