from diaryguider.auth import auth
from diaryguider.extensions import db
from diaryguider.models import User
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        print('POST')
        if user:
            if check_password_hash(user.password, password):
                print("password correct")
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.auth.profile'))
            else:
                print("password incorrect")
                flash('Incorrect password, try again.', category='error')
        else:
            print("email does not exist")
            flash('Email does not exist.', category='error')
    else:
        print("GET")
        if current_user.is_authenticated:
            print("user is authenticated")
            print(url_for('views.auth.profile'))
            return redirect(url_for('views.auth.profile'))
        
    print("rendering template")
    return render_template("login.html", user=current_user)