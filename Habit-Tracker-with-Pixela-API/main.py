#NOTE This is a program to track your habit by implementing Pixela API with http POST requests, https://pixe.la/ 

import requests
from datetime import datetime as dt

#* ----------------------------------------------------------------------------- CREATE A NEW ACCOUNT (POST)------------------------------------------------------
# https://docs.pixe.la/entry/post-user

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : "YOUR_TOKEN_HERE",
    "username" : "simonnchong",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# NOTE comment this out after user's account is created
response = requests.post(url=pixela_endpoint, json=user_params) 
print(response.text)




#* ---------------------------------------------------------------- LOGIN THE ACCOUNT (AUTHENTICATION) AND CREATE NEW GRAPH (POST) ------------------------------------------------------
# https://docs.pixe.la/entry/post-graph

graph_endpoint = f"{pixela_endpoint}/simonnchong/graphs"

graph_config = {
    "id" : "graph1",
    "name" : "Python Practicing",
    "unit" : "day",
    "type" : "int",
    "color" : "momiji",
}

# this API request a header to send the created token securely, this will be hidden in the url address
headers = {
    "X-USER-TOKEN" : "YOUR_TOKEN_HERE",
}

# NOTE comment this out after a new graph is created
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)




#* ---------------------------------------------------------------------------------- INSERT A PIXEL INTO THE CREATED GRAPH  (POST)------------------------------------------------------
# https://docs.pixe.la/entry/post-pixel

pixel_endpoint = f"{pixela_endpoint}/simonnchong/graphs/graph1"

today_datetime = dt.today() 
formatted_datetime = today_datetime.strftime("%Y%m%d") 

pixel_params = {
    "date" : formatted_datetime, # reference: https://www.w3schools.com/python/python_datetime.asp
    "quantity" : "2",
    "optionalData":"{\"description\":\"Learned HTTP GET TSLA stock API and Pixela API HTTP POST requests\"}"
}

# NOTE comment this out after new pixel is created
responses = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(responses.text)





#* --------------------------------------------------------------------------------- UPDATE/MODIFY A PIXEL INTO THE CREATED GRAPH  (PUT)------------------------------------------------------
# https://docs.pixe.la/entry/put-pixel


pixel_endpoint = f"{pixela_endpoint}/simonnchong/graphs/graph1/{formatted_datetime}"

pixel_params = {
    "quantity" : "1",
}


# NOTE comment this out after new pixel is updated
response = requests.put(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)




#* ----------------------------------------------------------------------------------- DELETE THE CREATED PIXEL (DELETE)------------------------------------------------------
# https://docs.pixe.la/entry/delete-pixel

pixel_endpoint = f"{pixela_endpoint}/simonnchong/graphs/graph1/{formatted_datetime}"


# NOTE comment this out after pixel is deleted
response = requests.delete(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)
