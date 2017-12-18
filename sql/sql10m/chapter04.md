# 第4章: 过滤数据 #

## 4.1 使用WHERE子句 ##

只检索所需数据需要指定搜索条件, 也称为过滤条件.

```
SELECT prod_name, prod_price
FROM Products
WHERE prod_price = 3.49;
```

- ORDER BY 语句应该位于 WHERE 之后

## 4.2 WHERE子句操作符 ##

SQL 支持的所有条件操作符如下:

| 操作符  | 说明                             |
| :--     | :--                              |
| =       | 等于                             |
| <>      | 不等于                           |
| !=      | 不等于                           |
| <       | 小于                             |
| <=      | 小于等于                         |
| !<      | 不小于                           |
| >       | 大于                             |
| >=      | 大于等于                         |
| !>      | 不大于                           |
| BETWEEN | 在指定的两个值之间, 包含这两个值 |
| IS NULL | 为 NULL 值                       |

### 4.2.1 检查单个值 ###

```
SELECT prod_name, prod_price FROM Products WHERE prod_price <= 10;
```

### 4.2.2 不匹配检查 ###

```
SELECT vend_id, prod_name FROM Products WHERE vend_id <> 'DLL01';
```

- 单引号用来限定字符串

### 4.2.3 范围值检查 ###

```
SELECT prod_name, prod_price FROM Products WHERE prod_price BETWEEN 5 AND 10;
```

### 4.2.4 空值检查 ###

```
SELECT prod_name, prod_price FROM Products WHERE prod_price IS NULL;
```

- 过滤时不会返回含 NULL 值的行
