from item import Item
from phone import Phone


# we still can set/use the attributes in Item (parent class) by its constructor through Phone (child class) instance
phone1 = Phone("jscPhone10", 500, 5, 1)

# we still can access the attributes in Item (parent class) by the Phone instance
print(phone1.price)
print(phone1.name)