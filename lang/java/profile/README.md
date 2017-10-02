# Java Profile 笔记 #

## 查看 IO 高的线程 ##

1. 首先通过 iotop 命令观察线程的 io 情况, 假设发现 tid 为 20058 的线程 IO 操作比较多, 然后将线程号转换为 0x4e5a, 表示为 16 进制.
2. 通过 jps 或者 ps -ef 获取 Java 的进程号
3. 通过 jstack pid 获取线程的 stack 快照
4. 查找 nid=0x4e5a 的线程即为该 IO 操作多的线程堆栈

