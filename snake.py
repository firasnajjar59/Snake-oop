from turtle import Turtle
START_POSIONS=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.body=[]
        self.init_snake()
        self.head=self.body[0]
    def init_snake(self):
        for pos in START_POSIONS:
            self.add_body_part(pos)
    def add_body_part(self,posion):
        new_segment=Turtle(shape="square")
        new_segment.penup()
        new_segment.goto(posion)
        new_segment.color("white")
        self.body.append(new_segment)

    def extend(self):
        self.add_body_part(self.body[-1].pos())
    def move(self):
        for num in range(len(self.body)-1,0,-1):
            new_x=self.body[num-1].xcor()
            new_y=self.body[num-1].ycor()
            self.body[num].goto(new_x,new_y)
        self.head.forward(20)
    def up(self):
        if self.head.heading()==0 or self.head.heading()==180:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()==0 or self.head.heading()==180:
            self.head.setheading(270)
    def left(self):
        if self.head.heading()==90 or self.head.heading()==270:
            self.head.setheading(180)
    def right(self):
        if self.head.heading()==90 or self.head.heading()==270:
            self.head.setheading(0)
        