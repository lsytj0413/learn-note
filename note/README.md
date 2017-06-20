# note #

## ssh 中允许root登录 ##

编辑 /etc/ssh/sshd_config 文件, 将以下内容:

```
# Authentication:
LoginGraceTime 120
PermitRootLogin prohibit-password
StrictModes yes
```

修改为:

```
# Authentication:
LoginGraceTime 120
# PermitRootLogin prohibit-password
PermitRootLogin yes
StrictModes yes
```

然后使用以下命令重启 ssh 服务即可:

```
service ssh restart
```

## ssh免密码登录 ##

配置 A服务器的用户 ua 免密码登录 B 服务器的用户 ud.

```
# 在A服务器上
su - ua
# 生成密钥对
ssh-keygen -t rsa
ls -la ~/.ssh

# 将生成的公钥上传到 B服务器
ssh-copy-id ub@B
# 此时ua的公钥内容会写入 ub 的 ~/.ssh/authorized_keys 文件中

# 免密码登录
ssh hb@B
```

将公钥拷贝的其他服务器有以下几种方法:

1. 通过 scp 拷贝然后追加到 authorized_keys 文件

```
scp -P 22 ~/.ssh/id_rsa.pub user@host:~/
# 然后追加到 authorized_keys
```

2. 通过 ssh-copy-id

```
ssh-copy-id user@host
```

3. 通过普通的 ssh 命令

```
cat ~/.ssh/id_rsa.pub | ssh -p 22 user@host 'cat >> ~/.ssh/authorized_keys'
```
