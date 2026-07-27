from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_to_left():
    tim.left(10)

def rotate_to_right():
    tim.right(10)

def clear_drawing():
    tim.reset()

# Make an Etch-A-Sketch App
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_to_left)
screen.onkey(key="d", fun=rotate_to_right)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()