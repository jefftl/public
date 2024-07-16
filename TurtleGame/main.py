import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("white")
screen.title("Turtle crossing")
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_forward, "w")
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if ((scoreboard.score + 1) * 0.1) > random.random():
        car_manager.add_car()

    car_manager.move_car()
    # Detect player has reached the other side.
    if player.ycor() > 260:
        scoreboard.increase_score()
        player.return_to_start()

    # Detect player if is squished
    if player.ycor() > -280:
        for car in car_manager.cars:
            if car.distance(player) < 20:
                scoreboard.game_over()
                game_is_on = False

screen.exitonclick()
