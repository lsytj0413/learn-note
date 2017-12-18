# 第9章: 汇总数据 #

## 9.1 聚集函数 ##

常用的聚集函数如下表:

| 函数 | 说明 |
|:--|:--|
| AVG | 返回某列的平均值 |
| COUNT | 返回某列的行数 |
| MAX | 返回某列的最大值 |
| MIN | 返回某列的最小值 |
| SUM | 返回某列值之和 |

### 9.1.1 AVG 函数 ###

AVG 通过对表中行数进行计数并计算其列值之和求得该列的平均值.

```
SELECT AVG(prod_price) AS avg_price
FROM Products
WHERE vend_id = 'DLL01';
```

- AVG 只能用来计算数值列的平均值, 列名必须作为参数给出
- 忽略 NULL 行

### 9.1.2 COUNT 函数 ###

COUNT 函数可以确定表中行的数目或符合特定条件的行的数目. 有以下两种使用方式:

- 使用 COUNT(*) 统计行的数目, 包含 NULL 值
- 使用 COUNT(column) 对特定列进行计数, 忽略 NULL 值

```
SELECT COUNT(cust_email) AS num_cust FROM Customers;
```

### 9.1.3 MAX 函数 ###

MAX 返回指定列中的最大值:

```
SELECT MAX(prod_price) AS max_price FROM Products;
```

- 在某些 DBMS 中可用于文本列, 此时返回排序后的最后一行
- 忽略 NULL 值

### 9.1.4 MIN 函数 ###

MIN 返回指定列中的最小值:

```
SELECT MIN(prod_price) AS min_price FROM Products;
```

- 在某些 DBMS 中可用于文本列, 此时返回排序后的第一行
- 忽略 NULL 值

### 9.1.5 SUM 函数 ###

SUM 用来返回指定列值的和:

```
SELECT SUM(quantity) AS items_ordered
FROM OrderItems
WHERE order_num = 20005;
```

- 忽略 NULL 值

## 9.2 聚集不同值 ##

聚集函数可以如下使用:

- 对所有行执行计算, 指定 ALL 参数(默认值)
- 只包含不同的值, 指定 DISTINCT 参数

```
SELECT AVG(DISTINCT prod_price) AS avg_price
FROM Products
WHERE vend_id = 'DLL01';
```

- DISTINCT 不能用于 COUNT(*)
- DISTINCT 可以用于 MAX 或 MIN, 但是没有实际价值

## 9.3 组合聚集函数 ##

SELECT 语句可根据需要包含多个聚集函数:

```
SELECT COUNT(*) AS num_items,
    MIN(prod_price) AS price_min,
    MAX(prod_price) AS price_max,
    AVG(prod_price) AS price_avg
FROM Products;
```
