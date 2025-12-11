import requests
from bs4 import BeautifulSoup
response=requests.get("https://books.toscrape.com/")
response.encoding='utf-8'

soup = BeautifulSoup(response.text, "html.parser")
soup2=soup.find_all('article',class_="product_pod")
for book in soup2:
   name=book.find('h3').a.text
   print(name)
   price=book.find('div',class_="product_price").find('p',class_='price_color').text.replace(' £', ' ')
   print(price)
   rating=book.find('p',class_="star-rating")
   rating_text=rating["class"][1]
   print(rating_text)

