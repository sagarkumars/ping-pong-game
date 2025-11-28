from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("White")
        self.goto(position)

    def up(self):
        new_pus = self.ycor() + 20
        self.goto(self.xcor(), new_pus)

    def down(self):
        new_pus = self.ycor() - 20
        self.goto(self.xcor(), new_pus)
