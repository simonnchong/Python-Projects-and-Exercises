from turtle import Turtle
from random import randint



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 0.1 # initialize the x axis moving speed of the ball
        self.y_move = 0.1 # initialize the y axis moving speed of the ball

    def move(self):
        new_x = self.xcor() + self.x_move # updated the x moving direction
        new_y = self.ycor() + self.y_move # updated the y moving direction
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1 # reverse the x direction, negative to positive, vice versa

    def bounce_y(self):
        self.y_move *= -1 # reverse the y direction, negative to positive, vice versa

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()