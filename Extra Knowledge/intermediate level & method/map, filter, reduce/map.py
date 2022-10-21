items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

prices_only = list(map(lambda item : item[1], items))
print(prices_only)
# [10, 9, 12]

prices_only = list(map(lambda item : item[1] > 10, items)) # different from filter, this will return Boolean from the condition instead of filter out
print(prices_only)
# [False, False, True]