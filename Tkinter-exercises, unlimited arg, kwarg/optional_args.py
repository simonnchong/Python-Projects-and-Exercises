# learn about "*args"
# you can rename the "args" to any parameter name

def add(*args):
    '''the argument will be in a tuple, accessible by index'''
    print(f"This a tuple args {args}")
    print(f"The first argument is {args[0]}")
    
    total = 0
    for num in args:
        total += num
    print (total)

add(1, 2, 3, 4, 5)
# This a tuple args (1, 2, 3, 4, 5)
# The first argument is 1
# 15