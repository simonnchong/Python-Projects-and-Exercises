import pandas as pd

data = pd.read_csv("./weather_data.csv") # the data will be in both dictionary and object forms
# print(data["day"])
# 0       Monday
# 1      Tuesday
# 2    Wednesday
# 3     Thursday
# 4       Friday
# 5     Saturday
# 6       Sunday
# Name: day, dtype: object

# # convert into dictionary
# data_dict = data.to_dict()
# print(data_dict)
# # {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}

# #* you are allow convert the data under "temp" column into list
# temp_list = data["temp"].to_list()
#* or
# print(temp_list)

#? get data in column
# read all data under "temp" column
# print(data["temp"]) # in dictionary form
# #* or
# print(data.temp) # in object form

# print(data["temp"].mean()) # calculate the mean 
# print(data["temp"].max()) # get the max

#? get data in row
# read the row where day="monday"
# print(data[data["day"] == "Monday"])
#* or
print(data[data.day == "Monday"])

# get the row with the max temperature
print(data[data.temp == data.temp.max()])

# get condition data on Monday
monday = data[data.day == "Monday"] # get the row of Monday
print(monday.condition) # get the condition data on Monday

# convert temperature on Wednesday from celsius into fahrenheit 
wednesday = data[data.day == "Wednesday"] # get the row of Wednesday
wednesday_temp = int(wednesday.temp) # convert into integer
wednesday_temp_in_fahrenheit = wednesday_temp * 9 / 5 + 32 # converting formula
print(wednesday_temp_in_fahrenheit)


#? create dataframe from scratch
data_dict = {
    "students" : ["Simon", "Peter", "Janet"],
    "scores": [76, 56, 65]
}
new_data = pd.DataFrame(data_dict)
print(new_data)

#? convert into csv file
new_data.to_csv("new_data.csv")