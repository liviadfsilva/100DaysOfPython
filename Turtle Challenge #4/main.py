#TODO: draw a random walk.
from turtle import Turtle, Screen
import random

screen = Screen()
screen.bgcolor("PapayaWhip")

hades = Turtle()
hades.shape("turtle")
hades.color("maroon")

for i in range(4):
    hades.forward(100)
    hades.left(90)

colors = ["aquamarine4", "DarkOrchid4", "DarkOrange2", "DeepPink2", "DarkSlateBlue", "DarkSeaGreen", "Coral",
          "gold1", "maroon", "RosyBrown2"]

#TODO: draw a random walk
directions = [0, 90, 180, 270]

hades.width(13)
hades.speed(5)

for _ in range(50):
    hades.pencolor(random.choice(colors))
    hades.forward(40)
    hades.setheading(random.choice(directions))

screen.exitonclick()