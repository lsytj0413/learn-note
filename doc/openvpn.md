# 搭建自己的 VPN #

1. 安装 openvpn

```
apt update
apt install openvpn easy-rsa
```

2. 复制 easy-ras 模板

```
mkdir-cadir ~/openvpn-ca
cd ~/openvpn-ca
```

3. 配置 CA 变量

打开 ~/openvpn-ca/vars 文件, 将以下内容:

```
export KEY_COUNTRY="US"
export KEY_PROVINCE="CA"
export KEY_CITY="SanFrancisco"
export KEY_ORG="Fort-Funston"
export KEY_EMAIL="me@myhost.mydomain"
export KEY_OU="MyOrganizationalUnit"
```

修改为任意的非空值, 将:

```
export KEY_NAME="server"
```

修改为任意值即可.

4. 构建 CA

```
cd ~/openvpn-ca
source vars
./clean-all
./build-ca
./build-key-server server
./build-dh
openvpn -genkey --secret keys/ta.key
```

5. 生成客户端证书密钥

```
cd ~/openvpn-ca
source vars
# xclient 为客户端名字
./build-key xclient
```

6. 配置 openvpn

```
$ cd ~/openvpn-ca/keys
$ sudo cp ca.crt ca.key server.crt server.key ta.key dh2048.pem /etc/openvpn
# 复制一个 openvpn 配置示例
$ gunzip -c /usr/share/doc/openvpn/examples/sample-config-files/server.conf.gz | sudo tee /etc/openvpn/server.conf
```

打开 /etc/openvpn/server.conf 文件, 将 redirect-gateway 行注释去掉, 并修改为如下:

```
push "redirect-gateway def1 bypass-dhcp"
```

将 dhcp-option 及 tls-auth 行注释去掉, 并修改:

```
push "dhcp-option DNS 208.67.222.222"
push "dhcp-option DNS 208.67.220.220"

tls-auth ta.key 0 # This file is secret
# 新增一行
key-direction 0
```

最后, 去掉 user 和 group 行的注释(这个配置似乎版本较老):

7. 调整网络配置

编辑 /etc/sysctl.conf 配置文件, 增加:

```
net.ipv4.ip_forward=1
```

使用 **sysctl -p** 命令使配置生效.

8. 调整 UFW 规则(似乎会使 ssh 失效, 可不配置, 直接使用 iptables)

编辑 /etc/ufw/before.rules, 新增 OpenVPN 相关内容:

```
1 # START OPENVPN RULES
12 # NAT table rules
13 *nat
14 :POSTROUTING ACCEPT [0:0] 
15 # Allow traffic from OpenVPN client to eth0
16 -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE
17 COMMIT
18 # END OPENVPN RULES
```

其中的 eth0 需使用服务器的网络设备名称, 可使用 **ip route | grep default** 命令获取.

修改 /etc/default/ufw 文件, 修改如下行:

```
DEFAULT_FORWARD_POLICY="ACCEPT"
```

打开 ufw:

```
$ sudo ufw allow 1194/udp

$ sudo ufw disable
$ sudo ufw enable
```

或者将如上内容采用 iptables 命令配置:

```
iptables -t nat -A POSTROUTING -o eth1 -s 10.8.0.0/24 -j MASQUERADE
```

9. 启动 OpenVPN

```
$ sudo systemctl start openvpn@server
# 设置自启动
$ sudo systemctl enable openvpn@server
```

10. 创建客户端配置

```
$ mkdir -p ~/client-configs/files
$ chmod 700 ~/client-configs/files
$ cp /usr/share/doc/openvpn/examples/sample-config-files/client.conf ~/client-configs/base.conf
```

打开 base.conf 文件, 将 remote 行修改为服务器IP, 去掉 user 和 group 前注释, 注释掉如下内容:

```
# SSL/TLS parms.
# See the server config file for more
# description.  It's best to use
# a separate .crt/.key file pair
# for each client.  A single ca
# file can be used for all clients.
#ca ca.crt
#cert client.crt
#key client.key
```

并新增一行:

```
key-direction 1
```

11. 创建配置生成脚本

新建 ~/client-configs/make_config.sh 内容如下:

```
#!/bin/bash

# First argument: Client identifier

KEY_DIR=~/openvpn-ca/keys
OUTPUT_DIR=~/client-configs/files
BASE_CONFIG=~/client-configs/base.conf

cat ${BASE_CONFIG} \
    <(echo -e '<ca>') \
    ${KEY_DIR}/ca.crt \
    <(echo -e '</ca>\n<cert>') \
    ${KEY_DIR}/${1}.crt \
    <(echo -e '</cert>\n<key>') \
    ${KEY_DIR}/${1}.key \
    <(echo -e '</key>\n<tls-auth>') \
    ${KEY_DIR}/ta.key \
    <(echo -e '</tls-auth>') \
    > ${OUTPUT_DIR}/${1}.ovpn
```

赋予执行权限:

```
$ chmod 700 ~/client-configs/make_config.sh
```

12. 生成客户端配置

```
$ cd ~/client-configs
$ ./make_config.sh xclient
```

生成的配置文件在 ~/client-configs/files 目录下.