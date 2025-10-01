from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    # Initialize all of the objects
    menu: Menu = Menu()
    coffee_maker: CoffeeMaker = CoffeeMaker()
    money_machine: MoneyMachine = MoneyMachine()

    # Display the menu items and take an order
    while True:
        user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
        if user_choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        elif user_choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(user_choice)
            if drink and coffee_maker.is_resource_sufficient(drink):
                print(f"Please pay {drink.cost}")
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)


main()
