class Item:
    def __init__(self, name: str, price: float, quantity = 0): 
        # self is the created instance itself like in line 22 => item1
        # "name: str" is to set the datatype of parameter to avoid int as the argument input mistake
        # "quantity = 0" is also to set the datatype and initialize the parameter value at the same time

        # in order to avoid unwanted data, e.g: a negative value being passed into parameter price and quantity, 
        # use "assert" to do a data validation before it get processed
        # the string is the error message will be show if unwanted data being passed into this class constructor
        assert price >= 0, f"Price {price} cannot be negative value"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative value"

        self.name = name
        self.price = price
        self.quantity =  quantity
        
    def calculated_total_price(self):
        return self.price * self.quantity
        
item1 = Item("Phone", 100, 7)
#*same as ....
# item1.name = "Phone"
# item1.price = 100  
# item1.quantity = 5

item2 = Item("Laptop", 400, 2)
# same as ....
# item2.name = "Laptop" 
# item2.price = 400
# item2.quantity = 2
item2.has_numpad = True # we still can create and assign an new attribute to an existing instance although 
# it is not been initialized in the __init__ class, for example here, we wanna see does the laptop has a 
# numpad, but phone doesn't have this stuff, so it is better to create and assign it to a single 
# instance -> item2 which is laptop only

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)

print(item1.calculated_total_price())
print(item2.calculated_total_price())