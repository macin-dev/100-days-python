import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.random_position()

    def move(self, car_speed):
        self.backward(car_speed)

    def random_position(self):
        self.goto(300, random.randint(-250, 250))

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            self.all_cars.append(Car())

    def move_cars(self):
        for car in self.all_cars:
            car.move(self.car_speed)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT

