from turtle import Turtle, Screen


def draw_square(turtle: Turtle) -> None:
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_dashed_line(turtle: Turtle) -> None:
    for _ in range(15):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()


def draw_shape(turtle: Turtle, sides: int) -> None:
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(360 / sides)


def main():
    tim = Turtle()
    tom = Turtle()
    # tim.shape("circle")
    # tim.color("chartreuse4")
    # draw_square(tim)

    shapes: list[int] = [3, 4, 5, 6, 7, 8, 9, 10]
    colors: list[str] = [
        "coral",
        "coral1",
        "coral2",
        "coral3",
        "coral4",
        "cornflower blue",
        "cornsilk1",
        "cornsilk2",
        "cornsilk3",
        "cornsilk4",
    ]

    for shape, color in zip(shapes, colors):
        tim.color(color)
        draw_shape(tim, shape)

    # draw_dashed_line(tom)
    screen = Screen()
    screen.exitonclick()


main()
