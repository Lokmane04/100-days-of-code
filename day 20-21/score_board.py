from turtle import Turtle

FONT = ("Courier", 16, "normal")
SCORE = 0


class ScoreBoard(Turtle):

    def __init__(self):
        self.score = SCORE
        self.high_score = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_text()

    def update_text(self):
        self.clear()
        self.goto(x=0, y=270)
        self.write(f" Score : {self.score}  High score : {self.high_score}", move=True, align="center", font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_text()

    #    def game_over(self):
    #       self.goto(x=0, y=0)
    #      self.write(f"GAME OVER", move=True, align="center", font=FONT)

    def increment(self):
        self.score += 1
        self.clear()
        self.update_text()
