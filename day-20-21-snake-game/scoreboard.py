from turtle import Turtle
ALIGNMENT = "center"
FONT  = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.sety(270)
        self.display_scoreboard()
        self.hideturtle()

    def display_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.display_scoreboard()

    def reset(self):
        self.high_score = max(self.score, self.high_score)
        self.score = 0
        self.display_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)