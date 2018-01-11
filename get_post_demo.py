"""
get & post
"""

from flask import Flask, render_template, request

app = Flask(__name__)


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
        return 'login'
    else:
        return 'post request'


if __name__ == '__main__':
    app.run(debug=True)
