from tkinter import *
import requests
from random import choice 


def get_quote():
    url = "https://type.fit/api/quotes" 

    response = requests.get(url) # get the object from endpoint
    response.raise_for_status() # raise an error if failed to fetch data from API
    quote_dict = response.json() # get the json into a dictionary in a list
    random_quote = choice(quote_dict) # pick randomly a quote from the list
    canvas.itemconfig(quote_text, text=random_quote["text"]) # only get the text
    print(random_quote["text"])



window = Tk()
window.title("Keep Motivating!")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

next_image = PhotoImage(file="./next.png", width=30, height=30)
next_button = Button(image=next_image, highlightthickness=0, command=get_quote)
next_button.grid(row=1, column=0)



window.mainloop()
