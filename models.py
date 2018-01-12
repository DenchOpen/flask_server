# encoding: utf-8

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# 用户表
class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    mobile = db.Column(db.String(11), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user_name


# 问答
class Question(db.Model):
    __tablename__ = 'question'
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # 默认时间直接使用timestamp()函数名
    create_time = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    author = db.relationship('User')

    def __repr__(self):
        return '<Question %r>' % self.title
