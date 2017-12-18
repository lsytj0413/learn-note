# 第10章: 分组数据 #

## 10.1 数据分组 ##

使用分组可以将数据分为多个逻辑组, 对每个组进行聚集计算.

## 10.2 创建分组 ##

分组是使用 SELECT 语句的 GROUP BY 子句建立的:

```
SELECT vend_id, COUNT(*) AS num_prods
FROM Products
GROUP BY vend_id;
```

使用 GROUP BY 的规则如下:

- 可以包含任意数目的列
- 如果在 GROUP BY 中嵌套了分组, 数据将在最后指定的分组上进行汇总
- GROUP BY 中列出的每一列都必须是检索列或有效的表达式
- 大多数 SQL 实现不允许 GROUP BY 带有长度可变的数据类型
- 除聚集函数外, SELECT 语句的每一列都必须在 GROUP BY 子句中给出
- 如果分组列中含有 NULL 值, 所有 NULL 将分为一组
- GROUP BY 必须出现在 WHERE 之后, ORDER BY 之前

## 10.3 过滤分组 ##

SQL 允许对分组进行过滤, 即使用类似 WHERE 子句的 HAVING 子句, 而且 HAVING 子句支持所有 WHERE 子句的用法, 只是关键字不同:

```
SELECT cust_id, COUNT(*) AS orders
FROM Orders
GROUP BY cust_id
HAVING COUNT(*) >= 2;
```

也可以同时使用 WHERE 与 HAVING:

```
SELECT vend_id, COUNT(*) AS num_prods
FROM Products
WHERE prod_price >= 4
GROUP BY vend_id
HAVING COUNT(*) >= 2;
```

## 10.4 分组和排序 ##

GROUP BY 和 ORDER BY 的差别如下:

| ORDER BY | GROUP BY |
|:--|:--|
| 对产生的输出排序 | 分组, 但输出可能不是分组的顺序 |
| 任意列可使用 | 只能使用选择列或表达式列, 而且必须使用每个选择列表达式 |
| 不一定需要 | 如果与聚集函数一起使用列或表达式, 则必须使用 |

- 一般在使用 GROUP BY 时也应该给出 ORDER BY 子句

```
SELECT order_num, COUNT(*) AS items
FROM OrderItems
GROUP BY order_num
HAVING COUNT(*) >= 3
ORDER BY items, order_num;
```

## 10.5 SELECT 子句顺序 ##

SELECT 子句及其顺序如下表:

| 子句 | 说明 | 是否必须 |
| SELECT | 要返回的列或表达式 | 是 |
| FROM | 从中检索数据的表 | 仅在从表中选择数据时使用 |
| WHERE | 行级过滤 | 否 |
| GROUP BY | 分组说明 | 仅在按组计算聚集时使用 |
| HAVING | 组级过滤 | 否 |
| ORDER BY | 输出排序顺序 | 否 |
