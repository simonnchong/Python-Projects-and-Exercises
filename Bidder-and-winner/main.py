from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

more_bidders = True

bidders = {}
highest_price = 0

while more_bidders == True:
    
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid? $"))
    
    bidders[name] = bid_amount

    if bid_amount > highest_price:
        highest_price = bid_amount
        
    anymore_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if anymore_bidders == 'no':
        more_bidders = False
    else:
        clear()

for key in bidders:
    if bidders[key] == highest_price:
        print(f"The winner is {key} with bid of ${highest_price}")
    
# winner_name = bidders[]
# winner_price = 