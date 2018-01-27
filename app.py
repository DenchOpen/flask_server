#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main 入口
"""
from flask import Flask, render_template, redirect, url_for, request, session, jsonify
from decorators import login_required
from models import db, User, Article
from datetime import datetime
import config
from sqlalchemy import and_, or_

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

with app.app_context():
    # db.drop_all()
    db.create_all()
    print("database create all finish.")


@app.route('/')
def index():
    questions = Article.query.order_by('-create_time').all()
    # print(questions)
    return render_template('index.html', questions=questions)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        mobile = request.form.get('mobile')
        password = request.form.get('password')
        user = User.query.filter(User.mobile == mobile).filter(User.password == password).first()
        if user:
            session['user_id'] = user.user_id
            # 31天内不需要登录
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return "用户名或密码错误"


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        mobile = request.form.get('mobile')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # 验证手机号
        user = User.query.filter(User.mobile == mobile).first()
        if user:
            return '该手机号已经存在'
        else:
            user = User(mobile=mobile, user_name=username, password=password1)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))


@app.route('/question/', methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        author_id = session.get('user_id')
        question1 = Article(title=title, content=content, author_id=author_id,
                            create_time=datetime.now().timestamp())
        db.session.add(question1)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/detail/<question_id>')
def detail(question_id):
    question_ = Article.query.filter(Article.article_id == question_id).first()
    print(question_)
    return render_template('detail.html', question=question_)


''' -------------------  API ------------------- '''
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Connection': 'keep-alive',
    'Version-Code': 1
}


# 服务成功
def json_success_response(dict_data=None):
    if not dict_data:
        dict_data = {}
    dict_data['status'] = 1
    dict_data['message'] = '成功'

    rst = jsonify(dict_data)
    rst.headers = headers
    return rst


# 服务失败
def json_error_response(status=0, message='服务异常'):
    dict_data = {
        'status': status,
        'message': message
    }
    rst = jsonify(dict_data)
    rst.headers = headers
    return rst


# ------- user api ----------
# 用户注册
@app.route('/user/register.action', methods=['GET', 'POST'])
def user_register_action():
    values = request.json
    if not values:
        values = request.form
    mobile = values.get('mobile')
    username = values.get('username')
    password = values.get('password')
    if not mobile or not username or not password:
        return json_error_response(status=101, message='缺少必要的参数.')
    # 验证手机号是否存在
    user = User.query.filter(User.mobile == mobile).first()
    if user:
        return json_error_response(status=102, message='该手机号已经存在')
    else:
        user = User(mobile=mobile, user_name=username, password=password)
        db.session.add(user)
        db.session.commit()
        return json_success_response()


# 用户登录
@app.route('/user/login.action', methods=['GET', 'POST'])
def user_login_action():
    values = request.json
    if not values:
        values = request.form
    user_name = values.get('username')
    password = values.get('password')
    if (not user_name) or (not password):
        return json_error_response(status=101, message='用户名或密码错误')
    user = User.query.filter(and_(or_(User.user_name == user_name, User.mobile
                                      == user_name), User.password == password)).first()
    if user:
        return json_success_response(user.to_json())

    else:
        return json_error_response(status=102, message='用户名或密码错误')


# ------- article api ----------
# 添加文章
@app.route('/article/add.action', methods=['GET', 'POST'])
def article_add_action():
    values = request.json
    if not values:
        values = request.form
    title = values.get('title')
    content = values.get('content')
    author_id = values.get('author_id')
    if (not title) or (not content) or (not author_id):
        return json_error_response(status=101, message='缺少必要参数')
    user = User.query.filter(User.user_id == author_id).first()
    if not user:
        return json_error_response(status=102, message='用户不存在')
    article = Article(title=title, content=content, author_id=author_id,
                      create_time=datetime.now().timestamp())
    db.session.add(article)
    db.session.commit()
    return json_success_response()


# 文章列表
@app.route('/article/list.action', methods=['GET', 'POST'])
def article_list_action():
    articles = Article.query.all()
    json_articles = {
        'articles': [article.to_json() for article in articles]
    }
    return json_success_response(json_articles)


# 文章详情
@app.route('/article/detail.action', methods=['GET', 'POST'])
def article_detail_action():
    values = request.json
    if not values:
        values = request.form
    article_id = values.get('article_id')
    if not article_id:
        return json_error_response(status=101, message='数据不能为空')
    article = Article.query.filter(Article.article_id == article_id).first()
    if not article:
        return json_error_response(status=102, message='文章消失了')
    else:
        return json_success_response(article.to_json())


# 文章删除
@app.route('/article/delete.action', methods=['GET', 'POST'])
def article_delete_action():
    values = request.json
    if not values:
        values = request.form
    article_id = values.get('article_id')
    if not article_id:
        return json_error_response(status=101, message='数据不能为空')
    Article.query.filter(Article.article_id == article_id).delete()
    db.session.commit()
    return json_success_response()


if __name__ == '__main__':
    app.run()
