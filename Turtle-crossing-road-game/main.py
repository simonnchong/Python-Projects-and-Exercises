import time
from turtle import Screen, done
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()



screen.setup(width = 600, height = 600)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()
screen.title("Simon's turtle crossing game!")

turtle = Player()

screen.onkey(turtle.move_forward, "w")
screen.onkey(turtle.move_left, "a")
screen.onkey(turtle.move_right, "d")
screen.onkey(turtle.move_backward, "s")

car_manager = CarManager()

scoreboard = ScoreBoard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(turtle) < 25:
            game_is_on = False
            scoreboard.game_over()

    #detect if crossing successful
    if turtle.is_reach_finish_line():
        turtle.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

done()