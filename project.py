from cs50 import SQL
from flask import Flask, render_template, request, redirect, url_for
import os
import random
import json

app = Flask(__name__)

# Configure CS50 Library to use SQLite database
sql_url = "postgres://u71tjn7urbb255:pf8cbeacf614de01f5f9c1f3a6e4b04eca424c680723cec5bd98b689664376179@c5p86clmevrg5s.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dt7786muekh2d"
db_url = os.getenv("DATABASE_URL").replace("postgres://", "postgresql://", 1)
db = SQL(db_url)

def reshape_and_reshuffle(query_result):
    reshuffled_data = []

    for item in query_result:
        reshuffled_data.append({"id": item["id"], "lang": item["english"]})
        reshuffled_data.append({"id": item["id"], "lang": item["dutch"]})

    random.shuffle(reshuffled_data)
    return reshuffled_data

@app.route("/")
def index():
    """Select library, redirect user to match page"""
    if request.method == "GET":
        libraries = db.execute("SELECT DISTINCT library FROM words;")
        return render_template("index.html",libraries=libraries)

@app.route("/game")
def game():
    """Make a page with word pairs"""
    library = request.args.get('library', 'animals')

    if request.method == "GET":
        words = db.execute("SELECT * FROM words WHERE library = ?;",library)
        words_reshuffled = reshape_and_reshuffle(words)
        wordsamount = len(words)
        return render_template("game.html",words_reshuffled=words_reshuffled ,wordsamount=wordsamount)

@app.route("/api/words")
def words():
    """Get words from library"""
    if request.method == "GET":
        return db.execute("SELECT * FROM words;")


if __name__ == "__main__":
    app.run(debug=True)