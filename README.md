# book-search-web-app 

## Create a virtual environment 

``
conda create -n book-search-web-app python=3.11
``

## Activate virtual environment

``
conda activate book-search-web-app
``

## Install all required packages 

``
pip install -r requirements.txt
``

## Run the book_search.py file from the local command line

``
python -m app.book_search
``

## Run app in the local server from the command line using FLASK 

``
FLASK_APP=web-app flask run
``

## Visit on local server at: http://127.0.0.1:5000

## Testing 

``
pytest
``