from functools import reduce

items = [
    (10),
    (8),
    (12)
]

total_price = reduce(lambda current_item, next_item : current_item + next_item, items)

print(total_price)
# 30