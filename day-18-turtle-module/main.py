from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()

timmy.shape("turtle")
timmy.color("green")

# Draw a square using Turtle
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

my_screen.exitonclick()