from diaryguider import app
from flask import render_template

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return "<p>This is my about page!</p>"