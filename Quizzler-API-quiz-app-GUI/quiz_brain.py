import html

class QuizBrain:

    def __init__(self, q_list): # receive question_bank list from main
        self.current_question_number = 0 # initialize current question number
        self.score = 0 # initialize 
        self.question_list = q_list # save the question_bank list into a new list 
        self.current_question = None # initialize current question object

    def still_has_questions(self): # check if still has question in the list when user answering questions
        return self.current_question_number < len(self.question_list) 

    def next_question(self): # produce next question
        self.current_question = self.question_list[self.current_question_number] # get the next question by accessing next index in a list
        self.current_question_number += 1 # increase 1 index for the list
        q_text = html.unescape(self.current_question.text) # unescape from html entities, reference: https://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string
        return f"Q.{self.current_question_number}: {q_text}" # return the question number and text 


    def check_answer(self, user_answer): # check if user's answers is correct
        correct_answer = self.current_question.answer # get the correct for the current question from 
        if user_answer.lower() == correct_answer.lower(): # compare user's answer and real answer
            self.score += 1 # plus 1 score if user's answer is correct
            print(f"{self.current_question_number}, You got it right!")
            return True # return True for true_button() method in ui.py
        else:
            print(f"{self.current_question_number}, You got it wrong!")
            return False # return False for true_button() method in ui.py

