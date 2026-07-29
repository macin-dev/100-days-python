import time
from turtle import Screen
from player import Player
from car_manager import CarManager, Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Turtle Crossing")

# Instances of classes
player = Player()
car_manager = CarManager()

# Listen for keys
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Add and move cars
    car_manager.add_car()
    car_manager.move_cars()

    # Detect collision with wall
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # Reset the turtle's position once it crossed the finish line
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.level_up()



screen.exitonclick()