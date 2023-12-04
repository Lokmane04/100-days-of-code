from turtle import Turtle

FONT = ("Courier", 16, "normal")
SCORE = 0


class ScoreBoard(Turtle):

    def __init__(self):
        self.score = SCORE
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_text()

    def update_text(self):
        self.goto(x=0, y=270)
        self.write(f" Score : {self.score}", move=True, align="center", font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", move=True, align="center", font=FONT)

    def increment(self):
        self.score += 1
        self.clear()
        self.update_text()
