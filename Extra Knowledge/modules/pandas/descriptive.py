import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}

#Create a DataFrame
df = pd.DataFrame(d)
print(df)
#       Name  Age  Rating
# 0      Tom   25    4.23
# 1    James   26    3.24
# 2    Ricky   25    3.98
# 3      Vin   23    2.56
# 4    Steve   30    3.20
# 5    Smith   29    4.60
# 6     Jack   23    3.80
# 7      Lee   34    3.78
# 8    David   40    2.98
# 9   Gasper   30    4.80
# 10  Betina   51    4.10
# 11  Andres   46    3.65


#Create a DataFrame
print(df.sum())
# Name      TomJamesRickyVinSteveSmithJackLeeDavidGasperBe...
# Age                                                     382
# Rating                                                44.92
# dtype: object