# 第3章: 排序检索数据 #

## 3.1 排序数据 ##

可以使用 ORDER BY 子句来排序检索出的数据:

```
SELECT prod_name FROM Products ORDER BY prod_name;
```

- ORDER BY 应该是 SELECT 语句中最后一条子句
- 可以使用非检索的列排序数据

## 3.2 按多个列排序 ##

可以对多个列进行排序, 例如首先按价格, 然后按名称排序:

```
SELECT prod_id, prod_price, prod_name
FROM Products
ORDER BY prod_price, prod_name;
```

## 3.3 按列位置排序 ##

ORDER BY 子句支持按相对位置进行排序:

```
SELECT prod_id, prod_price, prod_name
FROM Products
ORDER BY 2, 3;
```

## 3.4 指定排序方向 ##

默认的排序顺序是升序, 也可以指定 DESC 关键字进行降序排序:

```
SELECT prod_id, prod_price, prod_name
FROM Products
ORDER BY prod_price DESC, prod_name;
```

DESC 关键字只应用到直接位于其前面的列名.

