from turtle import Turtle


class Border:
    def __init__(self):
        """Creates a Border at the center of the screen"""
        self.border = []
        self.create_border()

    def create_border(self):
        y = 410
        for border_seg in range(11):
            border_seg = Turtle("square")
            border_seg.shapesize(stretch_wid=1, stretch_len=0.5)
            border_seg.color("white")
            border_seg.penup()
            border_seg.sety(y)
            y -= 80
            self.border.append(border_seg)
