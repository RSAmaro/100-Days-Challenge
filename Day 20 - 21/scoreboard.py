from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\nScore: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
