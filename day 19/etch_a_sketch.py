from turtle import Screen, Turtle

tim = Turtle()


def move_forward():
    tim.setheading(0)
    tim.forward(100)


def move_backward():
    tim.setheading(180)
    tim.forward(100)


def move_counter_clockwise():
    tim.setheading(90)
    tim.forward(100)


def move_clockwise():
    tim.setheading(270)
    tim.forward(100)


screen = Screen()

screen.listen()

screen.onkey(key='w',fun=move_forward)
screen.onkey(key='s',fun=move_backward)
screen.onkey(key='a',fun=move_counter_clockwise)
screen.onkey(key='d', fun=move_clockwise)

screen.exitonclick()
