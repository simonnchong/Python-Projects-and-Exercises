from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = "D:/chromedriver"
driver = webdriver.Chrome(chrome_driver)


driver.get("https://www.python.org/")

driver.implicitly_wait(1)

# Selenium Python provides two types of waits - implicit & explicit. An explicit wait makes selenium wait for a specific condition to occur before proceeding further with execution.
# An implicit wait makes selenium python poll the DOM for a certain amount of time with a 300ms interval when trying to locate an element.

latest_news = driver.find_elements(By.CLASS_NAME, value="widget-title")
for section_title in latest_news:
    print(section_title.text)

text_box = driver.find_element(by=By.CSS_SELECTOR, value="input#id-search-field")
text_box.send_keys("selenium")

submit_button = driver.find_element(by=By.NAME, value="submit")
submit_button.click()

driver.quit()

