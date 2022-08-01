import turtle
import pandas as pd

screen = turtle.Screen()

screen.title("U.S. State Game")
image = "./blank_states_img.gif"
screen.addshape(image) # load the .gif file

turtle.shape(image) # display the .gif

data_of_50_states_csv = pd.read_csv("./50_states.csv")
all_states = data_of_50_states_csv["state"].to_list()



guessed_states = [] # stored the correct guessed state

while len(guessed_states) < 50: # keep repeating the quiz prompt if not all correct
    answer_state = screen.textinput(title = f"You get {len(guessed_states)}/50 States Correct", 
                                    prompt = "What's another state's name").title() # prompt an input box to let user input state name
    # record the states that not get guessed correct into a csv file
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:  # iterate item in the all states list
            if state not in guessed_states: # iterate every state in the list and check if the state is in the guessed correct list
                missing_states.append(state) # if not, add the state name into the missing state list
        missing_state_dataframe = pd.DataFrame(missing_states) # generate a dataframe/dataset
        missing_state_dataframe.to_csv("States_that_not_guessed_correct.csv") # convert and save into a csv file
        
        break
    if answer_state in all_states:
        guessed_states.append(answer_state) # add the correct state into a list
        state_name_pen = turtle.Turtle() # create the turtle object for writing the state name
        state_name_pen.hideturtle()
        state_name_pen.penup()
        state_row = data_of_50_states_csv[data_of_50_states_csv["state"] == answer_state] # extract the row of the correct state
        state_name_pen.goto(int(state_row["x"]), int(state_row["y"])) # move the pen to the state position
        state_name_pen.write(answer_state, move=False, align="center", font=("Arial", 8, "normal"))  # or `data_of_50_states_csv["states"].item()` -> return first value






# # get the x, y coordinate on the image by mouse click
# def get_mouse_click_coordinate(x, y):
#     print(x, y)
    
# turtle.onscreenclick(get_mouse_click_coordinate)


