from diaryguider.auth import auth
from diaryguider.extensions import db
from diaryguider.models import User
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user

@auth.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user)