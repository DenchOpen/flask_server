# encoding: utf-8

__author__ = 'Dench'

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


@app.route('/')
def index():
    print("finish")
    return "hello world"


def create_database():
    import models
    models.create_database()


def drop_database():
    import models
    models.drop_database()


if __name__ == '__main__':
    create_database()
    app.run()
