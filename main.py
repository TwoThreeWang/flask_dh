# encoding: utf-8
# !/usr/bin/env python
'''
@version ：python 3.7
@File ：main.py
@Author ：WangTwoThree
@Site ：https://wangtwothree.com
@Date ：2022/11/24 14:18
@Description ：导航
'''
import os, codecs
from flask import Flask, render_template, request, send_from_directory, abort
from sqlmodel.database import db
from sqlmodel.curd import DbCurd
from markdown import Markdown
from views import admin
from utils.cache_util import cache
from utils.get_ip_util import get_rel_ip
from werkzeug.middleware.proxy_fix import ProxyFix
from utils.api_reponse import reponse

app = Flask(__name__)
app.secret_key = 'abcdef'
app.register_blueprint(admin.mod)
# 前端页面代码压缩
app.wsgi_app = ProxyFix(app.wsgi_app)
# 模版文件改动自动重新加载
app.config['TEMPLATES_AUTO_RELOAD'] = True
# 配置数据库链接
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./data.db?check_same_thread=False'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# 注册数据库连接
db.app = app
db.init_app(app)
dc = DbCurd()


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images/'), 'favicon.png',
                               mimetype='image/vnd.microsoft.icon')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error_info=error), 404


@app.route('/')
def index():
    if cache.get('index_all_links'):
        all_class = cache.get('all_class')
        all_links = cache.get('index_all_links')
        new_link = cache.get('new_link')
    else:
        all_class, all_links = dc.db_get_all_links()
        new_link = dc.db_get_url_by_create(12)
        cache.set('all_class', all_class)
        cache.set('index_all_links', all_links)
        cache.set('new_link', new_link)
    return render_template('index.html', all_class=all_class, all_links=all_links, new_link=new_link)


@app.route('/board/<int:cid>/<cname>')
def board(cid, cname):
    if cache.get(f'all_links_{cid}'):
        all_links = cache.get(f'all_links_{cid}')
    else:
        all_links = dc.db_get_links(cid)
        cache.set(f'all_links_{cid}', all_links)
    rank_links = dc.db_get_url_by_random(12)
    return render_template('board.html', cname=cname, all_links=all_links, rank_links=rank_links)


@app.route('/search')
def search():
    keyword = request.args.get("q")
    all_links = {}
    if keyword:
        all_links = dc.db_search_link(keyword)
    rank_links = dc.db_get_url_by_random(12)
    return render_template('search.html', keyword=keyword, all_links=all_links, rank_links=rank_links)


@app.route('/click/link/<int:link_id>/<int:type>')
def click_link(type, link_id):
    ip = get_rel_ip(request)
    c_key = f"{ip}clicklink{link_id}"
    if cache.get(c_key):
        data = '重复操作！'
    else:
        data = 1 if type == 1 else -10
        data = dc.db_click_link(link_id, data)
        cache.set(c_key, 1)
    return reponse(data=data)


def markdown_to_html(name):
    file = f"post/{name}.md"
    with codecs.open(file, mode='r', encoding='utf-8', errors='ignore') as f:
        body = f.read()
        md = Markdown(extensions=['fenced_code', 'meta', 'admonition', 'tables'])
        content = md.convert(body)
        meta = md.Meta if hasattr(md, 'Meta') else {}
        return meta, content


@app.route('/post/<name>')
def post(name):
    try:
        meta, content = markdown_to_html(name)
    except:
        return abort(404)
    return render_template('post.html', meta=meta, content=content)


if __name__ == '__main__':
    # 用来创建table，一般在初始化的时候调用
    # db.create_all()
    app.run(host="127.0.0.1", port=4000, threaded=True, debug=True)
