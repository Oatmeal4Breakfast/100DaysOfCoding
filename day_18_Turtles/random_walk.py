import random
from turtle import Turtle, Screen
import turtle


def random_color() -> tuple[int, int, int]:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def main():
    directions: list[int] = [90, 180, 270, 0]
    # colors: list[str] = [
    #     "coral",
    #     "coral1",
    #     "coral1",
    #     "coral2",
    #     "coral3",
    #     "coral4",
    #     "cornflower blue",
    #     "cornsilk1",
    #     "cornsilk2",
    #     "cornsilk3",
    #     "cornsilk4",
    # ]

    # setting the color mode to 255
    turtle.colormode(255)

    # configuring tim the turtle
    tim: Turtle = Turtle()
    tim.shape("classic")
    tim.speed("fastest")
    tim.pensize(15)

    for _ in range(200):
        tim.color(random_color())
        tim.setheading(random.choice(directions))
        tim.forward(30)

    screen: Screen = Screen()
    screen.exitonclick()


main()
