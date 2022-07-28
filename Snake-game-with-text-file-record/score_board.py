from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle): # set the inheritance parent class name -> Turtle, so we don't have to create a instance like this -> food = Turtle(), just use the "self" as the instance 
    def __init__(self):
        super().__init__() # inherit the constructor form parent
        self.score = 0 # initialize the score
        self.highest_score = 0 # initialize the highest score
        self.color("white") # set the scoreboard color
        self.penup() # dont draw the line when move the scoreboard to top of the screen
        self.goto(0, 350) # move the scoreboard to top of the screen
        self.update_score()
        self.hideturtle() # dont show the turtle

    def update_score(self):
        self.clear() # clear the initial score that has been called in constructor
        self.write(f"Your Score: {self.score}, Highest Score: {self.highest_score}", move = False, align = ALIGNMENT, font = FONT) # set the score board properties

    def plus_one_point(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        self.update_score()