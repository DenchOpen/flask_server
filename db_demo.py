__author__ = 'Dench'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class User(db.Model):
    __talbename__ = 'user'
    user_id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


class Artical(db.Model):
    __tablename__ = 'artical'
    artical_id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.TEXT, nullable=False)
    author_id = db.Column(db.INTEGER, db.ForeignKey('user.user_id'))

    author = db.relationship('User', backref=db.backref('articles'))


db.create_all()


@app.route('/add/')
def index():
    # user = User(name='James')
    # db.session.add(user)
    # db.session.commit()

    artical = Artical(title='aaa', content='bbb', author_id=4)
    artical2 = Artical(title='111', content='222', author_id=4)
    db.session.add(artical)
    db.session.add(artical2)
    db.session.commit()

    user2 = User.query.filter(User.name == 'James').first()
    for temp in user2.articles:
        print('--------')
        print(temp.title)

    return "hello world"


def addArtical():
    # add
    artical1 = Artical(title='aaa', content='bbb')
    db.session.add(artical1)
    db.session.commit()


def findArtical():
    articals = Artical.query.filter(Artical.title == 'aaa').all()
    print(articals[0].title)
    artical = Artical.query.filter(Artical.title == 'aaa').first()
    print(artical.title)


def updateArtical():
    artical = Artical.query.filter(Artical.title == 'aaa').first()
    artical.content = 'adkgjsldkj'
    db.session.commit()


def deleteArtical():
    artical = Artical.query.filter(Artical.content == 'bbb').first()
    db.session.delete(artical)
    db.session.commit()


if __name__ == '__main__':
    app.run()
