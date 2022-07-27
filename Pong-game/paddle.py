from turtle import Turtle

MOVING_STEP = 40

class Paddle(Turtle):
    def __init__(self, position : tuple): # receive the x and y coordinate in a tuple for initializing the starting position
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup() 
        self.goto(position) # receive initial position from "position" tuple, then move the paddle to the edge of screen, for both left and right paddle

    def go_up(self):
        if self.ycor() < 350:
            new_y = self.ycor() + MOVING_STEP # get the current paddle y position and + 20 when press "w" arrow key
            self.goto(self.xcor(), new_y) # remain the x coordinate, we only wanna move its y coordinate position

    def go_down(self):
        if self.ycor() > -350:
            new_y = self.ycor() - MOVING_STEP # get the current paddle y position and - 20 when press "s" arrow key
            self.goto(self.xcor(), new_y) # remain the x coordinate, we only wanna move its y coordinate position