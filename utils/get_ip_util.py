# encoding: utf-8
# !/usr/bin/env python
'''
@version ：python 3.7
@File ：get_ip_util.py
@Author ：WangTwoThree
@Site ：https://wangtwothree.com
@Date ：2022/12/19 22:02 
@Description ：
'''


def get_rel_ip(request):
    '''
    获取真实IP
    :param request:
    :return:
    '''
    if request.headers.get("x-forwarded-for", ""):
        ip = request.headers.get("x-forwarded-for", "")
    elif request.headers.get("X-Real-Ip", ""):
        ip = request.headers.get("X-Real-Ip", "")
    else:
        ip = request.remote_addr
    return ip
