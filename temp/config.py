"""
配置信息
"""

# Debug mode
DEBUG = True

# SQLAlchemy config
# dialect+driver://username:password@host:port/database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dench:123456@localhost:3306/zhifoudb?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = True
