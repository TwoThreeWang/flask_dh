# encoding: utf-8
# !/usr/bin/env python
'''
@version ：python 3.7
@File ：admin.py
@Author ：WangTwoThree
@Site ：https://wangtwothree.com
@Date ：2022/12/19 15:40 
@Description ：
'''
import functools, jwt
from flask import Blueprint, render_template, request, flash, redirect, url_for
from datetime import datetime, timedelta
from sqlmodel.curd import DbCurd
from utils.api_reponse import reponse
from config import users, expires, SECRET_KEY

mod = Blueprint('admin', __name__, url_prefix='/admin')
ALGORITHM = "HS256"
dc = DbCurd()


def auth_load(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        token = request.cookies.get('token')
        if token:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username, expire = payload.get("sub"), payload.get("exp")
            if username == users['username']:
                return func(*args, **kwargs)
        else:
            flash('请先登陆！')
            return redirect(url_for('admin.admin_login'))

    return inner


def create_token(username):
    expire = datetime.now() + timedelta(seconds=expires)
    return jwt.encode(
        {"sub": username, "exp": expire},
        key=SECRET_KEY,
        algorithm=ALGORITHM
    )


@mod.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            flash('Invalid input.')
            return redirect(url_for('admin.admin_login'))
        # 验证用户名和密码是否一致
        if username == users['username'] and password == users['password']:
            token = create_token(username)
            flash('登陆成功')
            resp = redirect(url_for('admin.admin_index'))
            resp.set_cookie('token', token, expires)
            return resp  # 重定向到主页
        flash('Invalid username or password.')  # 如果验证失败，显示错误消息
        return redirect(url_for('admin.admin_login'))  # 重定向回登录页面
    return render_template('admin/login.html')


@mod.route('/index')
@auth_load
def admin_index():
    return render_template('admin/index.html')


@mod.route('/class')
@auth_load
def admin_class():
    all_class = dc.db_get_class()
    return render_template('admin/class.html', all_class=all_class)


@mod.route('/add/class', methods=['GET', 'POST'])
@auth_load
def admin_add_class():
    data = request.json
    cid = dc.db_insert_class(data)
    return reponse(data=f"数据插入cid为：{cid}")


@mod.route('/del/class/<int:cid>')
@auth_load
def admin_del_class(cid):
    data = dc.db_delete_class(cid)
    return reponse(data=data)


@mod.route('/update/class', methods=['GET', 'POST'])
@auth_load
def admin_update_class():
    data = request.json
    msg = dc.db_update_class(data)
    return reponse(data=msg)


@mod.route('/links', defaults={'cid': 38})
@mod.route('/links/<int:cid>')
@auth_load
def admin_link(cid):
    keyword = request.args.get("q")
    all_class = dc.db_get_class()
    if keyword:
        all_links = dc.db_search_link(keyword)
    else:
        all_links = dc.db_get_links(cid)
    return render_template('admin/link.html', all_class=all_class, cid=cid, all_links=all_links)


@mod.route('/add/link', methods=['GET', 'POST'])
@auth_load
def admin_add_link():
    data = request.json
    id = dc.db_insert_link(data)
    return reponse(data=f"数据插入id为：{id}")


@mod.route('/del/link/<int:id>')
@auth_load
def admin_del_link(id):
    data = dc.db_delete_link(id)
    return reponse(data=data)


@mod.route('/update/link', methods=['GET', 'POST'])
@auth_load
def admin_update_link():
    data = request.json
    msg = dc.db_update_link(data)
    return reponse(data=msg)
