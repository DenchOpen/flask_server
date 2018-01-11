"""
session demo
"""

from flask import Flask, session, request
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


# session操作和字典操作是一样的
@app.route('/')
def hello_world():
    session['username'] = 'zhiliao'
    return 'Hello World!'


@app.route('/get/')
def get_session():
    username = session.get('username')
    return username


if __name__ == '__main__':
    app.run(debug=True)
