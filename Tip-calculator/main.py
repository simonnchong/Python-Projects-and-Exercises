#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

percentage = 1+(tip/100)

result = total / num_people * percentage

result = "{:.2f}".format(result) # to display the 2 decimal point although the last digit is 0, eg: 33.6 then we will get 33.60
message = f"Each person should pay: ${result}"
print(message)