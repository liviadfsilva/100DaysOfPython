import turtle as t
import random

hades = t.Turtle()

t.colormode(255)

colors = [(236, 35, 108), (221, 231, 237), (145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95),
              (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78),
              (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35)]

hades.speed("fastest")

hades.penup()
hades.hideturtle()

hades.setheading(225)
hades.forward(300)
hades.setheading(0)

number_of_dots = 100

for dots in range(1, number_of_dots + 1):
    hades.dot(20, random.choice(colors))
    hades.forward(50)

    if dots % 10 == 0:
        hades.setheading(90)
        hades.forward(50)
        hades.setheading(180)
        hades.forward(500)
        hades.setheading(0)

screen = t.Screen()
screen.exitonclick()