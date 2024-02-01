from enum import IntEnum
from diaryguider.extensions import db,login_manager
from datetime import datetime, date, time
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    user = db.session.query(User).get(user_id)
    return user

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100), nullable=False)
    diary = db.relationship('Diary_Entry', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.email
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
class Diary_Entry(db.Model):
    __tablename__ = 'diary_entry'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    path_to_content = db.Column(db.String(100)) # store the diary into files
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date, default=date.today, nullable=False)
    time = db.Column(db.Time, default=time(0,0,0,0), nullable=False)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversation.id'))

    def __repr__(self):
        return '<Diary_Entry %r>' % self.title
    
class conversation_user_type(IntEnum):
    AI = 1
    user = 2
    system = 3

class Conversation(db.Model):
    __tablename__ = 'conversation'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.String(1000))
    path_to_content = db.Column(db.String(100))
    diary_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Conversation %r>' % self.content
    
class conversation_message(db.Model):
    __tablename__ = 'conversation_message'
    id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversation.id'), nullable=False)
    content = db.Column(db.String(1000))
    user_type = db.Column(db.Enum(conversation_user_type))
    date = db.Column(db.Date, default=date.today, nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return '<conversation_message %r>' % self.content