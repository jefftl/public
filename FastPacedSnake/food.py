from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        food_position_x = random.randint(-280,280)
        food_position_y = random.randint(-280,280)
        self.goto(food_position_x, food_position_y)

    def refresh(self):
        food_position_x = random.randint(-280, 280)
        food_position_y = random.randint(-280, 280)
        self.goto(food_position_x, food_position_y)