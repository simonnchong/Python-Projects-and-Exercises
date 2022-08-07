# reference: Pandas-exercises\Pandas-iterate-over-dataframe.py

import pandas as pd

{"A": "Alfa", "B": "Bravo"}

data = pd.read_csv("./nato_phonetic_alphabet.csv")

alpha_dict = {row.letter : row.code for index, row in data.iterrows()} 

def user_input():
    user_word = input("Input a word: ").upper()
    return user_word

while True:
    try:
        result = [alpha_dict[letter] for letter in user_input()]
    except KeyError:
        print("Sorry, please insert alphabet only")
        user_input()
    else:
        print(result)    
        break


