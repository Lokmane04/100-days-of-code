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

user_paddle= Paddle("user")
computer_paddle = Paddle("computer")
screen.listen()

screen.onkey(user_paddle.move_up, "Up")
screen.onkey(user_paddle.move_down, "Down")

while not game_over:
    time.sleep(0.05)
    screen.update()
    ball.goto_random_place()

screen.exitonclick()
