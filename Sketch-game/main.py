# by using "w" "s" "a" "d" and "c" key to interact with the turtle

from turtle import Turtle, Screen, done

turtle = Turtle()
screen = Screen()


# event listener => screen.onkey(fun, key), receive a non-argument function as the argument for itself, so we need to create movement function without argument to pass to it 

def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def turn_left():
    turtle.left(10)


def turn_right():
    turtle.right(10)


def clear_screen():
    turtle.clear()
    turtle.penup() # without penup(), the line will be drawn when the turtle go home on next line
    turtle.home()
    turtle.pendown() # pendown() when turtle get home


screen.listen()
screen.onkey(key = "w", fun = move_forward) # use keyword arguments here, call move_forward() function when "w" key is pressed
screen.onkey(key = "s", fun = move_backward) # use keyword arguments here, call move_backward()  function when "s" key is pressed
screen.onkey(key = "a", fun = turn_left) # use keyword arguments here, call turn_left() function when "a" key is pressed
screen.onkey(key = "d", fun = turn_right) # use keyword arguments here, call turn_right() function when "d" key is pressed
screen.onkey(key = "c", fun = clear_screen) # use keyword arguments here, call turtle.clear function when "c" key is pressed, this is use to clear the current drawing



done()