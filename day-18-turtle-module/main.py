from random import choice, randint
from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()

timmy.shape("turtle")
timmy.pensize(10)
timmy.speed("fastest")
my_screen.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


# Draw a Random Walk
directions = [0, 90, 180, 270]

for _ in range(100):
    timmy.right(choice(directions))
    timmy.color(random_color())
    timmy.forward(20)

my_screen.exitonclick()