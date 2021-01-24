from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align='center', font=FONT)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=(FONT))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
