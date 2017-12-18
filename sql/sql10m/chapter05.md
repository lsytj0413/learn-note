# 第5章: 高级过滤数据 #

## 5.1 组合WHERE子句 ##

可以通过 AND 或 OR 字句组合多个 WHERE 条件.

### 5.1.1 AND 操作符 ###

```
SELECT prod_id, prod_price, prod_name
FROM Products
WHERE vend_id = 'DLL01' AND prod_price <= 4;
```

### 5.1.2 OR 操作符 ###

```
SELECT prod_id, prod_price, prod_name
FROM Products
WHERE vend_id = 'DLL01' OR vend_id = 'BRS01';
```

### 5.1.3 求值顺序 ###

WHERE 子句可以包含任意数目的 AND 和 OR 操作符, 并允许两者结合以进行复杂的过滤.

SQL 在处理 OR 操作符之前优先处理 AND 操作符. 可以使用括号进行明确的分组:

```
SELECT prod_id, prod_price, prod_name
FROM Products
WHERE (vend_id = 'DLL01' OR vend_id = 'BRS01')
AND prod_price >= 10;
```

- 使用具有 AND 和 OR 操作符的 WHERE 子句时都应该使用括号明确的分组

## 5.2 IN 操作符 ##

IN 操作符用来指定条件范围, 范围中的每个条件都可以进行匹配:

```
SELECT prod_name, prod_price
FROM Products
WHERE vend_id IN ('DLL01', 'BRS01')
ORDER BY prod_name;
```

- IN 操作符更清楚直观
- 求值顺序更易管理
- IN 操作符一般比一组 OR 执行更快
- 可以包含其他 SELECT 语句
- IN 操作符功能与 OR 相当

## 5.3 NOT 操作符 ##

NOT 可以否定其后所跟的任何条件, 可以用在要过滤的列前.

```
SELECT prod_name
FROM Products
WHERE NOT vend_id = 'DLL01'
ORDER BY prod_name;
```
