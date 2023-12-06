from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.x_axis = 10
        self.y_axis = 10

    def goto_random_place(self):
        self.goto(x=self.xcor()+self.x_axis, y=self.ycor()+self.y_axis)

    def bounce(self):
        self.y_axis *= -1