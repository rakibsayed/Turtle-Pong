from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        """Creates a ScoreBoard,
        To Keep Track of the Players score"""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 6
        self.r_score = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 300)
        self.write(self.l_score, align="center", font=("Agency FB", 80, "normal"))
        self.goto(100, 300)
        self.write(self.r_score, align="center", font=("Agency FB", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
