import turtle
from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.score}", align = "center" ,font=("Verdana",20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Verdana", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align="center", font=("Verdana", 35, "normal"))