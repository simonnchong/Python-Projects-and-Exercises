from selenium import webdriver
from selenium.webdriver.common.by import By

service = webdriver.ChromeService()
driver = webdriver.Chrome(service=service)

driver.get("https://popcat.click/")

cat_image = driver.find_element(By.ID, "app")

while True:
    cat_image.click()
