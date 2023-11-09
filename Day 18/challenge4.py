import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
# directions = [0, 45, 90, 135, 180, 225, 270, 315, 360]
directions = [0, 90, 180, 270, 360]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.pensize(10)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
