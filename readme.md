![图片alt](https://cdn.wangtwothree.com/imgur/IdeN4ZQ.png ''图片title'')

# 一个极简的 Flask 网站导航程序 

# 说明

使用 Flask 创建的极简网站导航程序。

- 不同于千篇一律的网站导航，简洁清爽的界面设计，点击直达无需二次跳转；
- MarkDown 文件生成前台文章
- 后端集成数据缓存，提高页面加载速度
- 链接根据点击量自动排序
- 点击接口防刷量设计

# DEMO

超赞网站导航： [https://one.wangtwothree.com](https://one.wangtwothree.com "https://one.wangtwothree.com")

# 截图

## 前台首页

![图片alt](https://cdn.wangtwothree.com/imgur/IdeN4ZQ.png ''图片title'')

## 前台搜索页

![图片alt](https://cdn.wangtwothree.com/imgur/clddQ3C.png ''图片title'')

## 前台分类页面

![图片alt](https://cdn.wangtwothree.com/imgur/GmVulIg.png ''图片title'')

## 前台文章页面

![图片alt](https://cdn.wangtwothree.com/imgur/hRzbfAl.png ''图片title'')

## 后台登陆页面

![图片alt](https://cdn.wangtwothree.com/imgur/HPQuee3.png ''图片title'')

## 后台管理首页

![图片alt](https://cdn.wangtwothree.com/imgur/XSOPg2q.png ''图片title'')

## 分类管理页面

![图片alt](https://cdn.wangtwothree.com/imgur/D8mznCt.png ''图片title'')

## 链接管理页面

![图片alt](https://cdn.wangtwothree.com/imgur/nx7tOgc.png ''图片title'')

# 使用

1、程序默认使用 SQLite 数据库，数据库文件在`instance/data.db`，数据库配置信息在`main.py`。

2、下载程序后修改`example_config.py`文件中的配置信息，然后将文件重命名为`config.py`。

3、本地调试可直接运行`main.py`，生产环境运行建议使用`run.py`，该文件使用`gevent`启动服务。

4、启动成功后访问 `127.0.0.1:4000`

5、使用`main.py`启动日志在控制台输出；使用`run.py`启动日志默认保存在`log`目录下。