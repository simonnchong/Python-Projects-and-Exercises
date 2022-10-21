# yield is used to pause the current statement and convert in into a iterable object
#! the iterable object called as a generator, it only can be call iterated once

def greeting():
    print('Hi!')
    yield 1
    print('How are you?')
    yield 2
    print('Are you there?')
    yield 3

iterator_greeting = greeting()

print(type(iterator_greeting))
# <class 'generator'>

print(next(iterator_greeting))
print(next(iterator_greeting))
print(next(iterator_greeting))

print("=" * 100)

# you wont see any output from the code below because line 17, 18, 19 have done the interation
# as mentioned it is agenerator so it only can be interated once
for message in iterator_greeting:
    print("-----------", message) 