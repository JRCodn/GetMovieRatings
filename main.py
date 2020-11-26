import bs4
import requests
from bs4 import BeautifulSoup
text = input("test: ")

# simple web scraper to get movie ratings

res = requests.get("http://google.com/search?q={}".format(text))

if res.status_code == 200:

    soup = bs4.BeautifulSoup(res.text,'html.parser')


    test = soup.find_all(class_="BNeawe s3v9rd AP7Wnd")[0].text

print(test)