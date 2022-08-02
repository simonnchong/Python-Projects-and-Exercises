import tkinter as tk

window = tk.Tk() # call the class for the window GUI
# write `window = Tk()` if `from tkinter import Tk`
window.title("My first GUI") # set the title of the window
window.minsize(width = 500, height = 300) # scale itself to the content if over the size
window.config(padx = 200, pady = 300) # add space around the window



#? ---------------------------------------------------------------- create label ----------------------------------------------------------------

my_label = tk.Label(text = "Label placeholder", font = ("Arial", 24, "bold")) # set the name will be displayed in the label, and the font properties
# my_label.pack() # place the from top to bottom, logically arrange
# pack(side = "right") # put the label at the right of screen, responsive to window size # left, top, bottom
# pack(expand = True) # put the label at the center of screen, responsive to window size
#! you cant usee pack() and grid() in the same file!!


#* other than the constructor passing setting as on line 9, there are 2 more approaches to do so
my_label["text"] = "Label placeholder" # access the dictionary 
my_label.config(text = "Label placeholder") # access the method of setter


# #* use place() for layout
# my_label.place(x = 0, y = 0) # the origin is at top left corner

#* use grid() for layout
my_label.grid(row = 0, column = 0)

my_label.config(padx = 20, pady = 30) # add space around the widget


#! reference : http://tcl.tk/man/tcl8.6/TkCmd/pack.htm





#? ---------------------------------------------------------------- create button ----------------------------------------------------------------

def button_click():
    entry_input = my_input.get() # receive the input from entry and return the input as string 
    my_label.config(text = entry_input) # change the text of label when button is clicked
    print("I am a button and I got clicked")
    
    
my_button = tk.Button(text = "Button Placeholder", command = button_click) # command receive the name of the function instead of the function itself, so no parenthesis needed


#* use grid() for layout
my_button.grid(row = 2, column = 2)


my_button2 = tk.Button(text = "Button Placeholder", command = button_click) # command receive the name of the function instead of the function itself, so no parenthesis needed


#* use grid() for layout
my_button2.grid(row = 1, column = 3)


#! http://tcl.tk/man/tcl8.6/TkCmd/button.htm







#? ---------------------------------------------------------------- create entry (input box) ----------------------------------------------------------------

my_input = tk.Entry(width = 10) # set the width


#* use grid() for layout
my_input.grid(row = 4, column = 4)


#! http://tcl.tk/man/tcl8.6/TkCmd/entry.htm




window.mainloop() # keep the window display on screen