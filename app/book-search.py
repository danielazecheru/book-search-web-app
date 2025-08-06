from dotenv import load_dotenv
import os

load_dotenv()
nyt_api_key = os.getenv("NYT_API_KEY")

import requests

url = f"https://api.nytimes.com/svc/books/v3/lists/overview.json?api-key={nyt_api_key}"
r = requests.get(url)
books = r.json()

genre = input("Please enter a genre you are interested in: ")

for list in books["results"]["lists"]:
    if genre == list["list_name"]:
        genre_encoded = list["list_name_encoded"]

url = f"https://api.nytimes.com/svc/books/v3/lists/{genre_encoded}.json?api-key={nyt_api_key}"
r = requests.get(url)
print(r.status_code)
books = r.json()
print("NYT Bestselling list for", genre)
print( )
for book in books["results"]["books"]:
    print(book["rank"], "-", book["title"], "by", book["author"])
    print("Description:", book["description"])
    print("Weeks spent on list:", book["weeks_on_list"])
    print("Buy on Amazon:", book["buy_links"][0]["url"])
    print( )