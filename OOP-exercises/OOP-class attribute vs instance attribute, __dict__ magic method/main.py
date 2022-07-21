class Item:
    pay_rate = 0.8 # The pay rate after 20% discount, this is a class attribute that not belong to any instance/object
                   # but still it still can be accessed via an instance
    def __init__(self, name: str, price: float, quantity = 0): 
        # self is the created instance itself like in line 27 => item1
        # "name: str" is to set the datatype of parameter to avoid int as the argument input mistake
        # "quantity = 0" is also to set the datatype and initialize the parameter value at the same time

        # in order to avoid unwanted data, e.g: a negative value being passed into parameter price and quantity, 
        # use "assert" to specify the rule before it get processed
        # the string is the error message will be show if unwanted data being passed into this class constructor
        assert price >= 0, f"Price {price} cannot be negative value"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative value"

        self.name = name
        self.price = price
        self.quantity =  quantity
        
    def calculated_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate # instead od using "Item.pay_rate", since item2 has its own discount rate, 
                                                # so we can use self here, item1 will retrieve the pay_rate from class level because it doesn't has 1
        

item1 = Item("Phone", 100, 10)

# use this magic method to debug
# print all attribute in class level
print(Item.__dict__)
# print all attribute in instance level
print(item1.__dict__)

# to access class level attribute
print(Item.pay_rate)
# item1 is still able to access class attribute when they cannot find their own attribute in their own instance
print(item1.pay_rate)

print(item1.name, "Before discount RM", item1.calculated_total_price())
item1.apply_discount()
print(item1.name, "After discounted RM", item1.calculated_total_price())

# let say you have a different discount rate for item2, so we can specify the pay_rate for its own instance only
item2 = Item("Laptop", 400, 2)
item2.pay_rate = 0.7
print(item2.name, "Before discount RM", item2.calculated_total_price())
item2.apply_discount()
print(item2.name, "After discounted RM", item2.calculated_total_price())
