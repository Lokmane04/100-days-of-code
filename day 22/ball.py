from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()

    def goto_random_place(self):
        self.goto(x=self.xcor()+5, y=self.ycor()+5)
