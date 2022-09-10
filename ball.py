from turtle import Turtle

STARTING_POS = (0, 0)


class Ball(Turtle):
    def __init__(self):
        """Creates a Ball"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.hideturtle()
        self.color("white")
        self.x_move = 0
        self.y_move = 0
        self.move_speed = 0.05

    def start_moving(self):
        """Ball will move"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Ball will bounce off the top and bottom of the screen"""
        self.y_move *= -1

    def bounce_x(self):
        self.move_speed *= 0.9
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
