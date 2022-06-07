import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

gesture_image = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors \n"))

if (user_choice > 2):
    print("Invalid Input!")
else:
    print(gesture_image[user_choice])
    
    computer_choice = random.randint(0,2)
    
    print("\nComputer chose:")
    print(gesture_image[computer_choice])
    
    if (user_choice == computer_choice):
        print("Tie")
    elif (user_choice == 0 and computer_choice == 1):
        print("You lose")
    elif (user_choice == 1 and computer_choice == 2):
        print("You lose")
    elif (user_choice == 2 and computer_choice == 0):
        print("You lose")
    else:
        print("You win")

