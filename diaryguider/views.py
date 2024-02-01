from flask import render_template,Blueprint

from diaryguider.auth import auth

views = Blueprint('views', __name__)

views.register_blueprint(auth)

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/about")
def about():
    return render_template("about.html")