from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(position)
            self.segments.append(snake)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            x_cord = self.segments[segment - 1].xcor()
            y_cord = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x=x_cord, y=y_cord)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
