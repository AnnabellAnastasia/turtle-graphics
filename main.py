import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
from scoreboard import Scoreboard

# Create a turtle player that starts
# at the bottom of the screen and listen for the "Up" keypress
# to move the turtle north.
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

def car_position_generator():
    y_cor = random.randint(-250, 250)
    return 280, y_cor


car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #Detect collistion with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        scoreboard.level_point()
        player.go_to_start()
        car_manager.level_up()

screen.exitonclick()
