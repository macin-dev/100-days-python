from turtle import Turtle, Screen
from random import choice

rgb_colors = [(208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165)]

tim = Turtle()
screen = Screen()

# Default configurations
screen.colormode(255)
screen.title("Hirst Spot Painting")
tim.hideturtle()
tim.speed("fastest")
tim.penup()
tim.goto(-250, -250)

num_rows = 10
num_dots = 10

for _ in range(num_rows):
    for _ in range(num_dots):
        tim.dot(20, choice(rgb_colors))
        tim.forward(50)

    tim.goto(-250, tim.ycor() + 50)

screen.exitonclick()