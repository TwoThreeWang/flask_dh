# encoding: utf-8
# !/usr/bin/env python
'''
@version ：python 3.7
@File ：run.py
@Author ：WangTwoThree
@Site ：https://wangtwothree.com
@Date ：2022/12/19 22:31 
@Description ：
'''
from gevent.pywsgi import WSGIServer
from main import app
from geventwebsocket.handler import WebSocketHandler
import logging
from logging.handlers import TimedRotatingFileHandler

# 定义日志输出格式
fmt_str = '%(asctime)s [level-%(levelname)s]:%(message)s'
logging.basicConfig(level=logging.INFO)
# when可设置月、日、时、分、秒等; interval: n个when更新一次; backupCount: 保留m个文件
files_handle = TimedRotatingFileHandler('./log/main.log', when='D', interval=1, backupCount=3)  # when S M H D midnight
# 注意时间的格式，区别 - 和 _ , 格式不对影响日志的删除
files_handle.suffix = "%Y-%m-%d_%H-%M-%S.log"
# 设置日志输出级别和格式
# files_handle.setLevel(logging.DEBUG)
formatter = logging.Formatter(fmt_str)
files_handle.setFormatter(formatter)
# 添加到日志处理对象集合
logging.getLogger('').addHandler(files_handle)

http_server = WSGIServer(('0.0.0.0', 4000), app, handler_class=WebSocketHandler)
http_server.serve_forever()
