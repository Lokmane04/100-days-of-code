from turtle import Turtle


FONT = ("Courier", 16, "normal")
SCORE = 0


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = None
        self.score = SCORE
        self.get_high_score()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_text()

    def update_text(self):
        self.clear()
        self.goto(x=0, y=270)
        self.write(f" Score : {self.score}  High score : {self.high_score}", move=True, align="center", font=FONT)

    def set_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def get_high_score(self):
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.update_text()

    #    def game_over(self):
    #       self.goto(x=0, y=0)
    #      self.write(f"GAME OVER", move=True, align="center", font=FONT)

    def increment(self):
        self.score += 1
        self.clear()
        self.update_text()
