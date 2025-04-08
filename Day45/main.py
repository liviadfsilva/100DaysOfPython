from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")

articles = soup.find("div", class_="article_article-content__3auQJ false")
titles = articles.find_all("strong")

titles_only = []

for i in titles:
    result = i.getText()
    titles_only.append(result)
            
# print(titles_only)

for i in titles_only:
    if i == "Director:" or i == "Starring:":
        titles_only.remove(i)
        
print(titles_only)