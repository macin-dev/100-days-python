from random import choice
from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()

timmy.shape("turtle")

# Draw a triangle, square, pentagon, hexagon,
# heptagon, octagon, nonagon, and decagon
colors = ["red", "blue", "green", "yellow", "orange", "pink", "purple"]

# Draw shapes from 3 sides (triangle) up to 10 sides (decagon)
for num_sides in range(3,11):
    angle = 360 / num_sides
    timmy.color(choice(colors))
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

my_screen.exitonclick()