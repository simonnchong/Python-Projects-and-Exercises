# NOTE All the program will be executed with Google Chrome
# NOTE The testing website is: https://www.python.org/

from selenium import webdriver
from selenium.webdriver.common.by import By

# check your chrome version and download the correct web driver from here: https://chromedriver.chromium.org/downloads
# read Selenium documentation: https://selenium-python.readthedocs.io/getting-started.html#simple-usage


# define the downloaded driver path 
chrome_driver_path = "C:\Other\chromedriver.exe" # can be either "/" or "\"
# set the path to the webdriver class
driver = webdriver.Chrome(executable_path=chrome_driver_path)


# open up a tab in browser
driver.get("https://www.python.org/")




# ------------------------------------------------------------ FIND SINGLE ELEMENT ------------------------------------------------------------

#* find by id
search_button = driver.find_element(by=By.ID, value="submit")
# <button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">GO</button>

print(search_button.text) # get the text of tag
# GO

print(search_button.tag_name) # get the tag name
# button

print(search_button.get_attribute("title")) # get the value of a attribute
# Submit this Search


#* find by class
introduction = driver.find_element(By.CLASS_NAME, "introduction")
print(introduction.text) # get the text of tag
# Python is a programming language that lets you work quickly
# and integrate systems more effectively. Learn More




#* find a input field by name
search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder")) # get the value of a attribute



#* find a link by CSS selector
# use CSS selector when there is no specific class for a tag, it is a hierarchy in its parent
documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# <div class="small-widget documentation-widget">
#   <h2 class="widget-title"><span aria-hidden="true" class="icon-documentation"></span>Docs</h2>
#   <p>Documentation for Python's standard library, along with tutorials and guides, are available online.</p>
#   <p><a href="https://docs.python.org">docs.python.org</a></p>
# </div>

print(documentation_link.text)
# docs.python.org      



success_stories = driver.find_element(By.CSS_SELECTOR, ".success-story-item a")
print(success_stories.text)
# Python and its broad variety of libraries are very well suited to develop customized machine learning tools which tackle the complex challenges posed by financial time series.


#* find a element by XPATH
# This is the most specific finding way to look for a specific data by its node path
faq = driver.find_element(By.XPATH, "//*[@id='container']/li[3]/ul/li[5]/a") # relative path
faq = driver.find_element(By.XPATH, "/html/body/div/footer/div[1]/div/ul/li[3]/ul/li[5]/a") # absolute path
print(faq.text)
# FAQ



# ------------------------------------------------------------ FIND MORE THAN 1 ELEMENTS ------------------------------------------------------------

# find all the upcoming event times
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time") # in a class "event-widget", then <time> tag
for time in event_times:
    print(time.text)

# find all the upcoming event titles
event_titles = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a") # in a class "event-widget", then <li> tag, then <a> tag
for title in event_titles:
    print(title.text)

event_dict = {}

# store it into a dictionary
for x in range(len(event_times)):
    event_dict[x] = {
        "time" : event_times[x].text,
        "title" : event_titles[x].text,
    }

print(event_dict)
# {0: {'time': '2022-09-03', 'title': 'PyCon APAC 2022'}, 1: {'time': '2022-09-07', 'title': 'NZPUG-Auckland: Crafting Software'}, 2: {'time': '2022-09-09', 'title': 'PyCon SK 2022'}, 3: {'time': '2022-09-10', 'title': 'PyBay 2022'}, 4: {'time': '2022-09-12', 'title': 'PyHEP 2022'}}






# close a single tab in browser
# driver.close()
# close entire browser
driver.quit()


# NOTE For locating elements, here is the reference: https://selenium-python.readthedocs.io/locating-elements.html#locating-elements
# find_element(By.ID, "id")
# find_element(By.NAME, "name")
# find_element(By.XPATH, "xpath")
# find_element(By.LINK_TEXT, "link text")
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")