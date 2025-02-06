from turtle import Screen
from player import Player
from Day23.car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("PapayaWhip")
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with cars.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect successful crossing.
    if player.ycor() == 280:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.update_level()

screen.exitonclick()
