from turtle import Turtle

FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1 
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align = "left", font = FONT)

    
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"Game Over, your highest level is {self.level}", align = "center", font = FONT)
