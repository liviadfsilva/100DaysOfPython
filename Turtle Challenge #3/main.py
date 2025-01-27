#TODO: draw multiple shapes.
from turtle import Turtle, Screen
import random

screen = Screen()
screen.bgcolor("PapayaWhip")

hades = Turtle()
hades.shape("turtle")
hades.color("maroon")

hades.up()
hades.left(90)
hades.forward(200)
hades.left(90)
hades.forward(50)
hades.right(180)
hades.down()

colors = ["aquamarine4", "DarkOrchid4", "DarkOrange2", "DeepPink2", "DarkSlateBlue", "DarkSeaGreen", "Coral",
          "gold1", "maroon", "RosyBrown2"]

def draw_shape(num_sides):
    angle = 360/num_sides

    for _ in range(num_sides):
        hades.forward(100)
        hades.right(angle)

for shape_n_sides in range(3, 11):
    hades.pencolor(random.choice(colors))
    draw_shape(shape_n_sides)

screen.exitonclick()