from turtle import Turtle
import random

COLORS = ["HotPink4", "MidnightBlue", "OrangeRed3", "purple", "DarkOliveGreen", "Black"]
x_directions = random.randint(-310, 300)
y_directions = random.randint(-250, 250)

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.goto(x_directions, y_directions)

    def move(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())
