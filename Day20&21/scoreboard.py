from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 13, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Courier", 13, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=("Arial", 17, "normal"))