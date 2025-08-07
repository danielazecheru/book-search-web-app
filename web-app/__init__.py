from flask import Flask, render_template, request

from app.book_search import fetch_bestselling_list , get_book_reviews

app = Flask(__name__)

# route for home page
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/results', methods=['POST'])
def results():

    user_choice = request.form.get('genre')

    print(request.form)

    bestselling_list = fetch_bestselling_list(user_choice)

    display_list = []
    for book in bestselling_list["results"]["books"]:
        title = book["title"]
        rank = book["rank"]
        author = book["author"]
        description = book["description"]
        weeks = book["weeks_on_list"]
        amazon = book["buy_links"][0]["url"]
        #display_list.append(f"{rank}. {title} by {author} - Description: {description} - Weeks spent on list: {weeks_on_list}")
        display_list.append({"title":title, "rank": rank, "weeks": weeks, "author": author, "description": description, "amazon": amazon})
   
    return render_template("results.html",
        user_choice=user_choice,
        display_list = display_list
    )

@app.route('/reviews')
def reviews():
    return render_template("reviews.html")

@app.route('/results2', methods=['POST'])
def results2():

    book_choice = request.form.get('book_title')
    author_choice = request.form.get('book_author')

    print(request.form)

    return render_template("results2.html",
        user_choice1=book_choice,
        user_choice2=author_choice, 
        book_reviews=get_book_reviews(book_choice, author_choice) 
    )

if __name__ == '__main__':

    app.run(debug=True)