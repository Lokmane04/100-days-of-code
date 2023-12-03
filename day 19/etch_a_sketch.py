from turtle import Screen, Turtle

tim = Turtle()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.forward(10)


def turn_left():
    tim.setheading(tim.heading()+10)
    tim.forward(10)


def turn_right():
    tim.setheading(tim.heading()-10)
    tim.forward(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen = Screen()
 
screen.listen()

screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()
