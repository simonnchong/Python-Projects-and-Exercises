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
        random_chance = randint(1, 6) # create the random chance
        if random_chance == 1 :
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid = 1, stretch_len = 2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-280, 280)
            new_car.goto(310, random_y)
            self.all_cars.append(new_car)


    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT