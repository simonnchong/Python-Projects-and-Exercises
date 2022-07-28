from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)] # initial position of the snakes that has 3 segments and its own positions
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_segments = [] # to store the initial snake body segment
        self.create_snake() # call the create_snake function in this class
        self.head = self.snake_segments[0] # set the first segment as the snake head 

    # initialize the snake
    def create_snake(self):
        for position in STARTING_POSITION: # create 3 different segments of snake body
            self.add_segment(position)

    # add the snake body
    def add_segment(self, position):
        new_snake_segment = Turtle("square") # it is a square for each segment
        new_snake_segment.color("white") # white color
        new_snake_segment.penup() # no line will be drawn when moving
        new_snake_segment.goto(position) # set the initial position from starting_position list
        self.snake_segments.append(new_snake_segment) # store the object into a list for moving

    def extend_snake(self):
        self.add_segment(self.snake_segments[-1].position()) # get the position of the last segment of the snake and pass it to add_segment() function 

    def move(self):
        # this loop is let the other than the first segment will follow the position of first segment after the first segment turn left and right or move to other position
        for seg_num in range(len(self.snake_segments) - 1, 0, -1): # move each of the snake segment starting from last segment position to second last segment position
            new_x = self.snake_segments[seg_num - 1].xcor() # get the x coordinate of second last segment
            new_y = self.snake_segments[seg_num - 1].ycor() # get the y coordinate of second last segment
            self.snake_segments[seg_num].goto(new_x, new_y) # move the last segment to the second segment position
        self.head.forward(MOVING_DISTANCE)
    
    #* defining the moving function by using arrow key
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]