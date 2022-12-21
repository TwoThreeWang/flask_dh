# encoding: utf-8
# !/usr/bin/env python
'''
@version ：python 3.7
@File ：models.py
@Author ：WangTwoThree
@Site ：https://wangtwothree.com
@Date ：2022/12/18 16:36 
@Description ：
'''
from sqlmodel.database import db


class Class(db.Model):
    __tablename__ = "w_class"

    cid = db.Column(db.Integer, primary_key=True, index=True)
    cname = db.Column(db.String)
    rank = db.Column(db.Integer, default=0)


class Links(db.Model):
    __tablename__ = "w_links"

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String)
    desc = db.Column(db.String)
    url = db.Column(db.String)
    cid = db.Column(db.Integer, index=True)
    rank = db.Column(db.Integer, default=0)

# with app.app_context():
#     db.create_all()

# with app.app_context():
#     student = Class.query.all()
#     # print(student) #这里student返回的是SQL语句
#     for s in student:
#         print(s)
#         print(s.cid, s.cname, s.rank)
