from turtle import Turtle

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color("maroon")
        self.shape("square")
        self.shapesize(1, 1)
        self.penup()
        self.goto(x=270, y=0)

    def move(self):
        new_x = self.xcor() - 10
        self.goto(new_x, 0)
