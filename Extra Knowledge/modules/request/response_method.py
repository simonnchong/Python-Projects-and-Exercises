# reference: https://www.geeksforgeeks.org/python-requests-tutorial/

from dataclasses import dataclass
import requests
from pprint import pprint

simon_github_URI = "https://api.github.com/users/simonnchong"
response = requests.get(simon_github_URI, verify=False)
print(response.headers) # returns a dictionary of response headers
print(response.encoding) #  returns the encoding used to decode response.content 
print(response.elapsed) # returns a timedelta object with the time elapsed from sending the request to the arrival of the response
print(response.content) #  returns the content of the response, in bytes
print(response.cookies) # returns a CookieJar object with the cookies sent back from the server
print(response.history) # returns a list of response objects holding the history of request (url)
print(response.is_redirect) # returns True if the response was redirected, otherwise False
print(response.is_permanent_redirect) # returns True if the response is the permanent redirected url, otherwise False
print(response.iter_content()  ) # iterates over the response.content
print(response.url) # returns the URL of the response.
print(response.text) # returns the content of the response, in unicode
print(response.status_code) # returns a number that indicates the status
print(response.request) # returns the request object that requested this response
print(response.reason) # returns a text corresponding to the status code
print(response.raise_for_status()) # returns an HTTPError object if an error has occurred during the process
print(response.ok) # returns True if status_code is less than 200, otherwise False
print(response.links) # returns the header links
print(response.close()) # close the connection to the server
pprint(response.json()) # returns a JSON object of the result (if the result was written in JSON format, if not it raises an error)
print("-"*100)
print(response.close()) # close the connection to the server




#* ----------------------------------------------- NOTES ---------------------------------------------------

# PUT vs PATCH 

# PUT - Replace the entire data
# PATCH - Modify part of data

