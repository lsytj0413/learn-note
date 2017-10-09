# Java 性能优化 #

## 火焰图 ##

本节介绍如何在 Java 中使用火焰图工具来查找性能瓶颈. 平台为 Ubuntu 16.04, java 版本为 1.8.0_144.

### perf-map-agent ###

本节介绍使用 perf-map-agent 来显示 Java 中的 CPU 使用率统计, 该使用率统计中不包括系统时间.

#### 安装工具 ####

1. 安装 Linux perf_events

```
apt install linux-tools-common
```

2. Java8

3. perf-map-agent

[perf-map-agent](https://github.com/jvm-profiling-tools/perf-map-agent) 一个 JVM Agent, 用来将 Java 符号翻译为 perf_events 可识别的符号.

```
apt install cmake
export JAVA_HOME=/path/jdk8
git clone --depth=1 https://github.com/jrudolph/perf-map-agent
cd perf-map-agent
cmake .
make
```

编译成功后会生成 out 目录, 包含 attach-main.jar 文件.

4. FlameGraph

[FlameGraph](https://github.com/brendangregg/FlameGraph) 是一个由 Perl 语言编写的火焰图生成工具, 用于将 perf 等的结果转换为更直观的火焰图图形.

```
git clone --depth=1 https://github.com/brendangregg/FlameGrap
```

FlameGraph 目录下包含有很多 perl 脚本, 可以将该目录添加到 **PATH** 中以方便使用.

#### 配置 Java ####

Java 程序需要使用 **+XX:PreserveFramePointer** 选项启动.

#### 生成火焰图 ####

在以下代码中假设 Java 程序的 pid 为 12345.

##### 生成系统范围内的火焰图 #####

```
sudo perf record -F 99 -a -g -- sleep 30
# 使用与 Java 进程 12345 相同的用户运行以下命令
java -cp attach-main.jar:$JAVA_HOME/lib/tools.jar net.virtualvoid.perf.AttachOnce 12345
sudo chown root /tmp/perf-*.map
sudo perf script | stackcollapse-perf.pl | flamegraph.pl --color=java --hash > flamegraph.svg
```

在上例中, 也可以在运行 perf record 时指定 pid 来针对某个进程进行采样. 例如:

```
sudo perf record -F 99 -a -g -p 12345 -- sleep 30
```

在运行 perf record 的命令的过程中, 会生成 perf.data 文件到当前目录.

**使用 jmaps 自动处理符号转换**

```
sudo perf record -F 99 -a -g -- sleep 30; sudo jmaps
sudo perf script | stackcollapse-perf.pl | flamegraph.pl --color=java --hash > flamegraph.svg
```

在执行 sudo 时可能会出现 jmaps not found 的错误(这是因为在 Ubuntu 上执行 sudo 命令时会重置 PATH), 这时在 ~/.bashrc 中加入以下内容即可:

```
alias sudo="sudo env PATH=$PATH"
```

##### 对不同的 Java 进程生成不同的火焰图 #####

在上节介绍的方法中, 会将系统中所有的 Java 进程生成到一起, 可以使用以下代码来区分不同的进程:

```
sudo perf record -F 99 -a -g -- sleep 30; sudo jmaps
sudo perf script -f comm,pid,tid,cpu,time,event,ip,sym,dso,trace | \
    stackcollapse-perf.pl --pid | \
    flamegraph.pl --color=java --hash > flamegraph.svg
```

经过 stackcollapse-perf.pl 处理的内容为每一行代表一个 stack, 可以在之后接入 grep/sed/awk 命令来对内容进行筛选, 例如在输入到 flamegraph.pl 之前使用 grep java-339 , 确保只输出 pid 为 339 的 Java 进程的火焰图.

### lightweight-java-profiler ###

[lightweight-java-profiler](https://github.com/dcapwell/lightweight-java-profiler) 是一个 stack trace 的 profiler 工具.

#### 安装 lightweight-java-profiler ####

```
git clone https://github.com/dcapwell/lightweight-java-profiler
cd lightweight-java-profiler
# 将 Makefile 中的 BITS 设置为 64, 和系统位数相关
make all
```

编译成功后会生成 build-64 目录, 其中包含 liblagent.so 文件.

在启动 Java 程序时添加参数 -agentpath:/path/to/liblagent.so, 然后在 Java 开始运行时会进行采样, 当程序结束时采样停止(不能 kill 进程), 采样数据会写入 traces.txt 文件中.

#### 生成火焰图 ####

可以通过 FlameGraph 将上一步生成的 traces.txt 文件输出为火焰图:

```
stackcollapse-ljp.awk < ./traces.txt | flamegraph.pl > traces.svg
```

# 参考资料 #

- [Java Flame Graphs --Brendan Gregg's Blog](http://www.brendangregg.com/blog/2014-06-12/java-flame-graphs.html)
- [[译]Java火焰图 --Brendan Gregg's Blog](http://colobu.com/2016/08/10/Java-Flame-Graphs/)
- [CPU Flame Graphs](http://www.brendangregg.com/FlameGraphs/cpuflamegraphs.html#Java)
- [Java in Flames](https://medium.com/netflix-techblog/java-in-flames-e763b3d32166)
