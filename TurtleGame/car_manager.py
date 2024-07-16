from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.penup()
        self.goto(500, 0)


    def add_car(self):
        new_car = Turtle("square")
        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        position_y = random.randint(-250, 250)
        new_car.goto(500, position_y)
        new_car.speed("slowest")
        self.cars.append(new_car)


    def move_car(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
