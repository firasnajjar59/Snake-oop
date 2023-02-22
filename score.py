from turtle import Turtle
from random import choice

class Score(Turtle):
    def __init__(self, shape: str = "square", undobuffersize: int = 1000, visible: bool = True):
        super().__init__(shape, undobuffersize, visible)
        self.score=0
        self.print_limits()
        self.print_score()
    def print_score(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0,260)
        self.write(f"Home:{self.score}",align="center",font=("Arial",15, "normal"))
    def print_limits(self):
        self.setpos(-250,-250)
        self.pendown()
        self.pensize("3")
        self.pencolor("red")
        self.goto(250,-250)
        self.goto(250,250)
        self.goto(-250,250)
        self.goto(-250,-250)
        self.penup()
    def game_over(self):
        self.setpos(0,0)
        self.write("GAME OVER",align="center",font=("Arial",20, "bold"))
        self.setpos(0,-30)
        self.write("To restart the game press the key 'y',",align="center",font=("Arial",15, "normal"))
        self.setpos(0,-60)
        self.write("to exit press the key 'n'",align="center",font=("Arial",15, "normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.print_limits()
        self.print_score()