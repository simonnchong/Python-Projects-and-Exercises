# general code
# `new_dict` = {`new_key`:`new_value` for `key`, `value` in `dict`.items() if `condition/test`}

from random import randint

#* ------------------------------------------------ using ordinary dictionary approach ------------------------------------
# the score is randomly set
student_scores = {
    "Alex" : randint(0, 100),
    "Beth" : randint(0, 100),
    "Caroline" : randint(0, 100),
    "Dave" : randint(0, 100),
    "Eleanor" : randint(0, 100),
    "Freddie" : randint(0, 100),
}

#* ------------------------------------------------ using dictionary comprehension approach ------------------------------------

student_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores2 = {student_name:randint(0, 100) for student_name in student_list}

# add the student_scores dictionary into a new_dictionary
student_scores3 = {student_name:score for student_name, score in student_scores.items()}

# add condition, check who passed the exam
passed_student = {student_name:score for (student_name, score) in student_scores2.items() if student_scores2[student_name] > 60}