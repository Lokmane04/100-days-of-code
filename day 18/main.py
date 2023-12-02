from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("triangle")
timmy.color("red")


def numberToShape(sides):
    for i in range(sides):
        timmy.forward(100)
        timmy.left(360 / sides)

def numberToShapeSymmetric(sides):
    for i in range(sides):
        timmy.forward(100)
        timmy.right(360 / sides)


for sides in range(3, 10):
    numberToShape(sides)
timmy.color("green")
for sides in range(3, 10):
    numberToShapeSymmetric(sides)

screen = Screen()
screen.exitonclick()
