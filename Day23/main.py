from turtle import Screen
from crosser import Crosser
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("PapayaWhip")
screen.tracer(0)

hades = Crosser()

screen.listen()
screen.onkey(hades.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()