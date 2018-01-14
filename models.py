# encoding: utf-8

from flask_sqlalchemy import SQLAlchemy

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

    def to_json(self):
        json_user = {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'mobile': self.mobile,
            'password': self.password
        }
        return json_user

        # @staticmethod
        # def from_json(json_user):
        #     user = User(
        #         user_id=json_user.get('user_id'),
        #         user_name=json_user.get('user_name'),
        #         mobile=json_user.get('mobile'),
        #         password=json_user.get('password')
        #     )
        #     return user


# 文章
class Article(db.Model):
    __tablename__ = 'article'
    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # 默认时间直接使用timestamp()函数名
    create_time = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    author = db.relationship('User')

    def to_json(self):
        json_article = {
            'article_id': self.article_id,
            'title': self.title,
            'content': self.content,
            'create_time': self.create_time,
            'author_id': self.author_id,
            'author_name': self.author.user_name,
        }
        return json_article

    def __repr__(self):
        return '<Article %r>' % self.title
