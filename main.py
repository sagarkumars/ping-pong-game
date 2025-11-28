from turtle import Screen

from paddle import Paddle

screen = Screen()
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("ping-pong")
right_puddle = Paddle((360, 0))
left_puddle = Paddle((-360, 0))
screen.listen()


screen.onkey(right_puddle.up, "Up")
screen.onkey(right_puddle.down, "Down")
screen.onkey(left_puddle.up, "w")
screen.onkey(left_puddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()