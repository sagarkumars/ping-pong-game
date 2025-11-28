from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.L_score = 0
        self.R_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.L_score} :  {self.R_score}", align="center", font=("Ärial", 32, "normal"))

    def left_scored(self):
        self.L_score += 1
        self.update_score()

    def right_scored(self):
        self.R_score += 1
        self.update_score()
