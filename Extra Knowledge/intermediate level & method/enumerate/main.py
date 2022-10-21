# reference: https://www.programiz.com/python-programming/methods/built-in/enumerate
# reference: https://www.pythontutorial.net/python-built-in-functions/python-enumerate/

# enumerate when you wanna count the indices of the iterable item without defining the index counter

grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))
# <class 'enumerate'>

# converting to list since it is a enumerate object, can't access it directly
print(list(enumerateGrocery))
# [(0, 'bread'), (1, 'milk'), (2, 'butter')]

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))
# [(10, 'bread'), (11, 'milk'), (12, 'butter')]

for item in enumerateGrocery:
  print(item)
# # (0, 'bread')
# # (1, 'milk')
# # (2, 'butter')


for count, item in enumerateGrocery:
  print(count, item)
# 0 bread
# 1 milk
# 2 butter

print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)
# 100 bread
# 101 milk
# 102 butter