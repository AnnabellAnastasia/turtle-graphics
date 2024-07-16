import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Create a turtle player that starts
# at the bottom of the screen and listen for the "Up" keypress
# to move the turtle north.
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()

screen.listen()
screen.onkey(turtle.go_up, 'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
