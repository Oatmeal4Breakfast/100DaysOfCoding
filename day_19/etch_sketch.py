from turtle import Turtle, Screen


tim: Turtle = Turtle()

tim.speed("fast")


def move_forwards() -> None:
    tim.forward(10)


def move_backwards() -> None:
    tim.backward(10)


def counter_clockwise() -> None:
    tim.left(10)


def clockwise() -> None:
    tim.right(10)


def clear_screen() -> None:
    tim.home()
    tim.clear()


def main() -> None:
    screen: Screen = Screen()

    screen.listen()
    screen.onkey(key="w", fun=move_forwards)
    screen.onkey(key="s", fun=move_backwards)
    screen.onkey(key="a", fun=counter_clockwise)
    screen.onkey(key="d", fun=clockwise)
    screen.onkey(key="c", fun=clear_screen)
    screen.exitonclick()


if __name__ == "__main__":
    main()
