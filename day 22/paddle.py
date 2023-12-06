from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, player_type):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.initialize_paddle_position(player_type)

    def initialize_paddle_position(self, player_type):
        """this function takes a string as a parameter , "first" or "computer" """
        if player_type == "user":
            self.goto(x=350, y=0)
        elif player_type == "computer":
            self.goto(x=-350, y=0)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
