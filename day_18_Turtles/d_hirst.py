import colorgram
import turtle as t
import random


def draw_dot(turtle: t.Turtle, color: tuple[int, int, int], size: int) -> None:
    turtle.dot(size, color)
    turtle.penup()
    turtle.forward(size * 2)
    turtle.pendown()


def main():
    # set the color mode
    t.colormode(255)

    colors = colorgram.extract("d_hirst_spot_painting.png", 20)
    y_pos: int = 0
    # initialize the turtle
    tim = t.Turtle()
    tim.speed("fastest")
    tim.setpos(0, y_pos)

    for _ in range(10):
        for _ in range(10):
            draw_dot(tim, random.choice(colors).rgb, 25)
            tim.penup()

        y_pos += 50
        tim.setpos(0, y_pos)

    # initialize the screen
    screen = t.Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
