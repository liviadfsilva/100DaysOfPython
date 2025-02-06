from turtle import Turtle

STARTING_POSITION = (0, -280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("aquamarine4")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def move(self):
        self.forward(20)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
