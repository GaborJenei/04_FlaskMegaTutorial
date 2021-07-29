from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # This is not an actual database field, but a high-level view of the relationship between users and posts
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))

    # note that I did not include the () after utcnow,
    # so I'm passing the function itself, and not the result of calling it
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    # db.ForeignKey() declaration, a model is given by its database table name,
    # for which SQLAlchemy automatically uses lowercase characters
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
