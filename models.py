# encoding: utf-8

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# 用户表
class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32))

    def __repr__(self):
        return '<User %r>' % self.username


# 创建所有数据库表
def create_database():
    db.create_all()
    print("database is created.")


# 删除所有数据库表
def drop_database():
    db.drop_all()
    print('database is dropped.')
