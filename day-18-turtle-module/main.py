from random import randint
from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()

timmy.shape("turtle")
timmy.speed("fastest")
my_screen.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


# Make a Spirograph
num_circles = int(360 / 5)

for _ in range(num_circles):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.left(5)

my_screen.exitonclick()