from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # this is use to click keyboard

chrome_driver_path = "C:\Other\chromedriver.exe" # can be either "/" or "\"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")


# ------------------------------------------------------------ CLICK A LINK ------------------------------------------------------------

total_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(total_articles.text)
total_articles.click() # to auto click the <a> link

# if you wanna click base on a link name
view_history = driver.find_element(By.LINK_TEXT, "View history")
view_history.click()




# ------------------------------------------------------------ CLICK A BUTTON ------------------------------------------------------------

language_setting_button = driver.find_element(By.CSS_SELECTOR, "button.uls-settings-trigger") # look for a <button> tag with a "uls-settings-trigger" class
language_setting_button.click()




# ------------------------------------------------------------ TYPE TEXT ------------------------------------------------------------

search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("Hello Simon!", Keys.ENTER)




# ------------------------------------------------------------ EXERCISE: SIGN UP AN ACCOUNT ------------------------------------------------------------

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
submit_button = driver.find_element(By.CSS_SELECTOR, "form button")

first_name.send_keys("Simon")
last_name.send_keys("Chong")
email.send_keys("simon@gmail.com")
submit_button.click()


# driver.quit()