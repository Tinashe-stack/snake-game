from turtle import Turtle
import random

GRID_SIZE = 20
RANGE_MIN = -280
RANGE_MAX = 280


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randrange(RANGE_MIN, RANGE_MAX + GRID_SIZE, GRID_SIZE)
        random_y = random.randrange(RANGE_MIN, RANGE_MAX + GRID_SIZE, GRID_SIZE)
        self.goto(random_x, random_y)
