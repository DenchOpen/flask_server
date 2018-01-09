# encoding: utf-8
__author__ = 'Dench'

from flask import Flask, render_template
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():
    class Person:
        name = 'James'
        age = 20

    p = Person()
    d = {
        'baidu': 'www.baidu.com',
        'google': 'www.google.com'
    }
    context = {
        'username': 'Dench',
        'age': 18,
        'sex': '男',
        'person': p,
        'dict': d
    }
    return render_template('index.html', **context)


@app.route('/ifelse/<islogin>')
def if_else(islogin):
    if islogin == '1':
        user = {
            'username': 'James',
            'age': 22
        }
        return render_template('ifelse.html', user=user)
    else:
        return render_template('ifelse.html')


@app.route('/for')
def for_test():
    user = {
        'username': 'James',
        'age': 22
    }
    for k, v in user.items():
        print(k, v)
    websites = ['baidu.com', 'google.com']

    books = [
        {
            'name': '西游记',
            'author': '吴承恩',
            'price': 200
        },
        {
            'name': '红楼梦',
            'author': '曹雪芹',
            'price': 300
        },
        {
            'name': '水浒传',
            'author': '施耐庵',
            'price': 100
        },
        {
            'name': '三国演义',
            'author': '罗贯中',
            'price': 120
        }
    ]
    return render_template('for.html', user=user, websites=websites, books=books)


if __name__ == '__main__':
    app.run()
