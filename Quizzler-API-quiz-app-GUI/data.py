import requests

Trivia_api =  "https://opentdb.com/api.php"

# this api receive some parameters such as "amount" and "type"
# here is the complete api address https://opentdb.com/api.php?amount=10&type=boolean
api_parameter = {
    "amount" : 20,
    "type" : "boolean",
    "category" : 18
}

response = requests.get(Trivia_api, api_parameter)
response.raise_for_status() # raise an error if connection to API is failed
data = response.json() # get all the data in a dictionary form

question_data = data["results"] # get the value with "results" key
