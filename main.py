import time
from turtle import Screen

from boll import Boll
from paddle import Paddle
import random

from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("ping-pong")
right_puddle = Paddle((360, 0))
left_puddle = Paddle((-360, 0))
boll = Boll()
scoreboard = ScoreBoard()
screen.listen()


screen.onkey(right_puddle.up, "Up")
screen.onkey(right_puddle.down, "Down")
screen.onkey(left_puddle.up, "w")
screen.onkey(left_puddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(boll.move_speed)
    boll.move()
    screen.update()

    # bounce walls
    if boll.ycor() > 280 or boll.ycor() < -280:
        boll.bounce_y()

    # bounce paddle
    if (boll.distance(right_puddle) < 50 and boll.xcor() > 320
            or boll.distance(left_puddle) < 50 and boll.xcor() < -320):
        boll.bounce_x()

    # detect miss
    if boll.xcor() > 380:
        boll.reset_position()
        scoreboard.right_scored()

    if boll.xcor() < -380:
        boll.reset_position()
        scoreboard.left_scored()

screen.exitonclick()