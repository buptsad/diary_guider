from flask import Flask
from flask import url_for

''' old version
app = Flask(__name__)

import diaryguider.views

if __name__ == "__main__":
    app.run()
'''

def create_app():
    app = Flask(__name__)
    app.config.from_object('diaryguider.config')
    
    from diaryguider.extensions import db
    db.init_app(app)
    
    from diaryguider.extensions import migrate
    migrate.init_app(app, db)
    
    from diaryguider.extensions import login_manager
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from diaryguider.views import views
    app.register_blueprint(views)

    return app
