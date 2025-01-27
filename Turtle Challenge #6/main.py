#TODO: draw a spirograph.
import turtle as t
from turtle import Screen
import random

screen = Screen()
screen.bgcolor("PapayaWhip")

hades = t.Turtle()
hades.shape("turtle")
hades.color("maroon")

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

hades.speed(11)

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        hades.pencolor(random_color())
        hades.circle(113)
        hades.setheading(hades.heading() + size_of_gap)

draw_spirograph(5)

screen.exitonclick()