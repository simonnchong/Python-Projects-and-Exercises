# CSV = Comma Separated Values 

# #* this program is to extract the temperature data under "temp" column in "weather_data.csv"
# #* showing the different between, without using csv library, using csv library and using pandas library

# #* read the weather_data.csv
# with open("weather_data.csv") as weather_file:
#      weather_data = weather_file.readlines()
#      print(weather_data)
# # #* ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']

#! but the data is in a list, it is hard to read, the output is:


#* so, there is another way, import "csv" library to read csv file
# import csv

# with open("./weather_data.csv") as data_file:
#     temperatures = []
#     csv_data = csv.DictReader(data_file) # return the data in a dictionary object, iterable
#     # or you may use 
#     # "csv.reader(data_file)",  # return the data in reader object form, iterable,  
#     # "next(data)" # skip the first row of the data which is header
#     # "for row in data:"
#     #   "temperatures.append(int(row[1]))" # row[1] is the temp column
#     for row in csv_data:
#         #* here is the output
#         # print(row)
#         # {'day': 'Monday', 'temp': '12', 'condition': 'Sunny'}
#         # {'day': 'Tuesday', 'temp': '14', 'condition': 'Rain'}
#         # {'day': 'Wednesday', 'temp': '15', 'condition': 'Rain'}
#         # {'day': 'Thursday', 'temp': '14', 'condition': 'Cloudy'}
#         # {'day': 'Friday', 'temp': '21', 'condition': 'Sunny'}
#         # {'day': 'Saturday', 'temp': '22', 'condition': 'Sunny'}
#         # {'day': 'Sunday', 'temp': '24', 'condition': 'Sunny'}
#         temperatures.append(int(row['temp'])) # append the data in integer under "temp" key into a list
       
# print(temperatures)

#! still many steps to achieve the goal

#* so let's use the "pandas" library

import pandas

# no need with open execution, it is auto completed in pandas library
data = pandas.read_csv("./weather_data.csv")
# print(data)
# output
#         day  temp condition
# 0     Monday    12     Sunny
# 1    Tuesday    14      Rain
# 2  Wednesday    15      Rain
# 3   Thursday    14    Cloudy
# 4     Friday    21     Sunny
# 5   Saturday    22     Sunny
# 6     Sunday    24     Sunny

# print(data["temp"]) # access the data "temp" column
print(data["day"])


# read() -> return the file in a string
# readline() -> return a single line from data file into a single string
# readline() -> return each line in data file into a list