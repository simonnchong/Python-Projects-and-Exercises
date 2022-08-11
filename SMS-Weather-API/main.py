# this is an application to send SMS if there is raining possibility in next 12 hours

import requests
from twilio.rest import Client
import os

#* get the weather form the API here
# sign in and get free API key here https://openweathermap.org/current
api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

#! This is to get the environment variable from the `env` command, this is for hiding the value purpose
#! Set a new environment variable by typing IN TERMINAL-> `export variable_name = value_here`
#! Don't forget to import "os" module
api_key = os.environ.get("YOUR_API-KEY_HERE")
#! If you wanna host the code on somewhere else, and you have to export the environment variable in order to work
#! Each environment variable is separated by a ";", and run the program ".py" file at the end of the command
#! By typing command `export variable_name = value_here; export variable_name = value_here; python main.py `

# the weather api requires certain parameter to get the data
api_parameter = {
    "lat" : 1.354214,
    "lon" : 110.401856,
    "appid" : api_key,
    "exclude" : "current,minutely,daily"
}

response = requests.get(api_endpoint, api_parameter)
response.raise_for_status()
weather_data =  response.json()

print(weather_data) # see data.json for the output

print(weather_data["hourly"][0]["weather"][0]["id"]) # try get the weather code for first hour
print(weather_data["hourly"][:12][0]["weather"][0]["id"]) # try to get the weather code for the next 12 hours 

# get the weather condition code greater than 700 which indicates got possibility to rain from the data, and save into a new list
weather_condition_code_of_next_12_hours = [hour_data["weather"][0]["id"] for hour_data in weather_data["hourly"][:12] if hour_data["weather"][0]["id"] < 700]

print(weather_condition_code_of_next_12_hours)

#* get the SMS services API here
# sign-in and send SMS via this website https://www.twilio.com/
account_sid = os.environ.get("YOUR_ACCOUNT_SID_HERE") # replace your account sid
auth_token = os.environ.get("TWILIO_AUTH_TOKEN") # replace your authentication token


if len(weather_condition_code_of_next_12_hours) > 0: # if the list consist of at least 1 item means there is a weather code is greater than 700, which means got a raining possibility
    print("It's raining!")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create( # this above backslash is to escape the line break 
                     body="It seems gonna rain today, don't forget to bring your umbrella ☔.", # the content of message body
                     from_="Your number here", # replace your phone number here
                     to="Receiver's number here" # replace receiver's number here
                 )
                
    print(message.sid)
    print(message.status)   