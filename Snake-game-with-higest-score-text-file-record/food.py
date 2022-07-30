from hashlib import new
from random import randint
from turtle import Turtle

POSITION = 350
SIZE = 0.5
class Food(Turtle): # set the inheritance parent class name -> Turtle, so we don't have to create a instance like this -> food = Turtle(), just use the "self" as the instance
    def __init__(self):
        super().__init__() # inherit the constructor form parent
        self.shape("circle")
        self.color("red")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len = SIZE, stretch_wid = SIZE) # initial size is 20, so here means 20 * 0.8 = 16
        random_x = randint(-POSITION, POSITION) # get a random number and assign to the food x coordinate
        random_y = randint(-POSITION, POSITION) # get a random number and assign to the food y coordinate
        self.goto(random_x, random_y)
        self.new_position() # call the new_position() function in this class

    def new_position(self):
        random_x = randint(-POSITION, POSITION) # get a random number and assign to the food x coordinate
        random_y = randint(-POSITION, POSITION) # get a random number and assign to the food y coordinate
        self.goto(random_x, random_y)