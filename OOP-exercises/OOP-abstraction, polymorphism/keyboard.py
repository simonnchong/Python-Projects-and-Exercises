from item import Item

class Keyboard(Item):

    pay_rate = 0.5 # redefine the pay_rate in Item (parent class) because of polymorphism
    
    def __init__(self, name: str, price: float, quantity = 0): 
        super().__init__(name, price, quantity)