from diaryguider.auth import auth
from diaryguider.extensions import db
from diaryguider.models import User
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.auth.login'))