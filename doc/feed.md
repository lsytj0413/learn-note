# feed流 #

## 简介 ##

Feed流是一种信息出口, 信息以持续的方式进行更新. 例如在知乎的首页, 可以源源不断的获取到信息, 既是一种典型的基于推荐算法的 feed 流.

## 模式 ##

### 举例 ###

先举一个例子, 假设在知乎中, 你回答了一个问题, 然后你的关注者就会在一定时间内收到你的回答信息.

### 推模式(push) ###

当用户回答了一个问题, 然后系统将这个信息推送到所有的粉丝的 feed 表中. 每个粉丝获取数据时从自己的 feed 表中读取.

### 拉模式(pull) ###

当用户回答了一个问题, 然后系统将这个信息推送到一个统一的 feed 表中. 每个粉丝获取数据时都从 feed 表中读取, 这时会进行一些过滤.

### 时间区分拉模式 ###

相对于拉模式, 主要改进在 feed 存储上, 将 feed 按照时间进行分区存储. 例如将最近的数据存储到缓存中.

## 格式 ##

### 如何表示 feed ###

feed 格式需要形成某种规范. 例如在 facebook 中将 feed 定义为一种 template:

```
# template
"{*actor*}在{*credit*}"

# feed 中包含字段数据
"{"credit": "80"}"
```

## 组织数据 ##

feed 数据一般会经过以下几个步骤然后再成为显示给用户的形态:

1. 聚合
2. 去重
3. 排序

## 参考资料 ##

1. [feed流简介及系统架构](http://www.lmyw.net.cn/?p=619)
2. [Design News Feed System](http://blog.gainlo.co/index.php/2016/03/29/design-news-feed-system-part-1-system-design-interview-questions/)
3. [了解Pinterest Feed算法与架构设计](http://www.iteye.com/news/31169)
4. [Etsy Activity Feeds Architecture](https://www.slideshare.net/danmckinley/etsy-activity-feeds-architecture)
5. [MongoDB Newsfeed Schema Design for Entexis](http://www.waistcode.net/blog/mongodb-newsfeed-schema-design-for-entexis)
6. [兴趣Feed技术架构与实现](http://www.iteye.com/news/31943)
7. [微博和知乎中的 feed 流是如何实现的？](https://www.zhihu.com/question/19645686)
