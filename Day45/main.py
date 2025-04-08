from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")

print(soup.title)