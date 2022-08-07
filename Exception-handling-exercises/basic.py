# There are 4 keywords:

#* try: something that might cause an exception
#* except: do this when there is was an exception
#* else: do this when there is were no exceptions
#* finally: do this no matter what happens


#? FileNotFound

# try:
#     file = open("not_exist.txt")
#     print("a"+3) 
# except:
#     print("The file is not existed!")
#     open("make_a_new_file.txt", "w") # in write mode, the file will be created if not existed
    
#! never write other code that might causes an error into the same try block and 
#! exception block, it will not give you error message if it is wrong, but do this instead

try:
    file = open("a_file.txt") # goes to `except FileNotFoundError` if catch an error here, the rest of code will be skipped
    dictionary = {"key" : "value"} 
    print(dictionary["ha"]) # goes to `except KeyError` if previous line doesn't catch error

# if any file not found error occurs in `try` block, this will catch the error    
except FileNotFoundError as message:
    print(f"Can't find the file because {message}")
    new_file = open("a_file.txt", "w") # in write mode, the file will be created if not existed
    new_file.write("Hello World")

# if any key error occurs in try block, this will catch the error
except KeyError as message: # get the error message
    print(f"The key: {message} not found")

# execute this block of code if no more exception from `try` block    
else:
    print("Everything works well, no error from try block")
    


try:
    x=int(input('Enter a number upto 100: '))
    if x > 100:
        raise ValueError("Number cannot over 100")


# execute this block of code no matter what happen:
finally:
    print("I will be executed anyway!")
    raise TypeError("This is an error I made up")


# Error types in Python:
# AssertionError 	Raised when the assert statement fails.
# AttributeError 	Raised on the attribute assignment or reference fails.
# EOFError 	Raised when the input() function hits the end-of-file condition.
# FloatingPointError 	Raised when a floating point operation fails.
# GeneratorExit 	Raised when a generator's close() method is called.
# ImportError 	Raised when the imported module is not found.
# IndexError 	Raised when the index of a sequence is out of range.
# KeyError 	Raised when a key is not found in a dictionary.
# KeyboardInterrupt 	Raised when the user hits the interrupt key (Ctrl+c or delete).
# MemoryError 	Raised when an operation runs out of memory.
# NameError 	Raised when a variable is not found in the local or global scope.
# NotImplementedError 	Raised by abstract methods.
# OSError 	Raised when a system operation causes a system-related error.
# OverflowError 	Raised when the result of an arithmetic operation is too large to be represented.
# ReferenceError 	Raised when a weak reference proxy is used to access a garbage collected referent.
# RuntimeError 	Raised when an error does not fall under any other category.
# StopIteration 	Raised by the next() function to indicate that there is no further item to be returned by the iterator.
# SyntaxError 	Raised by the parser when a syntax error is encountered.
# IndentationError 	Raised when there is an incorrect indentation.
# TabError 	Raised when the indentation consists of inconsistent tabs and spaces.
# SystemError 	Raised when the interpreter detects internal error.
# SystemExit 	Raised by the sys.exit() function.
# TypeError 	Raised when a function or operation is applied to an object of an incorrect type.
# UnboundLocalError 	Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
# UnicodeError 	Raised when a Unicode-related encoding or decoding error occurs.
# UnicodeEncodeError 	Raised when a Unicode-related error occurs during encoding.
# UnicodeDecodeError 	Raised when a Unicode-related error occurs during decoding.
# UnicodeTranslateError 	Raised when a Unicode-related error occurs during translation.
# ValueError 	Raised when a function gets an argument of correct type but improper value.
# ZeroDivisionError 	Raised when the second operand of a division or module operation is zero. 