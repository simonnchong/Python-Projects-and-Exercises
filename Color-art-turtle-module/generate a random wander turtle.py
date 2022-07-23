# generate a random wander turtle

from turtle import Shape, Turtle, Screen
from turtle import *
from random import randint, choice

turtle = Turtle()
screen = Screen()

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b) # return a tuple

turtle.shape("arrow")
turtle.color("pink")
turtle.width(6)
turtle.speed(0) # 1(slow) ... 10(fast), 0 is fastest
screen.colormode(255)

# turtle.hideturtle() # to hide the pen shape

directions = [0, 90, 180, 270]

for _ in range(10000):
    turtle.color(random_color())

    turtle.setheading(choice(directions)) # setheading() rotate in 0, 90, 180, 270 angle
    turtle.forward(30)
    print(_)


    
done() # keep the screen after the process is finish