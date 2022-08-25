#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint

data_manager = DataManager() 
sheet_data = data_manager.get_data()

# get the data from Google sheet
# pprint(sheet_data.get_data())
# [
#  {'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
#  {'city': 'Berlin', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
#  {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
#  {'city': 'Sydney', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
#  {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
#  {'city': 'Kuala Lumpur', 'iataCode': '', 'id': 7, 'lowestPrice': 414},
#  {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
#  {'city': 'San Francisco', 'iataCode': '', 'id': 9, 'lowestPrice': 260},
#  {'city': 'Cape Town', 'iataCode': '', 'id': 10, 'lowestPrice': 378}
# ]

for item in sheet_data: # iterate over "sheet_data" list
    # if item["iataCode"] == "": # check if the content in "iataCode" column is empty, then update the column
    # flight_search = FlightSearch(item["city"]) # get the data in "city" column
    # flight_search_result = flight_search.search_for_IATA_code() # get the iata_code
    # item["iataCode"] = flight_search_result # save the iata_code into the dictionary
    # data_manager.update_data(flight_search_result, item["id"])
    FlightData(item["city"])