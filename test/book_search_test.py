import pytest
from app.book_search import fetch_bestselling_list, get_book_reviews
import requests, sys, os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_list_fetch():
    test_list = fetch_bestselling_list("Hardcover Fiction")
    assert "results" in test_list
    assert "books" in test_list["results"]
