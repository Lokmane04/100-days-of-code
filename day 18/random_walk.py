import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("triangle")
timmy.color("red")
timmy.pensize(13)
timmy.speed(0)
timmy.hideturtle()
angles = [90, 180, 270, 360]

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97),
              (176, 192, 209)]
# another method using .color-mode(255)
color_list = [(r / 255, g / 255, b / 255) for r, g, b in color_list]


def random_walk(sides):
    for i in range(sides):
        timmy.color(random.choice(color_list))
        timmy.forward(40)
        timmy.left(random.choice(angles))


for sides in range(3, 55):
    random_walk(sides)

screen = Screen()
screen.exitonclick()
