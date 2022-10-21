# reference = https://www.pythontutorial.net/python-basics/python-unpacking-tuple/
# unpack means to split each item in tuple into a single variable

(x, y) = (1, 2)
print(x, y)
# 1 2

# swap 2 item without a temporary variable.
(x, y) = (y ,x)
print(x, y)
# 2 1

(x, y) = (10, 20, 30)
# ValueError: too many values to unpack (expected 2)

(x, y, _) = (10, 20, 30)
print(x, y, _) # may use "_" marks the variable is not important, it's a regular/dummy variable
# 20 20 30

(r, g, *other) = (192, 210, 100, 0.5, "hello") # only one * can be used
print(r, g, other)
# 192 210 [100, 0.5], 'hello'


# unpack the tuple and merge into a single variable
odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)
numbers = (*odd_numbers, *even_numbers)
# or 
# numbers = (odd_numbers+even_numbers)
print(numbers)