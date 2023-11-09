import colorgram
import turtle as turtle_module
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


print(rgb_colors)
turtle_module.colormode(255)
miles = turtle_module.Turtle()
miles.speed("fastest")
miles.penup()
miles.hideturtle()
dots_count = 100

miles.setheading(225)
miles.forward(300)
miles.setheading(0)

for dot_count in range(1, dots_count+1):
    miles.dot(20, random.choice(rgb_colors))
    miles.forward(50)

    if dot_count % 2 == 0:
        miles.setheading(90)
        miles.forward(50)
        miles.setheading(180)
        miles.forward(500)
        miles.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
