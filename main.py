from ball import Ball
from border import Border
from paddle import Paddle
from score import ScoreBoard
from turtle import Screen, Turtle
import time
from _tkinter import TclError

WIDTH = 900
HEIGHT = 900

# GAME WINDOW
screen = Screen()
screen.setup(WIDTH, HEIGHT, startx=530, starty=50)
screen.bgcolor("black")
screen.title('Pong')
screen.tracer(0)

# GAME TITLE
title = Turtle()
title.penup()
title.color("white")
title.hideturtle()
title.write("PONG", font=("Agency FB", 80, "bold"), align="center")
title.sety(-50)
title.write("press space to start the game", font=("Courier", 20, "normal"), align="center")

# GAME OBJECTS
right_paddle = Paddle("right")
left_paddle = Paddle("left")
ball = Ball()
score = ScoreBoard()

#  EVENT LISTENER
screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkey(lambda: [screen.clearscreen(), screen.bye()], "Escape")  # EXIT THE GAME

screen.update()
# PARTITION
border = Border()
border.create_border()


# MAIN GAME FUNCTION
def start_game():
    title.clear()
    ball.showturtle()
    # INITAIALLY THE BALL WAS HIDDEN 'CAUSE I DON'T WANT IT TO BE SHOWN WHEN THE TITLE PAGE APPEARS
    game_is_running = True
    while game_is_running:
        try:
            time.sleep(ball.move_speed)
            screen.update()
            ball.start_moving()

            # DETECTING COLLISON BETWEEN THE PADDLES AND THE BALL
            if ball.distance(right_paddle) < 60 and ball.xcor() > 380 or ball.distance(
                    left_paddle) < 60 and ball.xcor() < -380:
                ball.bounce_x()

            # DETECTING COLLISON WITH WALL
            if ball.ycor() > 420 or ball.ycor() < -420:
                ball.bounce_y()

            # IF THE BALL PASS BY THE RIGHT PADDLE AND OFF THE SCREEN
            if ball.xcor() > 450:
                score.l_point()
                score.update_scoreboard()
                ball.reset()

            # IF THE BALL PASS BY THE LEFT PADDLE AND OFF THE SCREEN
            if ball.xcor() < -450:
                score.r_point()
                score.update_scoreboard()
                ball.reset()

        # Incase If someone tries to close the app by clicking on "X" button
        except TclError:
            game_is_running = False


screen.onkeypress(start_game, "space")
screen.mainloop()
