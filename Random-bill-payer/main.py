import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total_participant = len(names)

random_number = random.randint(0, total_participant-1)
who_pay_for_the_meal = names[random_number]

print(who_pay_for_the_meal + " is going to buy the meal today!")
