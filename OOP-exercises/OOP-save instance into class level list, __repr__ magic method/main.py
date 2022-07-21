class Item:
    pay_rate = 0.8 # The pay rate after 20% discount, this is a class attribute that not belong to any instance/object
                   # but still it still can be accessed via an instance
    all_items = []


    def __init__(self, name: str, price: float, quantity = 0): 
        # self is the created instance itself like in line 27 => item1
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

        # adding all the item into a class level list
        Item.all_items.append(self)


    def calculated_total_price(self):
        return self.price * self.quantity
    

    def apply_discount(self):
        self.price = self.price * self.pay_rate # if no instance level pay_rate being assigned, it will get it from class level, line 2
        
    def __repr__(self): # a loop => representing magic method, return all the existing instances in string form instead of like the result in line 44
        return f"...line 34...Item('{self.name}', {self.price}, {self.quantity}"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# check if all items instance have been passed into the list, line 23
print(Item.all_items)

# print all instance attribute from all_items list that has been assigned in line 21
for instance in Item.all_items:
    print(f"\n----Item name: {instance.name}")
    print(f"    Item price: {instance.price}")
    print(f"    Item quantity: {instance.quantity}")