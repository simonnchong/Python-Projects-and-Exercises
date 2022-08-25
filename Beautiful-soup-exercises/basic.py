from bs4 import BeautifulSoup

with open("./website.html", encoding="utf8") as contents: # read and specify the unicode here
    data = contents.read()


print(data)
# <!DOCTYPE html>
# <html>

# <head>
#         <meta charset="utf-8">
#         <title>Simon's Personal Site</title>
# </head>

# <body>
#         <h1 id="testing">Hello World</h1>
#         <h1 id="name">Simon Chong</h1>
#         <p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em></p>
#         <p>I am an iOS and Web Developer. I ❤️ coffee and motorcycles.</p>
#         <hr>
#         <h3 class="heading">Books and Teaching</h3>
#         <ul>
#                 <li>The Complete iOS App Development Bootcamp</li>
#                 <li>The Complete Web Development Bootcamp</li>
#                 <li>100 Days of Code - The Complete Python Bootcamp</li>
#         </ul>
#         <hr>
#         <h3 class="heading">Other Pages</h3>
#         <a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>
#         <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>
# </body>

# </html>



soup = BeautifulSoup(data, "html.parser") # BeautifulSoup(markup_data, "data_type")


#* find the object data
print(soup) 
# <!DOCTYPE html>
# <html>
# <head>
# <meta charset="utf-8"/>
# <title>Simon's Personal Site</title>
# </head>
# <body>
# <h1 id="testing">Hello World</h1>
# <h1 id="name">Simon Chong</h1>
# <p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em></p>
# <p>I am an iOS and Web Developer. I ❤️ coffee and motorcycles.</p>
# <hr/>
# <h3 class="heading">Books and Teaching</h3>
# <ul>
# <li>The Complete iOS App Development Bootcamp</li>
# <li>The Complete Web Development Bootcamp</li>
# <li>100 Days of Code - The Complete Python Bootcamp</li>
# </ul>
# <hr/>
# <h3 class="heading">Other Pages</h3>
# <a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>
# <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>
# </body>
# </html>



#* find the object data in formatted/indented format
print(soup.prettify()) 
# <!DOCTYPE html>
# <html>
#  <head>
#   <meta charset="utf-8"/>
#   <title>
#    Simon's Personal Site
#   </title>
#  </head>
#  <body>
#   <h1 id="testing">
#    Hello World
#   </h1>
#   <h1 id="name">
#    Simon Chong
#   </h1>
#   <p>
#    <em>
#     Founder of
#     <strong>
#      <a href="https://www.appbrewery.co/">
#       The App Brewery
#      </a>
#     </strong>
#     .
#    </em>
#   </p>
#   <p>
#    I am an iOS and Web Developer. I ❤️ coffee and motorcycles.
#   </p>
#   <hr/>
#   <h3 class="heading">
#    Books and Teaching
#   </h3>
#   <ul>
#    <li>
#     The Complete iOS App Development Bootcamp
#    </li>
#    <li>
#     The Complete Web Development Bootcamp
#    </li>
#    <li>
#     100 Days of Code - The Complete Python Bootcamp
#    </li>
#   </ul>
#   <hr/>
#   <h3 class="heading">
#    Other Pages
#   </h3>
#   <a href="https://angelabauer.github.io/cv/hobbies.html">
#    My Hobbies
#   </a>
#   <a href="https://angelab#* findauer.github.io/cv/contact-me.html">
#    Contact Me
#   </a>
#  </body>
# </html>



#* find all data in text only, without the html tag
print(soup.get_text())
# Simon's Personal Site

# Hello World
# Simon Chong
# Founder of The App Brewery.
# I am an iOS and Web Developer. I ❤️ coffee and motorcycles.

# Books and Teaching

# The Complete iOS App Development Bootcamp
# The Complete Web Development Bootcamp
# 100 Days of Code - The Complete Python Bootcamp


# Other Pages
# My Hobbies
# Contact Me




#* find the type of soup object
print(type(soup))
# <class 'bs4.BeautifulSoup'>



#* find first all data with "title" html tag name
print(soup.title)
# <title>Simon's Personal Site</title>



#* find the html tag name
print(soup.title.name)
# title



#* find the content in <p> <em> hierarchy 
print(soup.p.em)
# <em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em>



#* find the content only of the "title" html tag
print(soup.title.string)
# OR
print(soup.title.get_text())
# Simon's Personal Site



#NOTE `find()` will return the first element, `find_all()` return all element as a list

#* find a specific data with specific tag and id
print(soup.find(id="testing"))
# <h1 id="testing">Hello World</h1>

print(soup.find(name="h1", id="name"))
# <h1 id="name">Simon Chong</h1>

print(soup.find_all(name="h3", class_="heading")) # in order to avoid class reserve keyword, it is `class_` instead
# <h3 class="heading">Books and Teaching</h3>

print(soup.find_all(name="h3", class_="heading")) # in order to avoid class reserve keyword, it is `class_` instead
# [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]




#* find all content with <a> html tag, return a list
print(soup.find_all(name="a"))
# [<a href="https://www.appbrewery.co/">The App Brewery</a>, <a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>, <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>]




#* iterate over a data list that used with `find_all()` method
for item in soup.find_all(name="a"):
    #* find all data in only text, without html tag
    print(item.get_text()) 
    # The App Brewery
    # My Hobbies
    # Contact Me
    #* find the data with "href" attribute
    print(item.get("href")) 
    # https://www.appbrewery.co/
    # https://angelabauer.github.io/cv/hobbies.html
    # https://angelabauer.github.io/cv/contact-me.html



#* find the attribute value inside a tag
print(soup.h3.get("class"))
# ['heading']



#* find element by using CSS selector
#NOTE `select_one()` will return the first element, `select()` return all element as a list

#* find a element that in a deep hierarchy by tag name
# you may remove the `selector` keyword here, just `soup.select_one("p em strong a")`
print(soup.select_one(selector="p em strong a")) # find the element in a <p>, then <em>, then <strong>, then <a> tag
# <a href="https://www.appbrewery.co/">The App Brewery</a>


#* find a element that in a deep hierarchy by id
print(soup.select_one(selector="#name"))
# <h1 id="name">Simon Chong</h1>


#* find a element that in a deep hierarchy by class
print(soup.select_one(selector=".heading"))
# <h3 class="heading">Books and Teaching</h3>


#* find all elements that in a deep hierarchy by class
print(soup.select(selector=".heading"))
# [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]