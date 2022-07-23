# print a n-number of sides of polygon

from turtle import Shape, Turtle, Screen
from turtle import *
from random import randint

turtle = Turtle()
screen = Screen()

turtle.shape("circle")
turtle.color("pink")
screen.colormode(255)

# draw a square

# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# # draw a dashed line
# for _ in range(15):
#     turtle.forward(10)
#     turtle.penup() # draw nothing
#     turtle.forward(10)
#     turtle.pendown() # draw

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(20)
        turtle.right(angle)


# turtle.hideturtle() # to hide the pen shape
turtle.speed(0)
turtle.penup()
turtle.left(90)
turtle.forward(450)
turtle.left(90)
turtle.forward(10)
turtle.right(90)
turtle.right(90)
turtle.pendown()

for num_sides in range(3, 1000): # 3 to 100 number of side
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    turtle.color(r, g, b)
    draw_shape(num_sides)
    print(num_sides)

turtle.done()