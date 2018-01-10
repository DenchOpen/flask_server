# encoding: utf-8

# Debug mode
DEBUG = True

# mysql config
# dialect+driver://username:password@host:port/database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dench:123456@localhost:3306/zhifoudb?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = True
