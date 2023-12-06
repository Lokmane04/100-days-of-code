from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard
game_over = False

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)
# initializing the scoreboard
score = ScoreBoard()
# creating the ballKK
ball = Ball()
# creating the two paddles

right_paddle = Paddle("user")
left_paddle = Paddle("computer")
screen.listen()

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

# initializing the ball speed
ball.increase_speed= 0.1
while not game_over:
    time.sleep(ball.increase_speed)
    screen.update()
    ball.goto_random_place()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 390:
        ball.home()
        ball.bounce_x()
        score.r_point()
    if ball.xcor() < -390:
        ball.home()
        ball.bounce_x()
        score.l_point()
    if score.left_score == 10:
        score.l_won()
        game_over = True

    elif score.right_score == 10:
        score.r_won()
        game_over = True

screen.exitonclick()
