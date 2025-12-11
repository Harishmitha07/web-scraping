import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import re


url = "https://books.toscrape.com/"
response = requests.get(url)
print(url)
print(response)

soup = BeautifulSoup(response.text, "html.parser")
books = soup.select("article.product_pod")

data = []

for book in books:

    name = book.select_one("h3 a")["title"]

    
    price = book.select_one(".price_color").text
    price_value = float(re.sub(r"[^\d.]", "", price))   # remove £, Â

   
    rating_class = book.select_one("p.star-rating")["class"][1]

   
    data.append({
        "Name": name,
        "Price": price_value,
        "Rating": rating_class
    })


df = pd.DataFrame(data)


df.to_csv("books_output.csv", index=False, encoding="utf-8")

print("Scraping completed. CSV file saved as books_output.csv")
df.to_excel("books_output.xlsx", index=False)
conn=sqlite3.connect("books_pd.db")
df.to_sql("books_table",conn,if_exists="replace",index=False)
conn.close()
print("saved to:books_output.csv,books_output.xlsx,books.db")
print(df.head())


