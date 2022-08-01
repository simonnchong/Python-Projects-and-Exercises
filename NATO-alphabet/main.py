# reference: Pandas-exercises\Pandas-iterate-over-dataframe.py

from sys import stdlib_module_names
import pandas as pd
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pd.read_csv("./nato_phonetic_alphabet.csv")

# store the dataframe from csv file and convert into a new dictionary by using dictionary comprehension
alpha_dict = {row.letter : row.code for index, row in data.iterrows()} 


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Input a word: ").upper()

# find the user input from dictionary by letter
result = [alpha_dict[letter] for letter in user_word]

# #* in traditional way
# result = []
# for letter in user_word:
#     result.append(alpha_dict[letter])


print(result)


# example output:
# input -> simon
# output -> ['Sierra', 'India', 'Mike', 'Oscar', 'November']