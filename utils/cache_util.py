# encoding: utf-8
# !/usr/bin/env python
'''
@version ：python 3.7
@File ：cache_util.py
@Author ：WangTwoThree
@Site ：https://wangtwothree.com
@Date ：2022/12/19 21:53 
@Description ：
'''
from cacheout import Cache
import time

cache = Cache(maxsize=256, ttl=60 * 1, timer=time.time, default=None)
