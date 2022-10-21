import pandas as pd
import numpy as np


# ------------------------------------------- Create a Series from ndarray ----------------------------------------
data = np.array(['a','b','c','d'])

s = pd.Series(data)
print(s)
# 0    a       
# 1    b       
# 2    c       
# 3    d       
# dtype: object

# user define the index number
s = pd.Series(data, index=[100,101,102,103])
print(s)
# 100    a      
# 101    b      
# 102    c      
# 103    d      
# dtype: object 


# ------------------------------------------- Create a Series from dict ----------------------------------------
# key of dictionary will be the index
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data) #If index is passed, the values in data corresponding to the labels in the index will be pulled out
print(s)
# a    0.0      
# b    1.0      
# c    2.0      
# dtype: float64   


data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data, index=['a', 'c']) #If index is passed, the values in data corresponding to the labels in the index will be pulled out
print(s)
# a    0.0      
# c    2.0
# dtype: float64


# ------------------------------------------- Create a Series from scalar ----------------------------------------
s = pd.Series(6, index=[0, 1, 2, 3])
print(s)
# 0    6
# 1    6
# 2    6
# 3    6


# ---------------------------------------- Accessing Data from Series with Position -------------------------------------
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
#retrieve the first element
print(s[0])
# 1

# get first three elements
print(s[:3])
# a    1
# b    2
# c    3

# get the last three elements
print(s[-3:])
# c    3
# d    4
# e    5
# dtype: int64

# ---------------------------------------- Retrieve Data Using Label (Index) -------------------------------------
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve a single element
print(s['e'])
# 5

#retrieve multiple elements
print(s[['a','c','d']])
# a    1
# c    3
# d    4
# dtype: int64