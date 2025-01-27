#TODO: draw a random walk with random RGB colors.
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

directions = [0, 90, 180, 270]
hades.width(13)
hades.speed(5)

for _ in range(50):
    hades.pencolor(random_color())
    hades.forward(40)
    hades.setheading(random.choice(directions))