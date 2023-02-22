from turtle import Turtle
from random import choice
START=-240
FINISH=240
FOOD_POS=[START]
while not FOOD_POS[len(FOOD_POS)-1]==FINISH:
    FOOD_POS.append(FOOD_POS[len(FOOD_POS)-1]+20)
class Food(Turtle):
    def __init__(self, shape: str = "square", undobuffersize: int = 1000, visible: bool = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.random_food_pos()
    def random_food_pos(self):
        random_x=choice(FOOD_POS)
        random_y=choice(FOOD_POS)
        self.goto(random_x,random_y)