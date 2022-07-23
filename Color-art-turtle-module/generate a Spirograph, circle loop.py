# generate a Spirograph, circle loop

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
# turtle.width(6)
turtle.speed(0) # 1(slow) ... 10(fast), 0 is fastest
screen.colormode(255)



def draw_spirograph(angle_of_rotation):
    for _ in range(round(360/angle_of_rotation)):
        turtle.color(random_color())
        turtle.circle(200)
        turtle.right(angle_of_rotation)
        print(_)

draw_spirograph(5)


turtle.hideturtle() # to hide the pen shape

    
done() # keep the screen after the process is finish