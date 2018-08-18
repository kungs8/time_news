from flask import Flask,session
# 数据迁移
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
# 用来指定 session 保存的位置
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis


class Config(object):
    """项目的配置"""
    DEBUG=True

    SECRET_KEY="QOsVz2IUxi6Q0srpc3itP/ParDygHBeVRhuh2++ik1ZlAbWET3t0L/yWGMeVyeLI"

    # 为数据库 添加配置
    SQLALCHEMY_DATABASE_URI="mysql://root:yanpenggong@127.0.0.1:3306/time_news"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    # Redis 的配置
    REDIS_HOST="127.0.0.1"
    REDIS_PORT=6379

    # Session 保存配置
    SESSION_TYPE="redis"
    # 开启 session 签名
    SESSION_USE_SIGNER=True
    # 指定 Session 保存的redis
    SESSION_REDIS=StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT=False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME=86400*2

app=Flask(__name__)

# 加载配置
app.config.from_object(Config)

# 初始化数据库
db=SQLAlchemy(app)

# 初始化 redis 存储对象
redis_store=StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_HOST)
# 开启当前项目 CSRF 保护，只做服务器验证功能
CSRFProtect(app)

# 设置 session 保存指定位置
Session(app)

manager=Manager(app)
# 将app与db关联
Migrate(app,db)
# 将迁移命令添加到manager中
manager.add_command('db',MigrateCommand)

@app.route('/')
def index():
    session['name']="Kungs"
    return 'index222'

if __name__=='__main__':
    manager.run()