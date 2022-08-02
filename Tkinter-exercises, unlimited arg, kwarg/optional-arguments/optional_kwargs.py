# learn about "**kwargs"
# you can rename the "**kwargs" to any parameter name

def calculate(n, **kwargs):
    '''the argument will be in a dictionary, accessible by key'''
    print(f"This a dictionary args {kwargs}")
    print(f"The value with \"a\" key is {kwargs['a']}")
    print(f"This item is not found: {kwargs.get('z')}") 
    # by using .get('key') in dictionary, it will return "None" if the key is not found in the dictionary, 
    # since there is no 'z' key being passed via the function argument, so it return "None"
    
    sum = 0
    for value in kwargs.values():
        sum += value
        print(sum)
        
    n += kwargs['b']
    n += kwargs['x']
    
calculate(2, a = 3, b = 4, x = 6)
# This a dictionary args {'a': 3, 'b': 4, 'x': 6}
# The value with "a" key is 3
# 3
# 7
# 13