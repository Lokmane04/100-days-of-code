import random
from turtle import Turtle, Screen

timmy = Turtle()

color_list = [(255, 105, 97), (255, 179, 71), (255, 209, 102), (6, 123, 176), (10, 189, 227), (115, 223, 255), (16, 172, 132), (51, 214, 159), (126, 214, 223)]

# another method using .color-mode(255)
color_list = [(r / 255, g / 255, b / 255) for r, g, b in color_list]

timmy.pensize(3)
timmy.speed("fastest")
timmy.hideturtle()

for i in range(int(360/5)):
    timmy.color(random.choice(color_list))
    timmy.circle(100)
    timmy.setheading(timmy.heading()+5)


screen = Screen()
screen.exitonclick()
