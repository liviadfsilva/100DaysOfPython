#TODO: draw a square.
from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("PapayaWhip")

hades = Turtle()
hades.shape("turtle")
hades.color("maroon")

for i in range(4):
    hades.forward(100)
    hades.left(90)

screen.exitonclick()