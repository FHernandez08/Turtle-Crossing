import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

new_player = Player()
new_car_manager = CarManager()

screen.listen()
screen.onkey(new_player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    new_car_manager.create_car()
    new_car_manager.move_car()

    for car in new_car_manager.all_cars:
        if car.distance(new_player) < 20:
            game_is_on = False

    if new_player.is_at_finish_line():
        new_player.go_to_start()
        new_car_manager.level_up()

screen.exitonclick()