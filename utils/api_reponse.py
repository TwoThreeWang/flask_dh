# encoding: utf-8
# !/usr/bin/env python
'''
@version ：python 3.7
@File ：api_reponse.py
@Author ：WangTwoThree
@Site ：https://wangtwothree.com
@Date ：2022/12/19 18:35 
@Description ：
'''
from flask import Response
import json


def reponse(code=200, msg="Success", data=[]):
    '''
    返回报文封装
    :param code:
    :param data:
    :param msg:
    :return:
    '''
    return Response(json.dumps({
        'code': code,
        'message': msg,
        'data': data,
    }), mimetype='application/json')
