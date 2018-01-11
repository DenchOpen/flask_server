"""
get & post
"""

from flask import Flask, render_template, request, session, redirect, url_for, g
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def index():
    return render_template('welcome.html')


@app.route('/search/')
def search():
    # arguments
    q = request.args.get('q')
    a = request.args.get('a')
    return 'q=' + q + '; a=' + a


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if password == '111111':
            session['username'] = username
            return 'success'
        else:
            session.clear()
            return 'username or password error.'


@app.route('/edit/')
def edit_user():
    if g.get('user'):
        return 'hello ' + g.user
    else:
        return redirect(url_for('login'))


@app.before_request
def bf_request():
    username = session.get('username')
    print("username:", username)
    if username is not None:
        if g.get('user') or g.get('user') != username:
            g.user = username
    else:
        if g.get('user'):
            g.pop('user')


if __name__ == '__main__':
    app.run(debug=True)
