# encoding: utf-8
# !/usr/bin/env python
'''
@version ：python 3.7
@File ：curd.py
@Author ：WangTwoThree
@Site ：https://wangtwothree.com
@Date ：2022/12/18 16:45 
@Description ：
'''
from sqlmodel.database import db
from sqlmodel.models import Class, Links
from sqlalchemy import and_, func


class DbCurd(object):
    def db_get_class(self):
        # 获取所有分类
        return Class.query.order_by(Class.rank.desc()).all()

    def db_insert_class(self, item):
        # 插入一条分类
        db_class = Class(**item)
        db.session.add(db_class)
        db.session.commit()
        db.session.refresh(db_class)
        return db_class.cid

    def db_delete_class(self, cid):
        # 删除分类
        res1 = Class.query.filter(Class.cid == cid).delete()
        res2 = Links.query.filter(Links.cid == cid).delete()
        db.session.commit()
        return f"成功删除 {res1} 个分类，{res2} 条链接"

    def db_update_class(self, item_data):
        # 修改分类
        cid = item_data['cid']
        del item_data['cid']
        res = Class.query.filter(Class.cid == cid).update(item_data)
        db.session.commit()
        return f"成功修改 {res} 个分类"

    def db_get_url_by_create(self, num):
        # 查询最新加入链接
        return Links.query.order_by(Links.id.desc()).limit(num).all()

    def db_get_links(self, cid):
        # 根据分类ID获取所有链接
        return Links.query.filter(Links.cid == cid).order_by(Links.rank.desc()).all()

    def db_get_links_by_rank(self, cid, num):
        # 获取分类下最热门链接
        return Links.query.filter(Links.cid == cid).order_by(Links.rank.desc()).limit(num).all()

    def db_get_all_links(self):
        # 获取所有链接根据分类转为dict
        all_class = self.db_get_class()
        all_links = {}
        for i in all_class:
            all_links[i.cid] = {
                "cname": i.cname,
                "data": self.db_get_links_by_rank(i.cid, 11)
            }
        return all_class, all_links

    def db_click_link(self, id, data):
        # 评价链接
        res = Links.query.filter(Links.id == id).update({"rank": Links.rank + data}, synchronize_session="evaluate")
        return f"成功操作 {res} 次id：{id}"

    def db_get_url_by_random(self, num):
        # 随机链接
        return Links.query.order_by(func.random()).limit(num).all()

    def db_search_link(self, keyword):
        # 搜索链接
        return Links.query.filter(
            Links.name.like(f'%{keyword}%') | Links.url.like(f'%{keyword}%') | Links.desc.like(f'%{keyword}%')).all()

    def db_insert_link(self, item):
        # 插入一条链接
        db_link = Links(**item)
        db.session.add(db_link)
        db.session.commit()
        db.session.refresh(db_link)
        return db_link.id

    def db_update_link(self, item_data):
        # 修改链接
        res = Links.query.filter(Links.id == item_data['id']).update(item_data)
        db.session.commit()
        return f"成功修改 {res} 个链接"

    def db_delete_link(self, id):
        # 删除链接
        res = Links.query.filter(Links.id == id).delete()
        db.session.commit()
        return f"成功删除 {res} 个链接"
