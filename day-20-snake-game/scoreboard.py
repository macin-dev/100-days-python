from turtle import Turtle
ALIGNMENT = "center"
FONT  = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.sety(270)
        self.display_scoreboard()
        self.hideturtle()

    def display_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_scoreboard()