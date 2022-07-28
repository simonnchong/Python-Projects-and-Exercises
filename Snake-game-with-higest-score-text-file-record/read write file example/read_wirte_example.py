
#* .......................reading the file ..................

# file = open("my_text.txt")
# file_contents = file.read()
# print(file_contents)
# file.close()

#! the above codes are same operation as...

with open("my_text.txt") as file:
    file_contents = file.read()
    print(file_contents)

# by using "with" keyword, Python will handle the file to close, 
# need no manual closing file action as on line 4
# "as" keyword to rename the file
# by default, the mode is only for reading


#* .......................writing the file ..................

# if the mode is "w" which is write mode, but the file doesn't exist, it will be created
with open("my_text2.txt", mode = "a") as file: # mode = "r" -> read, "w" -> write, "a" -> append
    file.write("\nNew insertion")