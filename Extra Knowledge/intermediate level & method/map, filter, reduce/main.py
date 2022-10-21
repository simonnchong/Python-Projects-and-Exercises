# this file is to apply map, filter, and reduce to get the ideal result which is the total price from list
# I wanna to have the total price of all product which above 50

from functools import reduce

items = [
    ("Product1", 95),
    ("Product2", 30),
    ("Product3", 12),
    ("Product4", 11),
    ("Product5", 99),
    ("Product6", 50),
]

# map(), to retrieve price only from the list
prices_list = list(map(lambda item : item[1], items))
print("Prices List:", prices_list)

# filter(), to filter out the price above 50
prices_above_50_list = list(filter(lambda price : price > 50, prices_list))
print("Prices above 50:", prices_above_50_list)

# reduce(), to sum up all prices above 50
total_price = reduce(lambda current_price, next_price : current_price + next_price, prices_above_50_list)
print("Total price:", total_price)
