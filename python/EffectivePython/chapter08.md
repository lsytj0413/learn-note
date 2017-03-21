# 第八章: 部署 #

## 第54条: 考虑用模块级别的代码来配置不同的部署环境 ##

### 介绍 ###

所谓部署环境就是程序在运行的时候所用的一套配置. 如果要在程序运行的时候支持不同的配置, 最佳的方案是在程序启动的时候覆写其中的某些部分, 以便根据部署环境来提供不同的功能.

```
# dev_main.py
TESTING = True
import db_connection
db = db_connection.Databse()

# prod_main.py
TESTING = False
import db_connection
db = db_connection.Databse()

# db_connection.py
import __main__

class TestingDatabase(object):
    pass
    
class RealDatabase(object):
    pass
    
if __main__.TESTING:
    Database = TestingDatabase
else:
    Database = TestingDatabase
```

### 要点 ###

1. 程序通常需要在不同的部署环境之中运行, 而这些环境所需的先决条件及配置信息也都互不相同
2. 我们可以在模块的范围内编写普通的Python语句, 以便根据不同的环境来定制本模块的内容
3. 我们可以根据外部条件来决定模块的内容

## 第55条: 通过repr字符串来输出调试信息 ##

### 介绍 ###

### 要点 ###

## 第56条: 用unittest来测试全部代码 ##

### 介绍 ###

### 要点 ###

## 第57条: 考虑用pdb实现交互调试 ##

### 介绍 ###

### 要点 ###

## 第58条: 先分析性能, 然后再优化 ##

### 介绍 ###

### 要点 ###

## 第59条: 用tracemalloc来掌握内存的使用及泄漏情况 ##

### 介绍 ###

### 要点 ###
