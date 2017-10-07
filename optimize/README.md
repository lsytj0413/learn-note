# 性能优化 #

## linux ##

### sysctl.conf ###

此节描述一些 sysctl.conf 中需要更改的配置, 在性能测试过程中使用的配置如下:


```
net.core.somaxconn=2550000
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_syncookies = 1    
fs.file-max = 999999    
net.ipv4.tcp_max_tw_buckets = 6000    
net.ipv4.tcp_tw_recycle = 1   
net.core.netdev_max_backlog=262114  
net.ipv4.tcp_max_syn_backlog = 262114    
net.ipv4.tcp_max_orphans=262114     
net.ipv4.tcp_synack_retries=1    
net.ipv4.tcp_syn_retries=1  
net.ipv4.tcp_keepalive_time = 600   
net.ipv4.tcp_fin_timeout = 30   
net.ipv4.ip_local_port_range = 1024 65000   
net.ipv4.tcp_rmem = 10240 87380 12582912
net.ipv4.tcp_wmem = 10240 87380 12582912
net.core.rmem_default = 6291456
net.core.wmem_default = 6291456
net.core.rmem_max = 12582912
net.core.wmem_max = 12582912 
```

[Linux Web Server Kernel Tuning](https://gist.github.com/kgriffs/4027835) 描述了如下的配置:

```
# Configuration file for runtime kernel parameters.
# See sysctl.conf(5) for more information.

# See also http://www.nateware.com/linux-network-tuning-for-2013.html for
# an explanation about some of these parameters, and instructions for
# a few other tweaks outside this file.

# Protection from SYN flood attack.
net.ipv4.tcp_syncookies = 1

# See evil packets in your logs.
net.ipv4.conf.all.log_martians = 1

# Discourage Linux from swapping idle server processes to disk (default = 60)
vm.swappiness = 10

# Tweak how the flow of kernel messages is throttled.
#kernel.printk_ratelimit_burst = 10
#kernel.printk_ratelimit = 5

# --------------------------------------------------------------------
# The following allow the server to handle lots of connection requests
# --------------------------------------------------------------------

# Increase number of incoming connections that can queue up
# before dropping
net.core.somaxconn = 50000

# Handle SYN floods and large numbers of valid HTTPS connections
net.ipv4.tcp_max_syn_backlog = 30000

# Increase the length of the network device input queue
net.core.netdev_max_backlog = 5000

# Increase system file descriptor limit so we will (probably)
# never run out under lots of concurrent requests.
# (Per-process limit is set in /etc/security/limits.conf)
fs.file-max = 100000

# Widen the port range used for outgoing connections
net.ipv4.ip_local_port_range = 10000 65000

# If your servers talk UDP, also up these limits
net.ipv4.udp_rmem_min = 8192
net.ipv4.udp_wmem_min = 8192

# --------------------------------------------------------------------
# The following help the server efficiently pipe large amounts of data 
# --------------------------------------------------------------------

# Disable source routing and redirects
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.all.accept_source_route = 0

# Disable packet forwarding.
net.ipv4.ip_forward = 0
net.ipv6.conf.all.forwarding = 0

# Disable TCP slow start on idle connections
net.ipv4.tcp_slow_start_after_idle = 0

# Increase Linux autotuning TCP buffer limits
# Set max to 16MB for 1GE and 32M (33554432) or 54M (56623104) for 10GE
# Don't set tcp_mem itself! Let the kernel scale it based on RAM.
# net.core.rmem_max = 16777216
# net.core.wmem_max = 16777216
# net.core.rmem_default = 16777216
# net.core.wmem_default = 16777216
# net.core.optmem_max = 40960
# net.ipv4.tcp_rmem = 4096 87380 16777216
# net.ipv4.tcp_wmem = 4096 65536 16777216


# --------------------------------------------------------------------
# The following allow the server to handle lots of connection churn
# --------------------------------------------------------------------

# Disconnect dead TCP connections after 1 minute
net.ipv4.tcp_keepalive_time = 60

# Wait a maximum of 5 * 2 = 10 seconds in the TIME_WAIT state after a FIN, to handle
# any remaining packets in the network. 
net.ipv4.netfilter.ip_conntrack_tcp_timeout_time_wait = 5

# Allow a high number of timewait sockets
net.ipv4.tcp_max_tw_buckets = 2000000

# Timeout broken connections faster (amount of time to wait for FIN)
net.ipv4.tcp_fin_timeout = 10

# Let the networking stack reuse TIME_WAIT connections when it thinks it's safe to do so
net.ipv4.tcp_tw_reuse = 1

# Determines the wait time between isAlive interval probes (reduce from 75 sec to 15)
net.ipv4.tcp_keepalive_intvl = 15

# Determines the number of probes before timing out (reduce from 9 sec to 5 sec)
net.ipv4.tcp_keepalive_probes = 5

```

另有一篇文章描述了如下的配置:

```
vm.swappiness = 0
net.ipv4.neigh.default.gc_stale_time=120
net.ipv4.conf.all.rp_filter=0
net.ipv4.conf.default.rp_filter=0
net.ipv4.conf.default.arp_announce = 2
net.ipv4.conf.all.arp_announce=2
net.ipv4.tcp_max_tw_buckets = 100
net.ipv4.tcp_syncookies = 0
net.ipv4.tcp_max_syn_backlog = 3240000
net.ipv4.tcp_window_scaling = 1
#net.ipv4.tcp_keepalive_time = 60
net.ipv4.tcp_synack_retries = 2
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
net.ipv4.conf.lo.arp_announce=2
fs.file-max = 40000500
fs.nr_open = 40000500
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_keepalive_time = 1
net.ipv4.tcp_keepalive_intvl = 15
net.ipv4.tcp_keepalive_probes = 3

net.ipv4.tcp_fin_timeout = 5
net.ipv4.tcp_mem = 768432 2097152 15242880
net.ipv4.tcp_rmem = 4096 4096 33554432
net.ipv4.tcp_wmem = 4096 4096 33554432
net.core.somaxconn = 6553600
net.ipv4.ip_local_port_range = 2048 64500
net.core.wmem_default = 183888608
net.core.rmem_default = 183888608
net.core.rmem_max = 33554432
net.core.wmem_max = 33554432
net.core.netdev_max_backlog = 2621244
kernel.sem=250 65536 100 2048
kernel.shmmni = 655360
kernel.shmmax = 34359738368
kerntl.shmall = 4194304
kernel.msgmni = 65535
kernel.msgmax = 65536
kernel.msgmnb = 65536

net.netfilter.nf_conntrack_max=1000000
net.nf_conntrack_max=1000000
net.ipv4.netfilter.ip_conntrack_max=1000000
kernel.perf_cpu_time_max_percent=60
kernel.perf_event_max_sample_rate=6250

net.ipv4.tcp_max_orphans=1048576
kernel.sched_migration_cost_ns=5000000
net.core.optmem_max = 25165824

kernel.sem=10000 2560000 10000 256
```

### limits.conf ###

有些时候需要修改文件句柄的限制数, 首先需要修改系统限制, 在 sysctl.conf 写入:

```
fs.file-max = 999999
```

然后编辑 /etc/security/limits.conf 文件:

```
* soft nofile 65535
* hard nofile 65535
# * does not match root on ubuntu
root soft nofile 65535
root hard nofile 65535
```

# 参考资料 #

[Optimizing servers - Tuning the GNU/Linux Kernel](https://tweaked.io/guide/kernel/)

[docker container optimize](http://blog.csdn.net/wangjia184/article/details/44907233)

[Linux下的IO监控与分析](http://itindex.net/detail/46239-linux-io-%E5%88%86%E6%9E%90)

[JVM performance optimization](https://www.javaworld.com/article/2078623/core-java/jvm-performance-optimization-part-1-a-jvm-technology-primer.html)

[Linux系统优化之网络IO调优](http://yijiu.blog.51cto.com/433846/1559472)

