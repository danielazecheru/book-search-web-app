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

## Run the book-search.py file from the local command line

``
python app/book-search.py
``

## Run app in the local server from the command line using FLASK 

``
FLASK_APP=web-app flask run
``

## Testing using command line

``
pytest
``