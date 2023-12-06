from turtle import Screen
from paddle import Paddle

game_over =False


screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

user_paddle= Paddle("user")
computer_paddle = Paddle("computer")
screen.listen()

screen.onkey(user_paddle.move_up, "Up")
screen.onkey(user_paddle.move_down, "Down")

while not game_over:
    screen.update()


screen.exitonclick()
