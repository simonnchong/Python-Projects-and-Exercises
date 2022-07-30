# this program is to count the number of squirrel in different number from the dataset

import pandas as pd

squirrel_data_set = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = squirrel_data_set["Primary Fur Color"] # extract all the data under "Primary Fur Color" column
grey_fur_color = squirrel_data_set[fur_color == "Gray"] # look for all the rows with the "Gray" from "Primary Fur Color" column
# grey_fur_color["Primary Fur Color"] # get the all rows only for "Primary Fur Color" column
grey_squirrel_count = len(grey_fur_color)

red_fur_color = squirrel_data_set[fur_color == "Cinnamon"]
red_squirrel_count = len(red_fur_color)

black_fur_color = squirrel_data_set[fur_color == "Black"]
black_squirrel_count = len(black_fur_color)

print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

# construct dataframe and save into a csv file
data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

squirrel_dataframe = pd.DataFrame(data_dict) # construct it into a dataframe
squirrel_dataframe.to_csv("squirrel_count.csv") # convert into csv file