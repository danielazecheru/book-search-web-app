from flask import Flask, render_template, request

from app.book_search import fetch_bestselling_list 

app = Flask(__name__)

# route for home page
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/results', methods=['POST'])
def results():

    user_choice = request.form.get('genre')

    print(request.form)

    return render_template("results.html",
        user_choice=user_choice,
        bestselling_list = fetch_bestselling_list(user_choice)
    )


if __name__ == '__main__':

    app.run(debug=True)