from turtle import Turtle, Screen, done, title
from random import randint
from tkinter import messagebox

screen = Screen()
title("Turtle racing game! Make a guess what color of turtle will win in a run!") # set the window name

is_race_start = False

turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black"]
starting_y_position = [170, 120, 70, 25, -25, -70, -120, -170]

screen.setup(width = 1000, height = 800) # setup the initial window screen size, keyword arguments here

all_turtles = []

#* draw the goal line
draw_goal_line = Turtle()
draw_goal_line.width(4)
draw_goal_line.hideturtle()
draw_goal_line.penup()
draw_goal_line.goto(x = 450, y = 300)
draw_goal_line.pendown()
draw_goal_line.goto(x = 450, y = -300)


#* set the turtle color, starting point before the race start
for turtle_index in range(0, 8):
    turtle = Turtle(shape = "turtle") # there is an shape argument in Turtle class constructor
    # turtle.speed(0)
    turtle.color("black", turtle_colors[turtle_index]) # set different color for each turtle, color(penColor, fillColor)
    turtle.penup()
    turtle.goto(x = -450, y = starting_y_position[turtle_index]) # set the turtle position
    all_turtles.append(turtle)

user_bet = screen.textinput(title = "Make your bet", prompt = f"Choose a turtle which gonna win in the race: \n ({', '.join(turtle_colors)}) ") # this will prompt out an input windows, textinput(title of the prompt, message)

if user_bet: # if user_bet is exist, when user input something, return true
    is_race_start = True

#* race is start here
while is_race_start:
    for turtle in all_turtles:
        if turtle.xcor() > 430: # compare if the turtle x-coordinate over the goal
            is_race_start = False # stop the loop when one of the turtles reach the goal
            print(f"The {turtle.fillcolor()} won the game!") # see which color of turtle reach the goal, only get the fill color without pen color
            winning_color = turtle.fillcolor()
            if winning_color == user_bet:
                messagebox.showinfo("You won!", f"You win the bet! {winning_color} turtle won!") # prompt winning message, showinfo(title of the prompt, message)
            else:
                messagebox.showinfo("You lost!", f"You lost the bet! {winning_color} turtle won!") # prompt losing message, showinfo(title of the prompt, message)
            break
        random_distance = randint(0, 10)
        turtle.forward(random_distance)


done()