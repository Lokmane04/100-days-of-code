from turtle import Turtle, Screen

game_over =False
def move_up():
    paddle.goto(paddle.xcor(), paddle.ycor() + 20)


def move_down():
    paddle.goto(paddle.xcor(), paddle.ycor() - 20)


screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle = Turtle("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color("white")
paddle.penup()
paddle.goto(x=350, y=0)
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

while not game_over:
    screen.update()


screen.exitonclick()
