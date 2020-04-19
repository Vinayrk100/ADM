import flask

from promotion import rfm_score
from recommendation import recommend_books
from unique_books import read_book_details
from books_recommendation_for_user import recommend_books_userbased

app = flask.Flask(__name__, template_folder='templates')


# # Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return flask.render_template('index.html')


@app.route('/books', methods=['GET', 'POST'])
def api_books():
    if flask.request.method == "POST":
        name = flask.request.form["name"]
        uid = int(flask.request.form["uid"])
        purchased_books, recommendations_genre, recommendations_author, \
        recommendations_bookpages = recommend_books_userbased(uid)
        segment, promo, colors = rfm_score(name)
    return flask.render_template('booksdetails.html',
                                 segment=segment,
                                 promo=promo.values.tolist(),
                                 colors=colors,
                                 purchased_books=purchased_books.values.tolist(),
                                 recommendations_genre=recommendations_genre.values.tolist(),
                                 recommendations_author=recommendations_author.values.tolist(),
                                 recommendations_bookpages=recommendations_bookpages.values.tolist())


@app.route('/recommendation', methods=['POST'])
def api_reco():
    # first_line = True
    # i_title = flask.request.form["title"]
    # i_author = flask.request.form["author"]
    # i_lg = flask.request.form["lg"]
    # i_genre = flask.request.form["genre"]
    # books_suggestion = recommend_books(i_title, i_author, i_lg, i_genre)
    # return flask.render_template('recommendation.html', books_suggestion=books_suggestion)

    first_line = True
    title = flask.request.form["title"]
    # books_suggestion = recommend_books(i_title, i_author, i_lg, i_genre)
    book_details = read_book_details(title)
    return flask.render_template('recommendation.html', book_details=book_details)


if __name__ == '__main__':
    app.run(debug=True)
