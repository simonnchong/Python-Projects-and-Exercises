# this is a program that get the International Space Station Current Location by using its API

import requests # use to request the API
import datetime as dt

#* ------------------------------------------------------- GET ISS LOCATION -----------------------------------------------------------

response = requests.get(url="http://api.open-notify.org/iss-now.json") # insert the endpoint of the API, get it from http://open-notify.org/Open-Notify-API/ISS-Location-Now/
response.raise_for_status() # a built-in exception handling in requests module, print the response code if failed
data = response.json() # print the json data that extracted from the API in dictionary format
# print(data)
#* {'iss_position': {'latitude': '28.0761', 'longitude': '20.2860'}, 'timestamp': 1659947052, 'message': 'success'}

#? to get the value of iss_position
# print(data["iss_position"] )
#* {'latitude': '35.9607', 'longitude': '29.6054'}


# to get latitude and longitude
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
ISS_position = (longitude, latitude)
print(ISS_position)

#? if the ISS is close to my location, +-5 longitude and latitude


#* ------------------------------------------------------- GET SUNSET TIME OF YOUR CURRENT LOCATION -----------------------------------------------------------

# in older version, this API request 2 parameters, longitude and latitude
# find your longitude and latitude from here https://www.latlong.net/

# set 2 constant as the longitude and latitude

# MY_LONGITUDE = 110.406571
# MY_LATITUDE = 1.360603

# create a dictionary to store the parameters

# api_parameters = {
#     "lat" : MY_LONGITUDE,
#     "lng" : MY_LATITUDE

# }
# response = requests.get("http://api.sunrise-sunset.org/json", params=api_parameters)

response = requests.get("http://api.sunrise-sunset.org/json", {"formatted":0}) # connect to the API, disable the 24 hours format with formatted parameter, this request.get() receive a dictionary as its parameter other than the first one
response.raise_for_status() # raise an error is connection is failed
data = response.json() # get the json data
# print(data)
#* {'results': {'sunrise': '6:01:06 AM', 'sunset': '6:10:13 PM', 'solar_noon': '12:05:39 PM', 'day_length': '12:09:07', 'civil_twilight_begin': '5:40:41 AM', 'civil_twilight_end': '6:30:38 PM', 'nautical_twilight_begin': '5:15:41 AM', 'nautical_twilight_end': '6:55:38 PM', 'astronomical_twilight_begin': '4:50:38 AM', 'astronomical_twilight_end': '7:20:41 PM'}, 'status': 'OK'}

sunrise = data["results"]["sunrise"] # get the sunrise value
sunset = data["results"]["sunset"] # get the sunset value

#? print(sunrise)
# #* 2022-08-08T06:01:06+00:00

# split the time from the sunrise variable
# sunrise.split("T") # split the string into a list when find "T"
# #* ['2022-08-08', '06:01:06+00:00']
# sunrise.split("T")[1] # get the second item in list
# #* 06:01:06+00:00

# sunrise.split("T")[1].split(":") # split the string into a list when find "#"
#* ['06', '01', '06+00', '00']

sunrise_hour = int(sunrise.split("T")[1].split(":")[0]) # get the first item in the list which is hour
print(sunrise_hour)
#* 06

#? print(sunset)
sunset_hour = int(sunset.split("T")[1].split(":")[0]) # get the first item in the list which is hour
print(sunset_hour)


time_now = dt.datetime.now() # get the current time
print(time_now)





#* ------------------------------------------------------- NOTES -----------------------------------------------------------


#? check the responses data
# print(type(data))
# # <class 'dict'>
# print(response) # return response code in object format, indicates if the response succeed or failed, just like 502, 404
# # <Response [200]>
# print(response.status_code)
# # 200
# print(type(response))
# # <class 'requests.models.Response'>


#? Response Code
# Common HTTP status code classes:
# 1xxs – Informational responses: The server is thinking through the request.
# 2xxs – Success! The request was successfully completed and the server gave the browser the expected response.
# 3xxs – Redirection: You got redirected somewhere else. The request was received, but there’s a redirect of some kind.
# 4xxs – Client errors: Page not found. The site or page couldn’t be reached. (The request was made, but the page isn’t valid — this is an error on the website’s side of the conversation and often appears when a page doesn’t exist on the site.)
# 5xxs – Server errors: Failure. A valid request was made by the client but the server failed to complete the request.