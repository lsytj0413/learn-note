# 第2章: MySQL基准测试 #

## 2.1 为什么需要基准测试 ##

- 验证基于系统的一些假设, 确认这些假设符合实际情况
- 重现某些异常行为
- 测试系统当前运行情况
- 模拟比当前系统更高的负载
- 规划未来的业务增长
- 测试应用适应可变环境的能力
- 测试不同的硬件, 软件和操作系统配置
- 证明新采购的设备是否配置正确

## 2.2 基准测试的策略 ##

主要有两种策略: 针对整个系统的整体测试(集成式)或单独测试 MySQL(单组件式).

如果能够在真实的数据集上执行重复的查询, 那么针对 MySQL 的基准测试也是可以的, 但是此时的数据本身和数据集的大小都应该是真实的.

### 2.2.1 测试何种指标 ###

- 吞吐量: 单位时间内的事务处理数
- 响应时间或者延迟: 测试任务所需的整体时间
- 并发性: 任意时刻有多少同时发生的并发请求, 需要关注正在工作中的并发操作或是同时工作的线程数/连接数
- 可扩展性

## 2.3 基准测试方法 ##

需要避免以下错误:

- 使用真实数据的子集而不是全集
- 使用错误的数据分布
- 使用不真实的分布参数
- 在多用户场景中只做单用户的测试
- 在单服务器上测试分布式应用
- 与真实用户行为不匹配
- 反复执行同一个查询
- 没有检查错误
- 忽略了系统的预热过程
- 使用默认的服务器配置
- 测试时间太短

### 2.3.1 设计和规划基准测试 ###

规划基准测试的第一步是提出问题并明确目标, 然后决定是采用标准的基准测试还是设计专用的测试.

设计专用的测试的过程如下:

1. 获取生产数据的快照
2. 针对数据运行查询

### 2.3.2 基准测试应该运行多长时间 ###

基准测试应该运行足够长的时间, 可以让测试一直运行持续观察直到确认系统已经稳定.

### 2.3.3 获取系统性能和状态 ###

需要尽可能多的手机被测试系统的信息, 包括测试结果, 配置文件, 测试指标, 脚本和其他相关说明都应该保存. 需要记录系统状态和性能指标, 包括 CPU 使用率, 磁盘 I/O, 网络流量统计, SHOW GLOBAL STATUS 计数器等.

如下是一个示例数据收集脚本:

```
#!/bin/sh

INTERVAL=5
PREFIX=$INTERVAL-sec-status
RUNFILE=/home/benchmark/running
mysql -e 'SHOW GLOBAL VARIABLES' >> mysql-variables
while test -e $RUNFILE; do
    file=$(date +%F_%I)
    sleep=$(date +%s.%N | awk "{print $INTERVAL - (\$1 % $INTERVAL)}")
    sleep $sleep
    ts="$(date +"TS %s.%N %F $T")"
    loadavy="$(uptime)"
    echo "$ts $loadavg" >> $PREFIX-${file}-status
    mysql -e 'SHOW GLOBAL STATUS' >> $PREFIX-${file}-status &
    echo "$ts $loadavg" >> $PREFIX-${file}-innodbstatus
    mysql -e 'SHOW ENGINE INNODB STATUS \G' >> $PREFIX-${file}-innodbstatus &
    echo "$ts $loadavg" >> $PREFIX-${file}-processlist
    mysql -e 'SHOW FULL PROCESSLIST \G' >> $PREFIX-${file}-processlist &
    echo $ts
done
echo Exiting because $RUNFILE does not exist.
```

### 2.3.4 获得准确的测试结果 ###

### 2.3.5 运行基准测试并分析结果 ###

### 2.3.6 绘图的重要性 ###

## 2.4 基准测试工具 ##

### 2.4.1 集成式测试工具 ###

- ab
- http_load
- JMeter

### 2.4.2 单组件测试工具 ###

- mysqlslap
- MySQL Benchmark Suite
- Super Smack
- Database Test Suite
- Percona's TPCC-MySQL Tool
- sysbench

## 2.5 基准测试案例 ##

### 2.5.1 http_load ###

### 2.5.2 MySQL 基准测试套件 ###

### 2.5.3 sysbench ###

### 2.5.4 数据库测试套件中的 dbt2 TPC-C 测试 ###

### 2.5.5 Percona 的 TPCC-MySQL 测试工具 ###
