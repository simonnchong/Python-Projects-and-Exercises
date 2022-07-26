from item import Item
from phone import Phone


item1 = Item("Item 1", 500, 5)

# abstraction example
# this three methods are not accessible because they are private
item1.__connect_smtp("A")
item1.__write_email()
item1.__upload_image()

# but ou can call the public method that calls the private methods
item1.send_email()

