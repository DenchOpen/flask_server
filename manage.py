"""
flask script command tool manage
"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from models import db

manage = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本命令到manager中
manage.add_command('db', MigrateCommand)
