from item import Item

class Phone(Item):
    
    def __init__(self, name: str, price: float, quantity = 0, broken_phone = 0): 
        # call for super() function to access all attributes and methods parent class
        super().__init__(name, price, quantity)

        # add some code only for this class but not existed in parent class
        assert quantity >= 0, f"Broken phone {broken_phone} cannot be negative value"
        self.broken_phone = broken_phone