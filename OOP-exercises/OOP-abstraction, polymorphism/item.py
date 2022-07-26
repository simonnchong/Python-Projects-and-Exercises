import csv

class Item:
    pay_rate = 0.8
    
    def __init__(self, name: str, price: float, quantity = 0): 

        assert price >= 0, f"Price {price} cannot be negative value"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative value"

        self.__name = name
        self.__price = price
        self.quantity =  quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate # if no instance level pay_rate being assigned, it will get it from class level, line 5

    @property
    def price(self):
        return self.__price
