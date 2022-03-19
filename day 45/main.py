# from bs4 import BeautifulSoup
# import requests
# respons = requests.get("https://news.ycombinator.com/")
# yr_web_page = respons.text
# 
# soup = BeautifulSoup(yr_web_page,"html.parser")
# headings = soup.find_all(name="a",class_="titlelink")
# article_texts = []
# article_links = []
# 
# for tag in headings:
#     text = tag.get_text()
#     article_texts.append(text)
#     link = tag.get("href")
#     article_links.append(link)
# article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name = "span" ,class_="score")]
# index = article_upvotes.index(max(article_upvotes))
# print(article_texts[index])
# print(article_links[index])
# print(article_upvotes[index])

# #import lxml
# with open("website.html","r") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# #print(soup.prettify())
# all_anchor_tag = soup.find_all(name="a")
# for tag in all_anchor_tag:
#     #print(tag.getText())
# #    print(tag.get("href"))
#     pass
# heading = soup.find(name="h1",id="name")
# #print(heading)
# section_heading = soup.find(name="h3",class_= "heading")
# #print(section_heading.getText())
# #print(all_anchor_tag)
# company_url = soup.select_one(selector="p a")
# print(company_url)
# name = soup.select_one(selector="#name").getText()
# print(name)
#
# classes = soup.select(".heading")
# print(classes)

# from bs4 import BeautifulSoup
# import requests
# URL = "https://www.empireonline.com/movies/features/best-movies-2/"
# response = requests.get(URL)
# movies_page = response.text
#
# soup = BeautifulSoup(movies_page,"html.parser")
# ALL_MOVI = soup.find_all(name="h3",class_="jsx-4245974604")
# for movi in ALL_MOVI:
#     print(movi)

#top 100 movies of all time using web Scraping with beautifuSoup

import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")