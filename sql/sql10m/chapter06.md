# 第6章: 用通配符进行过滤 #

## 6.1 LIKE 操作符 ##

通配符是 SQL 的 WHERE 子句中有特殊含义的字符, 在搜索子句中使用通配符必须使用 LIKE 操作符. 通配符只能用于搜索文本字段.

### 6.1.1 百分号通配符 ###

百分号表示任何字符出现任意次数:

```
SELECT prod_id, prod_name FROM Products WHERE prod_name LIKE 'Fish%';
```

- 百分号可以匹配0个字符
- 百分号不能匹配 NULL

### 6.1.2 下划线通配符 ###

用途与百分号一样, 但是只匹配单个字符.

```

SELECT prod_id, prod_name FROM Products WHERE prod_name LIKE '__ inch teddy bear';
```

### 6.1.3 方括号通配符 ###

方括号通配符用来指定一个字符集, 必须匹配指定位置的一个字符.

```
SELECT cust_concact FROM Customers WHERE cust_contact LIKE '[JM]%' ORDER BY cust_contact;
```

此通配符可以使用前缀字符 ^ 来否定.

```
SELECT cust_concact FROM Customers WHERE cust_contact LIKE '[^JM]%' ORDER BY cust_contact;
```

## 6.2 使用通配符的技巧 ##

- 不要过度使用
- 不要用在搜索模式的开始处
- 仔细注意通配符的位置
