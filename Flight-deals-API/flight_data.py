from datetime import datetime, timedelta
import requests

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, destination):
        self.price = 0
        self.departure_airport_code = "LON"
        self.departure_city = ""
        self.destination = destination
        date_from = datetime.now() + timedelta(days=1)
        date_to = datetime.now() + timedelta(days=180)
        self.formatted_date_from = date_from.strftime("%d%m%Y")
        self.formatted_date_to = date_to.strftime("%d%m%Y")
        return_from = date_from + timedelta(days=7)
        return_to = date_to + timedelta(days=28)
        self.formatted_return_from = return_from.strftime("%d%m%Y")
        self.formatted_return_to = return_to.strftime("%d%m%Y")
        self.API_ENDPOINT = "YOUR_API_ENDPOINT_HERE"
        
        self.headers = {
            "apikey" : "YOUR_API_KEY_HERE",
        }
        
        self.api_params = {
            "fly_from" : self.departure_airport_code,
            "fly_to" : self.destination,
            "date_from" :  self.formatted_date_from,
            "date_to" : self.formatted_date_to,
            "return_from" : self.formatted_return_from,
            "return_to" : self.formatted_return_to,
        }
        
        self.response = requests.get(self.API_ENDPOINT, params=self.api_params, headers=self.headers)
        self.response.raise_for_status()
        print("done")