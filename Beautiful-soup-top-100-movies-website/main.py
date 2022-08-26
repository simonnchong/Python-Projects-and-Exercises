# this program is to get the top 100 must watch movies and save into a txt file
# website -> https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL) # get all the website page source
soup = BeautifulSoup(response.text, "html.parser") # parse the data from a string form into a html object form

movie_titles = soup.find_all(name="h3", class_="title") # get all movie titles with <h3> tag and "title" class and save into a list

with open("must_watch_movies.txt", "w", encoding="utf8") as movie_file: # create a text file, define the encoding format here
    for movie in movie_titles[::-1]: # reverse the movie list because it was number 100 to 1 descending order, we need 1 to 100 ascending order
        movie_file.write(f"{movie.getText()}\n") # write the title into a txt file