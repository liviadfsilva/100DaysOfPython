from turtle import Turtle

class Crosser(Turtle):
    def __init__(self):
        super().__init__()
        self.color("aquamarine4")
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(x=0, y=-270)

    def go_up(self):
        new_y = self.ycor() + 60
        self.goto(self.xcor(), new_y)