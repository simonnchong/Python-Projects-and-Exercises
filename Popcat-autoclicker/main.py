from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Other\chromedriver.exe" # can be either "/" or "\"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://popcat.click/")

cat_image = driver.find_element(By.ID, "app")

while True:
    cat_image.click()