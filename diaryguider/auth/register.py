from diaryguider.auth import auth
from diaryguider.extensions import db
from diaryguider.models import User
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import re

def check_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    else:
        return False

@auth.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print("POST")
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user_exists = User.query.filter_by(email=email).first()
        
        if user_exists:
            print("user exists")
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            print("email too short")
            flash('Email must be greater than 3 characters.', category='error')
        elif not check_email(email):
            print("email invalid")
            flash('Email is invalid.', category='error')
        elif len(username) < 2:
            print("username too short")
            flash('Username must be greater than 1 character.', category='error')
        elif password1 != password2:
            print("passwords don't match")
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            print("password too short")
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.auth.profile'))
    else:
        print("GET")
    print("rendering template")
    return render_template("register.html", user=current_user)