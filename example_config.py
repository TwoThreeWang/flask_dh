# encoding: utf-8
# !/usr/bin/env python
'''
@version ：python 3.7
@File ：example_config.py.py
@Author ：WangTwoThree
@Site ：https://wangtwothree.com
@Date ：2022/12/21 16:49 
@Description ：配置文件示例，正式使用修改为 config.py
'''
# 后台登陆账户
users = {
    "username": "wangtwothree",
    "password": "123456"
}
# token有效期
expires = 60 * 60 * 2
# token密钥
SECRET_KEY = "wangtwothree"
