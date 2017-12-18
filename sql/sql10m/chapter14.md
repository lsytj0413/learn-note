# 第14章: 组合查询 #

## 14.1 组合查询 ##

SQL 允许执行多个查询并将结果作为一个查询结果集返回, 这种组合查询称为并(union)或复合查询. 主要有两种情况需要使用组合查询:

- 在一个查询中从不同的表返回数据结构
- 对一个表执行多个查询, 按一个查询返回数据

## 14.2 创建组合查询 ##

可用 UNION 操作符来组合数条 SQL 查询, 将他们的结果组合成一个结果集.

### 14.2.1 使用UNION ###

```
SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_state IN ('IL', 'IN', 'MI')
UNION
SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_name = 'Fun4All';
```

- SQL 没有限制 UNION 的数目, 但是 DBMS 可能有限制

### 14.2.2 UNION 规则 ###

- 必须由两条或以上的 SELECT 语句组成
- UNION 中的每个查询必须包含相同的列, 表达式或聚集函数, 但是不需要以相同次序列出
- 列数据类型必须兼容

### 14.2.3 包含或取消重复的行 ###

UNION 会从查询结果集中自动去除重复的行, 这是默认的行为. 如果需要所有的行可以使用 UNION ALL.

```
SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_state IN ('IL', 'IN', 'MI')
UNION ALL
SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_name = 'Fun4All';
```

### 14.2.4 对组合查询结果排序 ###

在使用 UNION 组合查询时, 只能使用一条 ORDER BY 字句, 并且它必须位于最后一条 SELECT 语句之后.

```
SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_state IN ('IL', 'IN', 'MI')
UNION
SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_name = 'Fun4All'
ORDER BY cust_name, cust_contact;
```
