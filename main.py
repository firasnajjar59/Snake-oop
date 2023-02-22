from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

def game_start():
    screen = Screen()
    def quit():
        screen.bye()
    def restart():
        return game_start()
    screen.clear()
    screen.setup(width=600,height=600)
    screen.title("Snake game")
    screen.bgcolor("black") 
    screen.tracer(0)
    snake= Snake()
    food=Food()
    score=Score()
    screen.update()
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")

    game_is_on=True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if round(food.distance(snake.head.pos()),0)==0:
            food.random_food_pos()
            score.increase_score()
            snake.extend()
        if snake.head.xcor()>250 or snake.head.xcor()<-250 or snake.head.ycor()>250 or snake.head.ycor()<-250:
            game_is_on=False
            score.game_over()
            screen.onkeypress(quit,"n")
            screen.onkeypress(restart,"y")
        for segment in snake.body[1:]:
            if snake.head.distance(segment)<9:
                game_is_on=False
                score.game_over()
                screen.onkeypress(quit,"n")
                screen.onkeypress(quit,"n")
    screen.exitonclick()
game_start()
