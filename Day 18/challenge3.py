from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed(50)
colors = ["crimson", "orange red", "olive drab", "dodger blue"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for n in range(3, 111):
    tim.color(random.choice(colors))
    draw_shape(n)

screen = Screen()
screen.exitonclick()
