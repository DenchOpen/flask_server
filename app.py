"""
Main 入口
"""
from flask import Flask
from models import db
import models
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()
    print("database create all finish.")


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()
