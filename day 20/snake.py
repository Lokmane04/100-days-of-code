from turtle import Turtle
class Snake:
    def __init__(self):
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        for position in self.starting_position:
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

        self.segments[0].forward(10)