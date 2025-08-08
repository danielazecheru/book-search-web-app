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

lists =[]

for list in books["results"]["lists"]:
    x = {"list_name": list["list_name"], "list_name_encoded":list["list_name_encoded"]}
    lists.append(x)


def fetch_bestselling_list(genre):
    for list in lists:
        if genre == list["list_name"]:
            genre_encoded =list["list_name_encoded"]
    url = f"https://api.nytimes.com/svc/books/v3/lists/{genre_encoded}.json?api-key={nyt_api_key}"
    r = requests.get(url)
    bestsellers = r.json()
    return bestsellers
    

def get_book_reviews(book_title, book_author):
    client = OpenAI(api_key=openai_api_key)
    response = client.responses.create(
        model="gpt-4.1",
        input=f"Without giving any plot spoilers, summarize in no more than 3 sentences the book reviews for {book_title} by {book_author}. Use a narrative style, no dialogue with the user."
    )
    return(response.output_text)


if __name__ == "__main__":

    genre = input("Please enter a genre you are interested in: ")

    chosen_list=fetch_bestselling_list(genre)

    print("NYT Bestselling list for", genre)
    print( )
    for book in chosen_list["results"]["books"]:
        print(book["rank"], "-", book["title"], "by", book["author"])
        print("Description:", book["description"])
        print("Weeks spent on list:", book["weeks_on_list"])
        print("Buy on Amazon:", book["buy_links"][0]["url"])
        print( )
    
    chosen_book = input("Please enter a book title you are interested in: ")
    chosen_author = input("Please enter a book author you are interested in: ")

    chosen_reviews=get_book_reviews(chosen_book,chosen_author)
    print( )
    print(chosen_reviews)