from art import logo, vs
from random import choice
from game_data import data
from os import system

def check_who_has_higher_follower():
    if celebrity_A_follower_count > celebrity_B_follower_count:
        return "A"
    else:
        return "B"

score = 0
correct_message = ""
incorrect_message = ""

celebrity_A = choice(data)
celebrity_A_name = celebrity_A["name"]
celebrity_A_follower_count = celebrity_A["follower_counts"]
celebrity_A_description = celebrity_A["description"]
celebrity_A_country = celebrity_A["countries"]

is_correct_answer = True
while is_correct_answer:
    print(logo)
    print(correct_message)

    print(f"Compare A: {celebrity_A_name}, a {celebrity_A_description}, from {celebrity_A_country}")

    print(vs)

    celebrity_B = choice(data)
    celebrity_B_name = celebrity_B["name"]
    celebrity_B_follower_count = celebrity_B["follower_count"]
    celebrity_B_description = celebrity_B["description"]
    celebrity_B_country = celebrity_B["country"]

    print(f"Against B: {celebrity_B_name}, a {celebrity_B_description}, from {celebrity_B_country}")
    print("The answer is: ", check_who_has_higher_follower())

    user_ans = input("Who have more followers? Type 'A' or 'B': ").upper()

    answer = check_who_has_higher_follower()

    if user_ans== answer:
        score += 1
        correct_message = f"You're right, current score: {score}"
        celebrity_A_name = celebrity_B["name"]
        celebrity_A_follower_count = celebrity_B["follower_count"]
        celebrity_A_description = celebrity_B["description"]
        celebrity_A_country = celebrity_B["country"]
        system("cls")
    else:
        is_correct_answer = False # or break
        incorrect_message = f"Sorry, that's wrong. Final score: {score}"
        system("cls")
        print(logo)
        print(incorrect_message)    