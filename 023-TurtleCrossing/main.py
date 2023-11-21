import time
from playsound import playsound
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.level_up()
        scoreboard.update_scoreboard()
        car_manager.speed_up()
        playsound("../023-TurtleCrossing/assets/level_up.mp3")
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False


scoreboard.game_over()
playsound("../023-TurtleCrossing/assets/game_over.wav")
screen.exitonclick()
