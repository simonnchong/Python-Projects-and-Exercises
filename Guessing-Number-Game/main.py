from random import randint
from art import logo
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

print(logo)

EASY_LEVEL = 10
HARD_LEVEL = 5

number_of_attempts = 0
random_number = randint(1,100)

print("Welcome to Simon's Guessing Number Game!")
print("I'm thinking of a number between 1 and 100")
print(f"The answer is {random_number}")

def difficulty_level():
    difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ")

    if difficulty_level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

number_of_attempts = difficulty_level()

repeat = True
while repeat:
    print(f"    You have {number_of_attempts} attempts remaining to guess")
    user_guess = int(input("Make a guess ----> "))

    if (user_guess == random_number):
        print(f"You got it! The answer is {random_number}")
        repeat = False #or => break
    elif (user_guess < random_number):
        print("Too low, guess a higher number")
        number_of_attempts -= 1
    elif (user_guess > random_number):
        print("Too high, guess a lower number")
        number_of_attempts -= 1

    if number_of_attempts == 0:
        print("You lose the game, out of lives")
        repeat = False #or => break
