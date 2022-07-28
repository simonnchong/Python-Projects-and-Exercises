from turtle import Screen, done
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

WALL_EDGE = 370

screen = Screen()

screen.setup(width = 800, height = 800) # set the output window size
screen.bgcolor("black") # background color
screen.title("Simon's Snake Game") # set the output window title
screen.tracer(0) # turn off the animation/disable the renderer of the turtle moving route when a turtle/segment moving from a position to another position

snake = Snake()
food = Food()
score_board = ScoreBoard()

# user is able to control the snake by pressing arrow key or "WASD"
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "Down")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "d")

game_is_running = True # keep the game running/looping
while game_is_running:
    snake.move()
    screen.update() # display the snake after moved to a new position, use with screen.tracer(0) on line 10
    time.sleep(0.1) # delay 0.1 second then display the new position again

    # detect collision with food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.new_position()
        snake.extend_snake()
        score_board.plus_one_point()

    # detect collision with food
    if snake.head.xcor() > WALL_EDGE or snake.head.xcor() < -WALL_EDGE or snake.head.ycor() > WALL_EDGE or snake.head.ycor() < -WALL_EDGE:
        score_board.reset()

    # detect collision with food
    for segment in snake.snake_segments[1:]: # iterate each segment in entire snake and only get the segments other than the head (first segment)
        if snake.head.distance(segment) < 10:
            score_board.reset()

screen.exitonclick()