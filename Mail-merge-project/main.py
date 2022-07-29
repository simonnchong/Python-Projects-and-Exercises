# this is a program that read the name in a file -> invited_names.txt and write those names into another a separate new file -> letter_for_name.txt

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

# open the file the read the name and return them in a list
# can be "./Input/Names/invited_names.txt"
# but cannot be "/Input/Names/invited_names.txt" because first "/" is for root when using absolute path
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

        
with open("Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        name_without_new_line = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, name_without_new_line) # replace() will iterate each string and replace the target 
        with open(f"Output/ReadyToSend/letter_for_{name_without_new_line}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)
            # or you may do this
            #! print(new_letter, file = completed_letter)
    

# Python file modes
#     r for reading – The file pointer is placed at the beginning of the file. This is the default mode.
#     r+ Opens a file for both reading and writing. The file pointer will be at the beginning of the file.
#     w Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
#     w+ Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, it creates a new file for reading and writing.
#     rb Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file.
#     rb+ Opens a file for both reading and writing in binary format.
#     wb+ Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, it creates a new file for reading and writing.
#     a Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
#     ab Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
#     a+ Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
#     ab+ Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
#     x open for exclusive creation, failing if the file already exists (Python 3)