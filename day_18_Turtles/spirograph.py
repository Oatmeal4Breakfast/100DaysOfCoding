import random
import turtle as t
from turtle import Turtle, Screen


def random_color() -> tuple[int, int, int]:
    r: int = random.randint(0, 255)
    g: int = random.randint(0, 255)
    b: int = random.randint(0, 255)
    return (r, g, b)


def main() -> None:
    t.colormode(255)

    tim: Turtle = Turtle()
    tim.shape("arrow")
    tim.speed("fastest")

    for angle in range(0, 360, 3):
        tim.color(random_color())
        tim.setheading(angle)
        tim.circle(100)

    screen: Screen = Screen()
    screen.exitonclick()


main()
