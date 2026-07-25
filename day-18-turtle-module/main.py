from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()

timmy.shape("turtle")
timmy.color("green")

# Draw a Dashed line
for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

my_screen.exitonclick()