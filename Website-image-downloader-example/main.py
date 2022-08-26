import os
import shutil
import requests
from bs4 import BeautifulSoup

# read all the website links from the text file
with open("./link.txt") as link_file: # open the file
    links = link_file.readlines() # read all lines and save in a list
final_link = [link.strip() for link in links] # remove the space before and after for each item

for link in final_link: # run the task base on the number of link
    
    # https://www.hello.net/2022/05/hello-world.html
    folder_name = link.split("/")[5].split(".")[0] # extract a part of the link as the folder name

    URL = link
    FOLDER_NAME = folder_name

    response = requests.get(URL) # get the data from website
    soup = BeautifulSoup(response.text, "html.parser") # parse into a beautiful object

    div_tags = soup.find_all("div", class_="separator") # find the element with <div> tag with "separator" class

    #* here is one of the example output of the "div_tags" list
    # [ <div class="separator" style="clear: both;">
    # <a href="https://aaaaaaa.jpg" 
    # style="display: block; padding: 1em 0; text-align: center; "><img alt="" border="0" data-original-height="900" data-original-width="634" src="aaaaaaa.jpg"/>
    # </a>
    # </div> .... ]

    #* after get the all entire <div> tag with class="separator", we need to get the value of "href" attribute, it is inside <a> tag
    div_list = [div_tag.img.get("src") for div_tag in div_tags] # extract only the image source link into a new list

    x = 0 # for counter and file name use
    for img_src in div_list: # iterate over the image source link list
        x += 1 # plus 1
        get_image = requests.get(img_src, stream=True) # stream is used to prevent large responses from entirely loading into the memory at once.

        folder = f"./{FOLDER_NAME}/image{x}.jpg" # make and new folder and new empty image file
        os.makedirs(os.path.dirname(folder), exist_ok=True) # create a folder if it is not exist, `exist_ok=True` means do not raise error when folder if already exist 

        with open(folder, 'wb') as f: # "wb" is write binary because we want to write a image instead of a string
            shutil.copyfileobj(get_image.raw, f)  # write the downloaded image and save it into the created empty .jpg file as binary data and save the image into the folder
        print(f"Done {x} in {FOLDER_NAME}") # see the progress by printing the number of object being written

print("Tasks Completed!")