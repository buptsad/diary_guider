from flask import Flask
from flask import url_for

app = Flask(__name__)

import diaryguider.views

if __name__ == "__main__":
    app.run()