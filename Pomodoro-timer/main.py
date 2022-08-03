# this is a pomodoro timer app, it's work as below technique
# Using this method, you break your workday into 25-minute chunks separated by 
# five-minute breaks. These intervals are referred to as pomodoro.
# After about four pomodoro, you take a longer break of about 20 minutes.

#* 1. work (25 minutes)
#* 2. short break (5 minutes)
#* 3. work (25 minutes)
#* 4. short break (5 minutes)
#* 5. work (25 minutes)
#* 6. short break (5 minutes)
#* 7. work (25 minutes)
#* 8. long break (20 minutes)



from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT_SIZE = 30
FONT_STYLE = "bold"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

repetition = 0 # as the counter to count the repetition of timer
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    '''stop and reset the timer and repetition when reset button is pressed'''
    window.after_cancel(timer) # stop the timer
    canvas.itemconfig(timer_text, text = "00:00") # different config style because it was created in a canvas
    title_label.config(text = "Timer") # reset the timer text
    check_mark.config(text = "") # reset the check to nothing
    global repetition # without this "global", we are unable to change the value outside the function but only can read
    repetition = 0 # reset the repetition counter


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    '''start count down when start button is pressed'''
    global repetition 
    repetition += 1

    work_second = WORK_MIN * 60
    short_break_second = SHORT_BREAK_MIN * 60
    long_break_second = LONG_BREAK_MIN * 60
    
    
    if repetition % 8 == 0: # check if this is the 8th round of repetition
        count_down(long_break_second) 
        title_label.config(text = "Long Break", fg = "red") # change the title text and color in different session 
    elif repetition % 2 == 0: # if the repetition is in a even round number
        count_down(short_break_second)
        title_label.config(text = "Short Break", fg = "pink")

    else:
        count_down(work_second)
        title_label.config(text = "Work", fg = "green")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    '''a recursive function, wait for a certain period and the interaction, (1000 ms, function name, optional function argument)
    after every 1 second, call this function, count - 1'''
    
    count_minute = count // 60  # convert the seconds into minute and its floor number
    count_second = count % 60
    
    # to avoid the second being displayed in a single decimal value like so.... 15:9, 15.8 but 15:09, 15:08 instead
    if count_second < 10:
        count_second = f"0{count_second}"
    
    canvas.itemconfig(timer_text, text = f"{count_minute}:{count_second}") # update the timer text, (object you wanna edit, text you wanna replace)
    
    if count >= 1: # stop the counter if it is lower than 1
        global timer
        timer = window.after(1000, count_down, count - 1) 
    else:
        start_timer() # start the timer again if finish 1 round
        marks = ""
        work_session = repetition//2
        for _ in range(work_session): # count the round of current session
            marks += "✔"
        check_mark.config(text = marks)   

    


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx = 100, pady = 50, bg = YELLOW) # set the window padding and background color


#* ------------------------------------------------------- title -------------------------------------------------------
title_label = Label(text = "Timer", bg = YELLOW, fg = GREEN,  font = (FONT_NAME, 50, FONT_STYLE))
title_label.grid(row = 0, column = 1)


#* ------------------------------------------------------- canvas -------------------------------------------------------
canvas = Canvas(width = 200, height = 240, bg = YELLOW, highlightthickness = 0) # create a canvas to place the UI/elements, and set the background color, highlightthickness = 0 is to remove the border between image and canvas
tomato_img = PhotoImage(file = "./tomato.png") # load the image
canvas.create_image(100, 112, image = tomato_img) # create image, x and y position, in pixel. And image object
timer_text = canvas.create_text(100, 125, text = "00:00", fill = "white", font = (FONT_NAME, FONT_SIZE, FONT_STYLE)) # create a text, x and y position. And content, font properties
canvas.grid(row = 1, column = 1)


#* ------------------------------------------------------- start button -------------------------------------------------------
start_button = Button(text = "Start", command = start_timer)
start_button.grid(row = 2, column = 0)


#* ------------------------------------------------------- reset button -------------------------------------------------------
reset_button = Button(text = "Reset", command = reset_timer)
reset_button.grid(row = 2, column = 2)


#* ------------------------------------------------------- check mark -------------------------------------------------------

check_mark = Label(fg = GREEN, bg = YELLOW)
check_mark.grid(row = 2, column = 1)





window.mainloop()