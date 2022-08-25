import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.API_ENDPOINT = "YOUR_API_ENDPOINT_HERE"
        # {
        #   'prices': [
        #         {'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
        #         {'city': 'Berlin', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
        #         {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
        #         {'city': 'Sydney', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
        #         {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
        #         {'city': 'Kuala Lumpur', 'iataCode': '', 'id': 7, 'lowestPrice': 414},
        #         {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
        #         {'city': 'San Francisco', 'iataCode': '', 'id': 9, 'lowestPrice': 260},
        #         {'city': 'Cape Town', 'iataCode': '', 'id': 10, 'lowestPrice': 378}
        #   ]
        # }
        
    def get_data(self): # return the value in "price" key
        get_response = requests.get(self.API_ENDPOINT) # request the data from sheety API
        get_response.raise_for_status() # raise error message if any error occurs
        self.data = get_response.json() # save the data into a dictionary
        return self.data["prices"] 
        
    def update_data(self, iata_code_params, column_id): 
        '''update the "IATA Code" column in Google sheet, iata_code_params, get the response from the FlightSearch class via main, column_id from main'''
        # define the data will be updated to Google sheet
        iata_code = { 
            "price": { # "price" will be singular here, get the name from last word in API address
                "iataCode": iata_code_params, # update the "IATA Code" column in Google sheet, Sheety requires the column in Camel case, so -> "iataCode"
            }
        }
        put_response = requests.put(f"{self.API_ENDPOINT}/{str(column_id)}", json=iata_code) # put request to the Google sheet
        print(put_response.json()) # to see the response message         