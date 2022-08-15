import os
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY") # get the API key that has been store into environment variable
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params) # get stock data from API
stock_response.raise_for_status()

data = stock_response.json()["Time Series (Daily)"] # get the "Time Series (Daily)" value of the data dictionary
data_list = [value for key, value in data.items()] # get the value from the dictionary

yesterday_data = data_list[0] # get the latest data
yesterday_closing_price = yesterday_data["4. close"] # get closing price of yesterday
print(yesterday_closing_price)

day_before_yesterday = data_list[1] # get the second latest data
day_before_yesterday_closing_price = day_before_yesterday["4. close"] # get the closing price of second latest data
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price)) # compare the price, only in positive 
print(difference)


diff_percent = difference / float(yesterday_closing_price) * 100 # calculate the percentage of difference of price
print(diff_percent)

if diff_percent > 4: # if difference more than 4%
    news_params = {
        "apikey" : NEWS_API_KEY,
        "qInTitle" : COMPANY_NAME,
    }
    
    # get the 3 latest news from the news API
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    latest_three_articles = articles[:3]
    print(latest_three_articles)

    formatted_articles = [f"Headline: {article['title']}. \nDescription: {article['description']}" for article in latest_three_articles]
    print(formatted_articles)
