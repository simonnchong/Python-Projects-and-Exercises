#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
num_letters= int(input("How many letters would you like in your password?\n")) 
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

generated_password = ""

for letter in range(0, num_letters):
    generated_password += random.choice(letters)
    # same as:
    # random_number = random.randint(0, len(letters) - 1)
    # generated_password += letters[random_number]

for symbol in range(0, num_symbols):
    generated_password += random.choice(symbols)
    # same as:
    # random_number = random.randint(0, len(symbols) - 1)
    # generated_password += symbols[random_number]

for number in range(0, num_numbers):
    generated_password += random.choice(numbers)
    # same as:
    # random_number = random.randint(0, len(numbers) - 1)
    # generated_password += numbers[random_number]

print(generated_password)



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# random.sample return a list, so use join to join them as a string, "" means join with no space
# use "random.shuffle" insted if your data is a list
randomised_order_password = "".join(random.sample(generated_password, len(generated_password)))
print("Your password is : " + randomised_order_password)




# notes

# for letter in letters: //assign each of the item from letters into letter in each loop
#     print(letter)

# ------------------------- same as --------------------------------

# for letter in range(0, len(letters)): //letter will be 0, 1, 2, 3..... to len(letters), //assign each of the item from the range into letter in each loop
#     print(letters[letter])
