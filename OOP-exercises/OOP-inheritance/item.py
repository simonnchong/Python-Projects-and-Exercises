import csv

class Item:
    
    def __init__(self, name: str, price: float, quantity = 0): 
        # self is the created instance itself
        # "name: str" is to set the datatype of parameter to avoid int as the argument input mistake
        # "quantity = 0" is also to set the datatype and initialize the parameter value at the same time

        # in order to avoid unwanted data, e.g: a negative value being passed into parameter price and quantity, 
        # use "assert" to do a data validation before it get processed
        # the fstring is the error message will be show if unwanted data being passed into this class constructor
        assert price >= 0, f"Price {price} cannot be negative value"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative value"

        self.name = name
        self.price = price
        self.quantity =  quantity
