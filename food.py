from turtle import Turtle
import random
from scoreboard import Scoreboard

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed("fastest")
        self.color("blue")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-290, 290)
        random_y = random.randint(-290, 290)
        self.goto(random_x, random_y)

