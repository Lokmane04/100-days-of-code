import random
from turtle import Turtle, Screen

tim = Turtle()
tim.penup()
tim.hideturtle()
tim.speed(0)

color_list = [(174, 38, 107), (221, 168, 67), (59, 178, 130), (95, 191, 138), (231, 39, 90),
 (238, 223, 73), (65, 162, 216), (9, 108, 182), (11, 144, 99), (234, 232, 15),
 (239, 115, 145), (240, 88, 42), (241, 145, 172), (33, 61, 153), (45, 185, 208),
 (145, 32, 89)]

# another method using .color-mode(255)
color_list = [(r / 255, g / 255, b / 255) for r, g, b in color_list]
tim.setheading(225)
tim.forward(320)
tim.setheading(0)
for dot_count in range(1, 101):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
