import tkinter as tk

window = tk.Tk() # call the class for the window GUI
# write `window = Tk()` if `from tkinter import Tk`
window.title("My first GUI") # set the title of the window
window.minsize(width = 500, height = 300) # scale itself to the content if over the size




#? ---------------------------------------------------------------- create label ----------------------------------------------------------------

my_label = tk.Label(text = "Label placeholder", font = ("Arial", 24, "bold")) # set the name will be displayed in the label, and the font properties
my_label.pack() # place the label on screen, place top center in default
# pack(side = "right") # put the label at the right of screen, responsive to window size # left, top, bottom
# pack(expand = True) # put the label at the center of screen, responsive to window size

#! reference : http://tcl.tk/man/tcl8.6/TkCmd/pack.htm

#* other than the constructor passing setting as on line 9, there are 2 more approaches to do so
my_label["text"] = "Label placeholder" # access the dictionary 
my_label.config(text = "Label placeholder") # access the method of setter





#? ---------------------------------------------------------------- create button ----------------------------------------------------------------

def button_click():
    entry_input = my_input.get() # receive the input from entry and return the input as string 
    my_label.config(text = entry_input) # change the text of label when button is clicked
    print("I am a button and I got clicked")
    
    
my_button = tk.Button(text = "Button Placeholder", command = button_click) # command receive the name of the function instead of the function itself, so no parenthesis needed
my_button.pack()

#! http://tcl.tk/man/tcl8.6/TkCmd/button.htm







#? ---------------------------------------------------------------- create entry (input box) ----------------------------------------------------------------

my_input = tk.Entry(width = 10) # set the width
my_input.pack()


#! http://tcl.tk/man/tcl8.6/TkCmd/entry.htm





window.mainloop() # keep the window display on screen