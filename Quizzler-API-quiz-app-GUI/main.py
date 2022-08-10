from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = [] # save the generated questions in a list
for question in question_data:
    question_text = question["question"] # get the question from the question dictionary
    question_answer = question["correct_answer"] # get the correct answer form the question dictionary
    new_question = Question(question_text, question_answer) # pass the new question and answer to the Question class constructor and save the object into the list
    question_bank.append(new_question)


quiz = QuizBrain(question_bank) # pass the question_bank list to the QuizBrain constructor to process
quiz_ui = QuizInterface(quiz) # generate GUI


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.current_question_number}")