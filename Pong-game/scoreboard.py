from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.colon = ":"
        self.right_score = 0
        self.update_score_board()
      
    def update_score_board(self):
        self.clear()
        self.goto(-70, 280)
        self.write(self.left_score, align = "center", font = ("Courier", 70, "normal"))
        self.goto(0, 300)
        self.write(self.colon, align = "center", font = ("Courier", 50, "normal"))
        self.goto(70, 280)
        self.write(self.right_score, align = "center", font = ("Courier", 70, "normal"))

    # plus 1 point for left paddle if right paddle miss out the ball 
    def left_point(self):
        self.left_score += 1
        self.update_score_board()
    
    # plus 1 point for right paddle if left paddle miss out the ball 
    def right_point(self):
        self.right_score += 1
        self.update_score_board()
