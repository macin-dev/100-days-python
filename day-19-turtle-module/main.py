from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["pink", "red", "green", "blue", "purple", "orange"]

# Crete 6 instances of turtle
y_axis = -70
x_axis = -230

for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    tim.goto(x=x_axis, y=y_axis)
    y_axis += 30

screen.exitonclick()