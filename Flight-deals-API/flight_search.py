import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city):
        self.city = city
        self.API_ENDPOINT = "YOUR_API_ENDPOINT_HERE"
        self.API_KEY = "YOUR_API_KEY_HERE"

    def search_for_IATA_code(self):
        headers = {
            "apikey" : self.API_KEY,
        }
        
        params = {
            "term" : self.city
        }
        
        response = requests.get(self.API_ENDPOINT, params=params, headers=headers) 
        response.raise_for_status()
        city_code = response.json()["locations"][0]["code"]
        return city_code