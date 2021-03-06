"""
配置信息
"""
import os

# Debug mode
DEBUG = True

# SQLAlchemy config
# dialect+driver://username:password@host:port/database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dench:123456@localhost:3306/zhifoudb?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Session key (length 24)
SECRET_KEY = os.urandom(24)
