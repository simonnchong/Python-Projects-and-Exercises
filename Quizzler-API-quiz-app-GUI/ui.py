from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface(Tk): # if without inherit from Tk class, you have to create object like so, `self.window = Tk()`, `self.window.title("GUI QUIZ GAME")`
    def __init__(self, quiz_brain: QuizBrain): # receive quiz brain object from QuizBrain class
        super().__init__() # inherit from Tk() class
        self.quiz = quiz_brain # save the quiz brain object into a class properties
        self.title("GUI QUIZ GAME") # set the window title
        self.config(padx=20, pady=20, bg=THEME_COLOR) # set the padding x and y, background color
        
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 18, "italic")) # create score label
        self.score_label.grid(row=0, column=1, sticky="E") # stick to East, means right side of the grid position
        
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, font=("Arial", 20, "italic"), text="hahaahhaahah", fill=THEME_COLOR, width=280) # width -> to wrap the text longer than the canvas
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)
        
        false_icon = PhotoImage(file="./images/false.png") # we dont use `self` here because we dont need it at somewhere else other than set the image for the button
        self.false_button = Button(image=false_icon, command=self.false_button)
        self.false_button.grid(row=2, column=0)
        
        true_icon = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_icon, command=self.true_button)
        self.true_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.mainloop()
        
    def get_next_question(self):
        self.score_label.config(text=f"Score: {self.quiz.score}") # update the score label
        if self.quiz.still_has_questions(): # if still has more question currently
            q_text = self.quiz.next_question() # get next question
            self.canvas.itemconfig(self.question_text, text=q_text) # display next question
            self.canvas.config(bg='white') # change the background of canvas back to white
        else: # if no more question left in the question_bank list
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the question bank. Good Job!") # update the question text if no more question left in the question_bank list
            self.true_button.config(state="disable") # disable the buttons if no more question available
            self.false_button.config(state="disable")
            self.canvas.config(bg='lightblue') # change the question canvas background to lightblue
        
    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True")) # give_feedback() will receive a boolean when user get correct or wrong answer

    def false_button(self):
        self.give_feedback(self.quiz.check_answer("False")) # give_feedback() will receive a boolean when user get correct or wrong answer

    def give_feedback(self, is_right: bool): # feedback when user get correct or wrong answer
        if is_right: # if user get the correct answer
            self.canvas.config(bg='lightgreen') # change the canvas background color to lightgreen
        else: # if user get the wrong answer
            self.canvas.config(bg='pink')  # change the canvas background color to lightgreen
        self.after(1000, self.get_next_question) # stay showing the background color in canvas for 1 second and call get_next_question() after that 
        