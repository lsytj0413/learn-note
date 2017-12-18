# 第7章: 创建计算字段 #

## 7.1 计算字段 ##

计算字段并不实际存在于数据库表中, 是运行时在 SELECT 语句内创建的.

从客户端看, 计算字段的数据与其他列的数据的返回方式相同.

## 7.2 拼接字段 ##

例如要将 vend\_name 和 vend\_country 拼接成 vend\_name (vend\_country), 可以使用如下的写法:

```
SELECT RTRIM(vend_name) + '(' + RTRIM(vend_country) + ')'
FROM Vendors
ORDER BY vend_name;

# 或者
SELECT RTRIM(vend_name) || '(' || RTRIM(vend_country) || ')' AS vend_title
FROM Vendors
ORDER BY vend_name;

# MySQL
SELECT Concat(vend_name, '(', vend_country, ')') AS vend_title
FROM Vendors
ORDER BY vend_name;
```

- 使用 RTRIM 函数去除值右边的所有空格, 这一类函数包括 RTRIM, LTRIM, TRIM
- 可以使用加号或两个竖线, MySQL 中必须使用特殊的函数
- 可以使用 AS 关键字赋予别名

## 7.3 执行算术计算 ##

```
SELECT prod_id, quantity, item_price, quantity*item_price AS expanded_price
FROM OrderItems
WHERE order_num = 20008;
```

SQL 支持的算术操作符如下:

| 操作符 | 说明 |
|:--|:--|
| + | 加 |
| - | 减 |
| * | 乘 |
| / | 除 |

