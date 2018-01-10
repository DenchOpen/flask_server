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


@app.route('/filter')
def image_filter():
    img_url = 'http://avatar.csdn.net/1/5/0/3_kwu_ganymede.jpg'
    comments = [
        {
            'user': '韩梅梅',
            'content': '我是评论内容',
        },
        {
            'user': '李磊',
            'content': '我是评论内容',
        }
    ]
    return render_template('filter.html', img_url=img_url, comments=comments)


#
# class Person(object):
#     name = ''
#     age = 18
#
#
# class Student(Person):
#     def get_person(self):
#         return self


@app.route('/page2')
def extends_template2():
    return render_template('page2.html')


@app.route('/page1')
def extends_template1():
    return render_template('page1.html')


if __name__ == '__main__':
    app.run()
