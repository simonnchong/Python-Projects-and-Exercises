# ------------------------------------------- Create a DataFrame from Lists ----------------------------------------
import pandas as pd
data = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
df = pd.DataFrame(data, columns=['character']) # columns is used for the header of the column
print(df)
#   character
# 0         a
# 1         b
# 2         c
# 3         d
# 4         e
# 5         f
# 6         g


data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data, index=[1, 2, 3], columns=['Name','Age']) # index to define the index
print(df)
#      Name  Age
# 0    Alex   10
# 1     Bob   12
# 2  Clarke   13

# you can change the data type of the data
df = pd.DataFrame(data, columns=['Name','Age'], dtype=float)
print(df)
#      Name   Age
# 0    Alex  10.0
# 1     Bob  12.0
# 2  Clarke  13.0


# ------------------------------------------- Create a DataFrame from Dict of ndarrays / Lists ----------------------------------------
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)
#     Name  Age
# 0    Tom   28
# 1   Jack   34
# 2  Steve   29
# 3  Ricky   42


data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)
#         Name  Age
# rank1    Tom   28
# rank2   Jack   34
# rank3  Steve   29
# rank4  Ricky   42


# ------------------------------------------- Create a DataFrame from Dict of List of Dicts ----------------------------------------
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
#    a   b     c
# 0  1   2   NaN
# 1  5  10  20.0


data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print(df)
#         a   b     c
# first   1   2   NaN
# second  5  10  20.0



data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df1)
#         a   b
# first   1   2
# second  5  10
print(df2)
#         a  b1
# first   1 NaN
# second  5 NaN


# ------------------------------------------- Create a DataFrame from Dict of Series ----------------------------------------
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)
#    one  two
# a  1.0    1
# b  2.0    2
# c  3.0    3
# d  NaN    4