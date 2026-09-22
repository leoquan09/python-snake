from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, "center", ("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, -20)
        self.write(f"GAME OVER", False, "center", ("Courier", 50, "normal"))

    def reset(self):
        self.score = 0
        self.clear()
        self.goto(0, 270)
        self.update_score()
