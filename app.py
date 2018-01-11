"""
Main 入口
"""
from flask import Flask, render_template, redirect, url_for, request, session
from models import db
from models import User
import models
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

with app.app_context():
    # db.drop_all()
    db.create_all()
    print("database create all finish.")


@app.route('/')
def index():
    print('index refresh')
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        mobile = request.form.get('mobile')
        password = request.form.get('password')
        user = User.query.filter(User.mobile == mobile and User.password == password).first()
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


if __name__ == '__main__':
    app.run()
