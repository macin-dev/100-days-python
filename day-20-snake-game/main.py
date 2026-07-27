from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Create a snake body
last_position = 0.0

for i in range(3):
    sk = Turtle()
    sk.shape("square")
    sk.color("white")
    sk.penup()
    sk.forward(last_position)
    last_position += -20

screen.exitonclick()