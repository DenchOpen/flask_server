# encoding: utf-8
from flask import Flask, url_for, redirect

import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    # print(url_for("article_list"))
    # print(url_for('article', id='abc', user='lucy'))
    # return redirect('/list')
    # return redirect(url_for('login'))
    return 'Hello First app. debug mode.'


@app.route('/login')
def login():
    return 'Login'


@app.route('/article/<id>/<user>')
def article(id, user):
    if user == '0':
        return redirect(url_for('login'))
    else:
        return '您请求的参数是：' + id + ' 用户名：' + user


@app.route('/list')
def article_list():
    return 'list'


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
