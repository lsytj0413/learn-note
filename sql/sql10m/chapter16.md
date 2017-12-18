# 第16章: 更新和删除数据 #

## 16.1 更新数据 ##

可以使用 UPDATE 语句更新数据, 有以下两种使用方式:

- 更新特定行
- 更新所有行

```
UPDATE Customers
SET cust_contact = 'Sam Roberts',
    cust_email = 'sam@toyland.com'
WHERE cust_id = '1000000006';
```

- 在 UPDATE 语句中可以使用子查询

## 16.2 删除数据 ##

可以使用 DELETE 语句删除行, 有以下两种使用方式:

- 删除特定行
- 删除所有行

```
DELETE FROM Customers
WHERE cust_id = '1000000006';
```

- 如果要删除所有行可以使用 TRUNCATE TABLE 语句, 它速度更快

## 16.3 更新和删除的指导原则 ##

- 除非打算更新和删除每一行, 否则应该带 WHERE 子句
- 保证每个表都有主键
- 应该先用 SELECT 测试保证过滤的是正确的记录
- 使用强制实施引用完整性的数据库
- 有的 DBMS 允许管理员施加约束防止执行不带 WHERE 子句的 UPDATE 或 DELETE
