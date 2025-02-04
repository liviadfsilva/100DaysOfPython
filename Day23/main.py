from turtle import Screen
from crosser import Crosser
from car import Car
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("PapayaWhip")
screen.tracer(0)

hades = Crosser()
car = Car()

screen.listen()
screen.onkey(hades.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car.move()
    screen.update()

screen.exitonclick()