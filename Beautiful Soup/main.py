from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.find_all(name="span", class_="titleline")

article_titles = []
article_links = []
article_upvotes = []

for i in article_tag:
    a_tag = i.find("a")      
    
    if a_tag:
        upvotes = i.find_next(name="span", class_="score")
        if upvotes:
            all_votes = int(upvotes.getText().split()[0])
            article_upvotes.append(all_votes)
        
        href = a_tag.get("href")
        article_links.append(href)
        
        article_text = a_tag.getText()
        article_titles.append(article_text)
        
# print(article_titles)
# print(article_links)
# print(article_upvotes)

largest_number = max(article_upvotes)
max_index = article_upvotes.index(largest_number)

print(article_titles[max_index])
print(article_links[max_index])
print(largest_number)