import csv
from numpy import integer

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount, this is a class attribute that not belong to any instance/object
                   # but still it still can be accessed via an instance
    all_items = []
    

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

        # adding all the item into a class level list
        Item.all_items.append(self)

    def calculated_total_price(self):   # calculate the price for each item
        return self.price * self.quantity
    

    def apply_discount(self):
        self.price = self.price * self.pay_rate # if no instance level pay_rate being assigned, it will get it from class level, line 5

    
    #* use class method because we have a structured dataset (csv, JSON, yaml) and call the constructor in class it self
    # we pass the data from outside of the file instead of passing an instance, that's why no self as parameter but cls => class
    @classmethod
    def instantiate_from_csv(cls):
        # here will be using csv library 
        with open('item.csv', 'r') as file: #* open(file_name, permission)
            reader = csv.DictReader(file)   # get the data from the file and save into an object
            items = list(reader)    # convert the object into a list and save into a variable
        
        for item in items:
            #? print(item) # only see a bunch of dictionary instead of a list because it has been iterated
            Item(item["name"], float(item["price"]), int(item["quantity"])) # call item class constructor then assign the data from csv into it, convert data type from string into float and int for price and quantity respectively
            #* or Item(item.get("name"),item.get("price"), item.get("quantity"))
    
    #* use static method when the method not specifically belong to any instance
    # you may put this method outside the class since it doesn't belong to any instance, but still not recommended because it is still related to the class
    # doesn't receive the self instance itself as the argument
    @staticmethod
    def is_an_integer(num):
        # check and count if the decimal points are zero    
        # eg: 10.0, 5.0
        if isinstance(num, float): # check if the num is a float data type
            return num.is_integer() # return True if the float value is a whole number like 10.0, 5.0 instead of 10.1, 10.2.....
        elif isinstance(num, int): # check if the num is a int data type
            return True
        else:
            return False


    def __repr__(self): # an iterate => a "representing" in magic methods, return all the existing instances in string form instead of an object
        return f"Item('{self.name}', {self.price}, {self.quantity})\n"

Item.instantiate_from_csv()
print(Item.all_items) # without __repr__, we only can see the object form in console because we append entire object into the list

print(Item.is_an_integer(7.4)) # access @staticmethod in line 55

#! you can call the class method and static method from an instance, but there is no reason to do so, e.g:

#! item1 = Item()
#! item1 = instantiate_from_something()
#! item1 = is_an_integer(5)