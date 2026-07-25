from random import choice
from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()

timmy.shape("turtle")
timmy.pensize(10)
timmy.speed("fastest")

# Draw a Random Walk
colors = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]
directions = [90, 180, 270, 360]

for _ in range(100):
    timmy.right(choice(directions))
    timmy.color(choice(colors))
    timmy.forward(20)

my_screen.exitonclick()