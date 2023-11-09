import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)

directions = [0, 45, 90, 135, 180, 225, 270, 315, 360]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()