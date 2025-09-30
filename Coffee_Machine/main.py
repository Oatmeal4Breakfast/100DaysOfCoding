MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def prompt_user() -> str:
    """prompt the user for what they would like to drink"""
    valid_choices = ["espresso", "latte", "cappuccino", "report", "off"]
    user_choice: str = input(
        "What would you like? (espresso/latte/cappuccino): "
    ).lower()
    while user_choice not in valid_choices:
        user_choice = input(
            "Invalid choice. Please choose espresso, latte, cappuccino: "
        ).lower()
    return user_choice


def generate_report(resources: dict) -> list[str]:
    """generate a report of all resources"""
    list_of_resources = [
        f"{key}: {value}ml" for key, value in resources.items() if key != "coffee"
    ]
    list_of_resources.append(f"coffee: {resources['coffee']}g")
    list_of_resources.append(f"Money: ${resources.get('money', 0.0)}")
    return list_of_resources


def print_report(list_of_resources: list[str]) -> None:
    """print the report of all resources"""
    for resource in list_of_resources:
        print(resource)


def check_resources(drink_ingredients: dict, resources: dict) -> bool:
    """Returns True when order can be made, False if ingredients are insufficient."""
    for key, value in drink_ingredients.items():
        if value > resources.get(key, 0):
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def process_coins() -> float:
    """Calculate the total monetary value of coins inserted."""
    quarters: int = int(input("How many quarters?: "))
    dime: int = int(input("How many dimes?: "))
    nickel: int = int(input("How many nickels?: "))
    penny: int = int(input("How many pennies?: "))
    total: float = 0.25 * quarters + 0.10 * dime + 0.05 * nickel + 0.01 * penny
    return total


def check_transaction_successful(money_received: float, drink_cost: float) -> bool:
    """Check if the customer entered enough money to purchase the drink."""
    if money_received >= drink_cost:
        return True
    else:
        return False


def return_change(money_received: float, drink_cost: float) -> float:
    """returns the change to the user"""
    return round(money_received - drink_cost, 2)


def make_coffee(receipe: dict, resources: dict, beverage: str) -> None:
    """Make the coffee from the receipe and deduct the required ingredients from the resources."""
    for key, value in receipe.items():
        resources[key] -= value
    print(f"Here is your {beverage}. Enjoy!")


def main():
    # Make a copy of the resources to track available resources
    available_resources = resources.copy()

    while True:
        user_choice: str = prompt_user()

        # Turning off the machine if requested
        if user_choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        elif user_choice == "report":
            report = generate_report(available_resources)
            print_report(report)
        else:
            beverage_ingredients: dict = MENU[user_choice]["ingredients"]
            beverage_cost: float = MENU[user_choice]["cost"]
            if check_resources(beverage_ingredients, available_resources):
                print(f"The cost of a {user_choice} is ${beverage_cost}.")
                customer_payment: float = process_coins()
                if check_transaction_successful(customer_payment, beverage_cost):
                    change: float = return_change(customer_payment, beverage_cost)
                    if change > 0:
                        print(f"Here is ${change} in change.")
                    # Add the money to the resources
                    available_resources["money"] = (
                        available_resources.get("money", 0.0) + beverage_cost
                    )
                    make_coffee(
                        beverage_ingredients,
                        available_resources,
                        user_choice,
                    )


if __name__ == "__main__":
    main()
