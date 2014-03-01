TweetsWall
==========

### Noted:

1. 实际效果请访问: http://162.243.87.156:8888/tweets
2. 代码已经放在[Github](https://github.com/liamchzh/tweetwall)

### 使用的开源项目

1. Python框架：[Tornado](http://www.tornadoweb.org/en/stable/)
2. Twitter SDK：[Python Twitter Tools](https://github.com/sixohsix/twitter)
3. [Bootstrap](http://getbootstrap.com/)

### 设计
1. 在Twitter Developers申请新建一个应用，获得API key, API secret, Access token, Access token secret.
2. 调用官方API得到数据然后显示。

### 需要改进
1. 在前端使用JS定时拉取数据然后更新, 已经预留接口：`/search/`。
2. 部分话题的搜索结果没有完全显示。
3. 显示对话的上下文及回复。
4. 加上超链接。
