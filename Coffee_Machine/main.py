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
    list_of_resources.append(f"Money: ${resources.get('money', 0)}")
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


def main():
    print("mmmm Coffee")


if __name__ == "__main__":
    main()
