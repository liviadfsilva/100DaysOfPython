#TODO: draw a dashed line.
from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("PapayaWhip")

hades = Turtle()
hades.shape("turtle")
hades.color("maroon")

for i in range(10):
    hades.forward(10)
    hades.up()
    hades.forward(10)
    hades.down()

screen.exitonclick()