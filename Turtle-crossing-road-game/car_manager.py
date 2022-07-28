from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    
    def create_car(self):
        random_chance = randint(1, 6) # create the random chance to reduce the car quantity
        if random_chance == 1 :
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid = 1, stretch_len = 2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-280, 280) # use for the y-coordinate of the random car to start on
            new_car.goto(310, random_y) # set the random car to the initial position (on right of screen)
            self.all_cars.append(new_car) # add the card object into the list


    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE) # moving the car backward because the car is initially facing east direction
            car.backward(self.car_speed) # the initial car speed when the game start

    def level_up(self):
        self.car_speed += MOVE_INCREMENT # increase the car speed when it reach the destination