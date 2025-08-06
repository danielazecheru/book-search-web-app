from dotenv import load_dotenv
import os

load_dotenv()
nyt_api_key = os.getenv("NYT_API_KEY")

load_dotenv()
openai_api_key= os.getenv("OPENAI_API_KEY")

import requests

from openai import OpenAI # type: ignore

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


book = input("Please enter a book you want to learn more about: ")

client = OpenAI(api_key=openai_api_key)

response = client.responses.create(
    model="gpt-4.1",
    input=f"Without giving any plot spoilers, summarize in no more than 3 sentences the book reviews for {book}"
)

print(response.output_text)