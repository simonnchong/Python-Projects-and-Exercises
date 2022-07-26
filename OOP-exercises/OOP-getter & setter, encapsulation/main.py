from item import Item

item1 = Item("My Item", 750)

#! can't access this attribute because it is private
# print(item1.__name)

#! but you can access via its getter
print(item1.name) # this is the getter method, line 29 @property -> `name()`

#! can't edit this attribute because it is private
# item1.__name = "New name"
# print(item1.__name)

#! but you can edit it via its setter
item1.name = "New name"  # this is the setter method, line 36 @name.setter-> `name()`
print(item1.name)