from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("triangle")
timmy.color("blue")


def numberToShape(sides):
    for i in range(sides):
        timmy.forward(100)
        timmy.left(360 / sides)


for sides in range(3, 10):
    numberToShape(sides)

screen = Screen()
screen.exitonclick()
