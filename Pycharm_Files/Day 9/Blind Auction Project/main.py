# TODO-1: Ask the user for input
print("Welcome to the Silent Auction")
bids: dict = {}
some_one_else: bool = True

while some_one_else:
    bid: dict = {}
    name: str = input("What is your name?: ")
    price: int = int(input("Enter your bid: $"))
    bids[name] = price

    go_again: str = input("Would you like to go again? (yes/no): ").lower()

    print("\n" * 20)

    if go_again == "no":
        some_one_else = False

name = ""
highest_bid: int = 0
for entry in bids:
    if bids[entry] > highest_bid:
        highest_bid = bids[entry]
        name = entry

print(f"{name} had the highest bid of ${highest_bid}")




# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


