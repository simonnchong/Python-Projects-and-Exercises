from turtle import Screen, done
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 1200, height = 800)
screen.title("Pong Pong Pong!!!")
screen.tracer(0) # turn off the animation when paddle moving to edge/initial position

left_paddle = Paddle((-550, 0)) # pass the x and y coordinate in a tuple
right_paddle = Paddle((550, 0)) # pass the x and y coordinate in a tuple

screen.listen()
screen.onkey(left_paddle.go_up, "w") # call go_up function without the parentheses 
screen.onkey(left_paddle.go_down, "s") # call go_down function without the parentheses 
screen.onkey(right_paddle.go_up, "Up") # call go_up function without the parentheses 
screen.onkey(right_paddle.go_down, "Down") # call go_down function without the parentheses 

ball = Ball()
score_board = ScoreBoard()

is_game_on = True
while is_game_on:
    screen.update() # update the paddle after moving to a new position
    ball.move()

    # bounce the ball if touch the top and bottom wall
    current_x_coordinate = ball.xcor()
    current_y_coordinate = ball.ycor()
    if current_y_coordinate > 390 or current_y_coordinate < -390: # check if the ball hit the bottom and top wall -> y-wall/edge
        ball.bounce_y()

    # bounce the ball if touch the both paddles
    if ball.distance(left_paddle) < 50 and ball.xcor() < -540 or ball.distance(right_paddle) < 50 and ball.xcor() > 540: # check if the distance of center of ball and the center of paddle is less than 50, AND before it move over the paddles area
        ball.bounce_x()

    # detect if the ball move over the left wall, if so, reset the game
    if ball.xcor() > 570:
        ball.reset_position()    
        score_board.left_point()
    
    # detect if the ball move over the left wall, if so, reset the game
    if ball.xcor() < -570:
        ball.reset_position()
        score_board.right_point()


done()