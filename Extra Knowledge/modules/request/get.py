# importing the requests library
import requests
from pprint import pprint

# api-endpoint
URL = "http://maps.googleapis.com/maps/api/geocode/json?"

# location given here
location = "tun razak exchange kuala lumpur"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location}

# sending get request and saving the response as response object
response = requests.get(url = URL, params = PARAMS, verify=False)

# extracting data in json format
data = response.json()

print(response.raise_for_status)
pprint(data)

dic = dict(key1='value1', key2='value2')
print(dic)
