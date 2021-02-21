from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

L_PADDLE_POS = (-350, 0)
R_PADDLE_POS = (350, 0)

# Initialize the game screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

# Create objects: paddles, ball, scoreboard
l_paddle = Paddle(L_PADDLE_POS)
r_paddle = Paddle(R_PADDLE_POS)
ball = Ball()
scoreboard = Scoreboard()

# Event Listeners
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


# Start Game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if the right paddle misses
    if ball.xcor() >= 370:
        ball.refresh()
        scoreboard.l_point()

    # Detect if the left paddle misses
    if ball.xcor() <= -370:
        ball.refresh()
        scoreboard.r_point()

screen.exitonclick()
