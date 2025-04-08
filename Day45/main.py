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
            
final_result = [i for i in titles_only if i not in ["Director:", "Directors:", "Starring:", "READ MORE:"]]
final_result.reverse()
print(final_result)