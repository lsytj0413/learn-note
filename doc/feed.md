# feed流 #

## 简介 ##

Feed流是一种信息出口, 信息以持续的方式进行更新. 例如在知乎的首页, 可以源源不断的获取到信息, 既是一种典型的基于推荐算法的 feed 流.

1. 你的朋友产生一个一条新鲜事, 比如发布一个想法, 赞了一个主页等
2. 经过这个朋友的介绍, 到了你的首页, 你一刷新就能看见
3. 总体来说, 新的比旧的容易看见
4. 当新鲜事很多时, 需要考虑排序

## 模式 ##

### 举例 ###

先举一个例子, 假设在知乎中, 你回答了一个问题, 然后你的关注者就会在一定时间内收到你的回答信息.

### 推模式(push) ###

当用户回答了一个问题, 然后系统将这个信息推送到所有的粉丝的 feed 表中. 每个粉丝获取数据时从自己的 feed 表中读取.

Pinterest 采用推模式, HBase 存储(发表pool, 以及评分排序 pool 分开).

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

另一种:

```
Action {
    ActorId: {UserId},
    Conducted: time,
    IsHidden: bool,
    Scope: {Team},
    FanOut: {Pending | InProgress | Done}
}

NewsfeedItem {
    UserId: 0,
    ActionId: 0,
    Relevancy: time
}
```

## 组织数据 ##

feed 数据一般会经过以下几个步骤然后再成为显示给用户的形态:

1. 聚合 (Choosing Connections, Making Activity Sets, Classfication, Scoring, Pruning)
2. 去重
3. 排序 (需要从时间线, 到利用算法重新排序, 按照用户兴趣的相关程度展示 Feed)

## 难点 ##

### Data model ###

存储 feed 的数据模式, 需要针对读写进行优化.

Data 包含两个部分: user(用户ID, 名称等) 和 feed(feedID, type, content, metadata 等).

activity := [:owner, (subject, verb, object)]

activity := [Time, Actor, Verb, Object, Target(最终目标), Title, Summary], 例如用户A保存了电影B到清单C, B是 Object, C 是 Target.

例如: 2016年5月6日23:51:01（Time）@刑无刀（Actor）分享了（Verb） 一条微博（Object）给 @ResysChina（Target）。Title就是前面这句话去掉括号后的内容，Summary暂略。 

连接: [From, to, type/name(连接的类型), affinity]

### Ranking ###

排序.

Facebook 的排序(Edge Rank, 现在是机器学习): 亲密度(交互频率以及时间), 动作度(边权重, 例如点赞和发布内容重要程度不同), 时间(新鲜度).

### publish ###

发布.

一种方案:

- 对于活跃度高的用户: 使用推模式(中小型应用上即可使用, 集中存储所有动态的数据库, 为每个用户保存排序后的 feed(如 Redis), 异步从集中存储上写入每个用户的队列)
- 对于活跃度低的用户: 使用拉模式
- 对于热门的内容生产者: 缓存其最新的N条内容, 并使用拉取方式

另一种:

- 亲密度高: 优先推送
- 亲密度低: 不推送或延迟推送

# 参考资料 #

1. [feed流简介及系统架构](http://www.lmyw.net.cn/?p=619)
2. [Design News Feed System](http://blog.gainlo.co/index.php/2016/03/29/design-news-feed-system-part-1-system-design-interview-questions/)
3. [了解Pinterest Feed算法与架构设计](http://www.iteye.com/news/31169)
4. [Etsy Activity Feeds Architecture](https://www.slideshare.net/danmckinley/etsy-activity-feeds-architecture)
5. [MongoDB Newsfeed Schema Design for Entexis](http://www.waistcode.net/blog/mongodb-newsfeed-schema-design-for-entexis)
6. [兴趣Feed技术架构与实现](http://www.iteye.com/news/31943)
7. [微博和知乎中的 feed 流是如何实现的？](https://www.zhihu.com/question/19645686)
