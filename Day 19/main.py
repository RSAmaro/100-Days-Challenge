from turtle import Turtle, Screen, TK
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="Which Turtle will win? Enter a color:")
colors = ["red", "orange", "black", "green", "blue", "purple", "yellow", "aqua"]
pos_y = [-70, -40, -10, 20, 50, 80, 110, 140, 170]
turtles = []

print(user_bet)

for turtle_index in range(0, 8):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=pos_y[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                TK.messagebox.showinfo(title="The Turtle says:",
                                       message=f"You Won! The {win_color} turtle is the winner!")
            else:
                TK.messagebox.showinfo(title="The Turtle says:",
                                       message=f"You Lost! The {win_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)

        turtle.forward(rand_distance)

screen.exitonclick()
