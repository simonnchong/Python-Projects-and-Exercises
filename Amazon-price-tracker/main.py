import lxml
import requests
from bs4 import BeautifulSoup
import telegram_send

AMAZON_PRODUCT_URL = "https://www.amazon.com/OnePlus-10-Pro-Factory-Unlocked/dp/B09SKXXC87/ref=sr_1_1?keywords=oneplus+1&qid=1661664128&sprefix=oneplus+1-,aps,497&sr=8-1&language=en_US&currency=MYR"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Accept-Language" : "en-US,en;q=0.5",
}

amazon_product_response = requests.post(url=AMAZON_PRODUCT_URL, headers=headers)
amazon_product_response.raise_for_status()
amazon_product_soup = BeautifulSoup(amazon_product_response.text, "lxml")

product_price_whole_number = amazon_product_soup.find(name="span", class_="a-price-whole").getText().split(".")[0]
product_price_decimal = amazon_product_soup.find(name="span", class_="a-price-fraction").getText()
product_price = product_price_whole_number + "." + product_price_decimal
print(float(product_price))

if float(product_price) < 850:
    telegram_send.send(messages=[f"Oneplus 10 pro is now on promotion! Hurry up! Access this link:\n{AMAZON_PRODUCT_URL}"])