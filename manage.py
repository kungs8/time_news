from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis


class Config(object):
    """项目的配置"""
    DEBUG=True

    # 为数据库 添加配置
    SQLALCHEMY_DATABASE_URI="mysql://root:yanpenggong@127.0.0.1:3306/time_news"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    # Redis 的配置
    REDIS_HOST="127.0.0.1"
    REDIS_PORT=6379

app=Flask(__name__)

# 加载配置
app.config.from_object(Config)

# 初始化数据库
db=SQLAlchemy(app)

# 初始化 redis 存储对象
redis_store=StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_HOST)
# 开启当前项目 CSRF 保护，只做服务器验证功能
CSRFProtect(app)

@app.route('/')
def index():
    return 'index222'

if __name__=='__main__':
    app.run(debug=True)