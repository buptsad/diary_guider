# This is a minimal example of a Flask application.
from flask import Flask
from flask import url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

if __name__ == "__main__":
    with app.test_request_context():
        print(url_for('hello_world'))
        print(url_for('show_user_profile', username='John Doe'))
        print(url_for('show_post', post_id=1))
        print(url_for('show_subpath', subpath='/path/'))
    app.run()

    