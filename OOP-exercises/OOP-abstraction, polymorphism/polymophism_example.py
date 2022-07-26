name = "Simon"
from keyboard import Keyboard


print(len(name))

list = ["Hello", "World"]
print(len(list))

# see the len(), a built-in function can received different data type as its arguments
# or we say it can handle different kinds of objects

##########################################################################
item1 = Keyboard("Keyboard 1", 10, 2)

# instance of Keyboard class can access `apply_discount()` method in Item class and redefine the pay_rate because of polymorphism
print(item1.price)
item1.apply_discount()
print(item1.price)