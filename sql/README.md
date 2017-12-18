# SQL #

- [MySQL必知必会](./sql10m/README.md)

## MySQL ##

- [高性能MySQL](./HighPerformanceMySQL/README.md)

### 创建数据库及用户 ###

```
USE mysql;
CREATE DATABASE teach;
GRANT ALL PRIVILEGES ON teach.* TO 'user'@'%' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
```
