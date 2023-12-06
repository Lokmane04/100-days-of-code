from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

game_over = False

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

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

while not game_over:
    time.sleep(0.05)
    screen.update()
    ball.goto_random_place()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
screen.exitonclick()
