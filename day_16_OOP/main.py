from turtle import Turtle, Screen
from prettytable import PrettyTable


def main():
    # timmy.shape("turtle")
    #
    # timmy.color("DarkOrchid")
    #
    # timmy.forward(100)
    #
    # my_screen: Screen = Screen()
    # my_screen.exitonclick()
    table: PrettyTable = PrettyTable()
    table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
    table.add_column("Type", ["Electric", "Water", "Fire"])

    table.align = "l"
    print(table)


main()

