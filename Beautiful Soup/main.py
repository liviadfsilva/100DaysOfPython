from bs4 import BeautifulSoup
import lxml

with open("/Users/liviasilva/Documents/Projects/100DaysOfPython/Beautiful Soup/website.html") as web_page:
    content = web_page.read()
    
soup = BeautifulSoup(content, "lxml")