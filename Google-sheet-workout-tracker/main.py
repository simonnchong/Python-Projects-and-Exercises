# this is a workout tracker by using natural language to store the data into Google sheet with Nutritionix API

import requests
from datetime import datetime as dt
import os


#* ---------------------------------------------------------- NUTRITIONIX API ----------------------------------------------------------------
# get your api here -> https://www.nutritionix.com/business/api
# read the API documentation here -> https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#

NUTRITIONIX_API_ENDPOINT = os.environ.get("NUTRITIONIX_API_ENDPOINT")
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
AUTHORIZATION = os.environ.get("AUTHORIZATION")

headers = {
    "x-app-id" : NUTRITIONIX_APP_ID,
    "x-app-key" : NUTRITIONIX_API_KEY,
}

nutritionix_params = {
    "query": input("Enter your workout information here: "),
    "gender":"male",
    "weight_kg":80,
    "height_cm":188.88,
    "age":24,
}

nutritionix_response = requests.post(url=NUTRITIONIX_API_ENDPOINT, json=nutritionix_params, headers=headers)
print(nutritionix_response.json())


#* ------------------------------------------------------------------ GOOGLE SHEETY ---------------------------------------------------------------------
# get your api here -> https://sheety.co/, create a new project, link to the created Google sheet, enable GET, POST, PUT, DELETE base on your needs


SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

# get the current datetime
current_datetime = dt.today()
current_date = current_datetime.strftime("%d/%m/%Y")
current_time = current_datetime.strftime("%H:%M:%S")
print(current_date)
print(current_time)

# get the needed data from Nutritionix json -> exercise, duration, calories
nutritionix_data = nutritionix_response.json()

headers = {
    "Authorization": AUTHORIZATION
    }

# iterate over the nutritionix_data list
for exercise in nutritionix_data["exercises"]:
    # the keys must be in camelCase although they are upper case in your Google sheet, eg: in your Google sheet, 
    # header name is "My First Name", to define the key, you have to write "myFirstName"
    json = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise" : exercise["name"].title(), 
            "duration(mins)" : exercise["duration_min"],
            "calories" : exercise["nf_calories"],
        }
    } 


    response = requests.post(url=SHEETY_ENDPOINT, json=json, headers=headers)
    print(response.json())