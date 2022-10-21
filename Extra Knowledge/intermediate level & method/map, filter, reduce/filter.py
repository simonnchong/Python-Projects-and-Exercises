items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

filtered = [(item[0], item[1]) for item in items if item[1] >= 10]
# same as ...
filtered = list(filter(lambda item : item[1] >= 10, items)) # convert the filter object into a list

print(filtered)
# [('Product1', 10), ('Product3', 12)]