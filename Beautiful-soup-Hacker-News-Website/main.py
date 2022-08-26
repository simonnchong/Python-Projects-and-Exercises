# this is a program to grab the article with highest vote from https://news.ycombinator.com/ by using Beautiful Soup

import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/") # grab the web page source from the website
webpage_source = response.text # convert the object into string form
# print(type(webpage_source))
# <class 'str'>

soup = BeautifulSoup(webpage_source, "html.parser") # convert the object into BeautifulSoup object
# print(type(soup))
# <class 'bs4.BeautifulSoup'>

article_tag =  soup.find_all(name="a", class_="titlelink") # get all the element with <a> tag and "titlelink" class

# get_text() OR getText()
article_titles = [article.get_text() for article in article_tag] # get the title of all articles and store into a list
article_links = [article.get("href") for article in article_tag] # get tge link of all articles abd store into a list
article_upvote_nums = [int(score.getText().split()[0]) for score in soup.find_all("span", "score")] # find the upvote number of each article



print(article_titles)
print(article_links)
print(article_upvote_nums)

# print(type(article_upvote_nums))
# <class 'str'>

highest_vote = max(article_upvote_nums) # find the highest vote
highest_vote_index = article_upvote_nums.index(highest_vote) # find the index of highest vote among all articles from a list 

# print all info of the highest vote article
print("-" * 150)
print(article_titles[highest_vote_index])
print(article_links[highest_vote_index])
print(article_upvote_nums[highest_vote_index])



# ------------------------------------------------------- NOTE -----------------------------------------------------------------------

print(article_upvote_nums[0])
# 387 points

# to extract the number out of the string, there are 2 ways to achieve

# 1.replace " points" to a empty string
# replace(" points", "")
# 387

# 2.split the string by space and only retrieve the first element 
# article_upvote_nums[0].split()[0]
# 387
