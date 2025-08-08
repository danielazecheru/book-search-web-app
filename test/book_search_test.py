import pytest
from app.book_search import fetch_bestselling_list, get_book_reviews
import requests, sys, os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_list_fetch():
    test_list = fetch_bestselling_list("Hardcover Fiction")
    assert "results" in test_list
    assert "books" in test_list["results"]
    assert "title" in test_list["results"]["books"][0]
    assert "author" in test_list["results"]["books"][0]
    assert "rank" in test_list["results"]["books"][0]
    assert "description" in test_list["results"]["books"][0]
    assert "book_image" in test_list["results"]["books"][0]
    test_list = fetch_bestselling_list("Audio Fiction")
    assert "results" in test_list
    assert "books" in test_list["results"]
    assert "title" in test_list["results"]["books"][0]
    assert "author" in test_list["results"]["books"][0]
    assert "rank" in test_list["results"]["books"][0]
    assert "description" in test_list["results"]["books"][0]
    assert "book_image" in test_list["results"]["books"][0]

def test_reviews():
    test_reviews = get_book_reviews("Frankenstein", "Mary Shelley")
    assert isinstance(test_reviews, str)
    test_reviews = get_book_reviews("", "Emily Henry")
    assert isinstance(test_reviews, str)
    test_reviews = get_book_reviews("Les Miserables", "")
    assert isinstance(test_reviews, str)