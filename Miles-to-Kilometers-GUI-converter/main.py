import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Mile to KM Converter")
window.minsize(width = 350, height = 320) # responsive to padding size on next line
window.config(padx = 70, pady = 100)



#? ----------------------------------- entry for miles -----------------------------------
miles_entry = tk.Entry(width = 10)
miles_entry.insert(END, string = "0")
miles_entry.grid(row = 0, column = 1)



#? ----------------------------------- label for Miles -----------------------------------
mile_label = tk.Label(text = "Miles")
mile_label.grid(row = 0, column = 2)



#? ----------------------------------- label for is equal to -----------------------------------
is_equal_to_label = tk.Label(text = "is equal to")
is_equal_to_label.grid(row = 1, column = 0)



#? ----------------------------------- label for result -----------------------------------
result_label = tk.Label(text = "0") 
result_label.grid(row = 1, column = 1)



#? ----------------------------------- label for km -----------------------------------
km_label = tk.Label(text = "Km") 
km_label.grid(row = 1, column = 2)


#? ----------------------------------- button for calculate -----------------------------------
def convert():
    # check if the input is integer
    try:
        result = float(miles_entry.get()) * 1.60934 # calculate the result from the entry input
        result_label.config(text = result) # write the calculation result into the result label
        error_label.config(text = "") # reset the error label if input is correct
    except:
        error_label.config(text = "*Please insert \n a valid number")


calculate_button = tk.Button(text = "Calculate", command = convert)
calculate_button.grid(row = 2, column = 1)


#? ----------------------------------- label for input type error -----------------------------------
error_label = tk.Label(fg = 'red') 
error_label.grid(row = 3, column = 1)


window.mainloop()