from turtle import Turtle

WIDTH = 900
HEIGHT = 600
PADDLES_X = {"RIGHT": 400, "LEFT": -400}


class Paddle(Turtle):
    """Creates a Paadle for You
    Takes right or left as an argument"""
    def __init__(self, paddle: str):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.setx(PADDLES_X[paddle.upper()])

    def move_up(self):
        if self.ycor() < 380:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -370:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)
