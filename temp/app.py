"""
Main 入口
"""
from flask import Flask, current_app
from models import db
import models
import config

app = Flask(__name__)
app.config.from_object(config)
app.app_context().push()
db.init_app(app)

db.create_all()


# db.create_all(app=app)
# with app.app_context():
#     print(current_app.name)
#     db.create_all()


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()
