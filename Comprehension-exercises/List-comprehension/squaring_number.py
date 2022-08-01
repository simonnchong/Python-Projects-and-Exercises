numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [number * number for number in numbers]
# or
squared_numbers2 = [number ** 2 for number in numbers]
# or
squared_numbers3 = [pow(number, 2) for number in numbers]

#Write your code 👆 above:

print(squared_numbers)