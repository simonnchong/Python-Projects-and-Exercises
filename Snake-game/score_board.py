from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle): # set the inheritance parent class name -> Turtle, so we don't have to create a instance like this -> food = Turtle(), just use the "self" as the instance 
    def __init__(self):
        super().__init__() # inherit the constructor form parent
        self.score = 0 # initialize the score
        self.color("white") # set the scoreboard color
        self.penup() # dont draw the line when move the scoreboard to top of the screen
        self.goto(0, 350) # move the scoreboard to top of the screen
        self.update_score()
        self.hideturtle() # dont show the turtle

    def update_score(self):
        self.write(f"Your Score: {self.score}", move = False, align = ALIGNMENT, font = FONT) # set the score board properties

    def plus_one_point(self):
        self.score += 1
        self.clear() # clear the initial score that has been called in constructor
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)