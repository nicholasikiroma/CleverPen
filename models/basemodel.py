"""Constructs database for blog"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime


db = SQLAlchemy()




class Users(db.Model, UserMixin):
    __tablename__ = 'accounts'
    id=db.Column(db.Integer(), primary_key=True)
    username=db.Column(db.String(255), unique=True, nullable=False)
    email=db.Column(db.String(255), unique=True, nullable=False)
    password_hash=db.Column(db.Text(),nullable=False)
    posts = db.relationship('Posts', backref='author', lazy='dynamic')


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    date = db.Column(db.DateTime(timezone=True), index=True, default=datetime.utcnow())
    summary = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))

    def __repr__(self) -> str:
        return 'Post Title: {}\nID: {}'.format(self.title, self.id)

    def __repr__(self) -> str:
        return 'User: {}'.format(self.username)
