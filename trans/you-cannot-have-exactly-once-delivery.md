# 为什么正好一次(Exactly-Once)传递是不可能的? #

我经常感到惊讶的是, 人们对于分布式系统的行为有着根本性的误解. 我自己也有许多这样的错误观念, 因此我尽量不要贬低或者排斥, 而是去教育和启发, 希望能听到更少的这样的话. 我持续的从别人那里学习, 回想起来, 人们接受这些谬论并不奇怪, 但是去试图传达某些设计决定和限制时是令人沮丧的.

在分布式系统环境中, 你不能依靠 exactly-once 的消息传递. 无论是 Web 浏览器和服务器之间, 还是服务器和数据库之间, 或者是服务器和消息队列之间, 它们都是分布式的. 在任何的这些情况下, 你都不能依靠 exactly-once 传递语义.

在我过去的[文章](https://www.slideshare.net/TylerTreat/from-mainframe-to-microservice-an-introduction-to-distributed-systems-41004778/23)中我说过分布式系统主要的是关于 trade-off. 有三种关于消息传递的语义: 最多一次(at-most-once), 最少一次(at-least-once)和正好一次(exactly-once). 前两种语义是被广泛使用的. 你可能会说 at-least-once 也是不可能的, 因为从技术上将, 网络分区是不限制时间的. 如果你需要连接到的服务器的网络无限期中断, 那么你就无法传递任何内容. 但是从实际的角度上来说, 我们认为 at-least-once 是可能的(无限期的情况下你应该采取另外的解决办法, 比如致电 ISP), 在这种情况下, 网络分区是有时限的, 虽然这个时限是任意的.

所以我们需要在哪里 trade-off? 为什么 exactly-once 是不可能的? 这个答案就在拜占庭将军问题. 这是我[研究的问题](https://bravenewgeek.com/understanding-consensus/), 而且我们必须要考虑 [FLP结果](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf). 基本上来说, 考虑到可能存在错误的过程, 一个系统不可能就一个决定达成一致.

举个例子: 在我寄给你的信中, 我要求你一收到就给我打电话. 你永远不会打电话给我, 因为要么你不在乎我的信, 或者我的信迷失了方向. 或者我可以发送 10 封信, 并假设你至少能得到其中一封信. 这里的 trade-off 是非常明确的, 但发 10 封信并不能提供额外的任何保证. 在分布式系统中, 我们尝试通过等待接收到消息来确保消息准确传递到, 但是各种类型的事情都可能出错. 消息被删除了? Ack确认消息被丢弃了吗? 接收者是否崩溃? 或者他们只是变慢了吗? 还是网络变慢了? 这些都是无法确定的. 拜占庭将军问题不是设计的复杂性, 他们是不可能的结果.

人们经常扭曲“传递”这个词的含义, 以使自己的系统符合 exactly-once 的语义, 在其他情况下这个词也被赋予了完全不同的含义. 状态机复制就是一个很好的例子, 原子广播协议确保消息按顺序可靠的传递, 然而事实是我们我们不能可靠的传递消息, 在网络分区中, 如果没有高度协调就会遭遇崩溃. 当然, 这种协调需要付出延迟和可用性为代价, 同时依赖与 at-least-once 语义. [Zab](http://www.tcs.hut.fi/Studies/T-79.5001/reports/2012-deSouzaMedeiros.pdf) 是为 ZooKeeper 奠定了基础的原子广播协议, 实施幂等操作.

状态变化是幂等的, 并且多次应用相同的状态变化不会导致不一致. 只要申请顺序与传递顺序一致即可. 因此, 保证 at-least-once 语义是足够的, 并且可以简化实现.

简化实现是作者的微妙尝试. 状态机就是这样的, 如果复制的状态是有副作用的, 那么就会出问题了.

看看 at-most-once 传递: 当消息传递时, 它在接收者处理它之前立即被确认. 发送者终会收到 Ack 确认. 但是如果接收者在处理这个消息之前或期间崩溃了, 则该数据就会永远丢失. 这就是 at-most-once 传递的世界观. 根据具体情况, 实现 at-most-once 的语义比这里描述的更复杂, 如果多个程序或队列被复制, 代理必须要保证强一致性(CAP 定理中的 CP), 以确保一旦被确认的任务不会被传递给任何其他工作程序. Apache Kafka 使用 ZooKeeper 来处理这种协调.

另一方面, 我们可以在消息被处理后确认消息. 如果这个处理在接受消息之后但在确认之前崩溃(或者确认没有被递送), 则发送者将重新传送. 此外, 如果你想以传递到多个站点, 你需要一个会带来巨大的吞吐量的原子广播. 快速或一致性, 你就慢慢权衡吧, 欢迎来到分布式系统的世界.

所有的主流消息队列中间件都保证 at-least-once 传递. 如果有一个消息队列中间件[申明支持 exactly-once 传递](http://datasys.cs.iit.edu/publications/2014_SCRAMBL14_HDMQ.pdf), 那他们就在撒谎, 希望你不会购买他们自己都不明白的分布式系统. 无论如何, 这不是一个好的指标.

RabbitMQ 尝试提供如下的[保证](https://www.rabbitmq.com/reliability.html):

当使用确认时, 从信道或连接失败中恢复的生产者应该重新发送没有从代理收到确认的消息. 在这里有消息重复的可能性, 因为代理可能已经发送了一个从未到达生产者的确认(由于网络故障等). 因此消费者应用程序将需要执行重复数据删除或以幂等方式处理传入的消息.

我们在实践中实现 exactly-once 传递的方式是模拟它. 消息本身应该是幂等的, 这意味着它们可以被多次应用而没有不利影响, 或者我们通过重复数据删除来消除对幂等性的需求. 理想情况下, 我们的消息不需要严格的排序, 而是交换就可以. 无论你采取什么路线都有设计意义和权衡, 但这是我们必须生活的现实.

考虑将操作作为幂等行为说说很容易, 但是做起来很难, 大多数需要改变我们对状态的思考方式. 这最好通过重温复制状态机来描述. 相对于发布操作到各个节点并应用执行它们, 如果我们只是分布状态改变它们自己本身呢? 而不是将状态发布到各个节点. 这样我们只是及时报告各个点的发生事实. 这是Zab工作原理.

想象一下, 我们想告诉朋友来接我们. 我们向他发送一系列带有转弯路线的简讯, 但其中一则讯息会传送两次! 我们的朋友会不太高兴, 因为他发现自己在城市里兜圈了. 相反, 我们只是告诉他我们在哪里, 让他看着办吧. 如果消息被传递多次也没关系.

幂等操作的意义是非常深远的, 因为我们仍然在关注消息的顺序. 这就是为什么像交换commutative和收敛convergent复制的数据类型的解决方案正在变得越来越受欢迎. 也就是说, 我们可以通过外在手段如sequencing传统顺序, 向量时钟或其他部分排序机制等方式解决这个问题. 它通常是因果顺序, 虽然不是立即实时, 但是反正以后一直都是这样. 那些否定因果顺序的人实际不明白在分布式系统[没有现在](https://queue.acm.org/detail.cfm?id=2745385)这个精确概念或这个时间点, (需要各个服务器精确对表, 也就是校对时钟).

重申一下, 没有 exactly-once 传递这样的东西. 我们必须在两种罪恶之中进行选择, 在大多数情况下选择 at-least-once 传递. 可以通过确保幂等性或以其他方式消除操作的副作用来模拟一次性语义. 同样, 重要的是了解设计分布式系统时所涉及的权衡. 异步比比皆是, 这意味着你不能指望同步机制来保证行为. 针对这种异步自然属性为故障恢复和弹性进行设计.

# 资料 #

- 原文: [You Cannot Have Exactly-Once Delivery](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/)