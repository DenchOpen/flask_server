"""
装饰器
"""
from flask import g, redirect, url_for, session
from functools import wraps
from models import User


# 登录权限限制装饰器
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = session.get('user_id')
        print("user_id in session:", user_id)
        if user_id is not None:
            if g.get('user') is None or g.get('user').user_id != user_id:
                g.user = User.query.filter(User.user_id == user_id).first()
        else:
            if g.get('user'):  # 需要清除session
                g.pop('user')

        if g.get('user'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrapper
