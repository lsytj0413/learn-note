# 第十五章: 存储介质 #

本章介绍的命令如下:

- mount: 挂载文件系统
- unmount: 卸载文件系统
- fdisk: 硬盘分区命令
- fsck: 检查修复文件系统
- fdformat: 格式化软盘
- mkf: 创建文件系统
- dd: 向设备直接写入, 面向块数据
- genisoimage(mkisofs): 创建一个ISO9600映像文件
- wodim(cdrecord): 向光存储介质写入数据
- md5sum: 计算MD5校验码

## 15.1 挂载, 卸载存储设备 ##

将设备添加到文件系统树中, 从而允许操作系统可以操作该设备的过程称为挂载.

/etc/fstab 文件内容列出了系统启动时挂载的设备, 例如:

```
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/nvme0n1p3 during installation
UUID=dca22cc7-f4ac-4132-a504-d1742096a228 /               ext4    errors=remount-ro 0       1
# /boot was on /dev/nvme0n1p2 during installation
UUID=40fac7d4-d032-41e3-a831-7b3c22fa4d23 /boot           ext4    defaults        0       2
# /boot/efi was on /dev/nvme0n1p1 during installation
UUID=62E0-6A7E  /boot/efi       vfat    umask=0077      0       1
# /home was on /dev/nvme0n1p5 during installation
UUID=02c7ab2f-3bfb-4571-8153-0cf798c18268 /home           ext4    defaults        0       2
# swap was on /dev/nvme0n1p4 during installation
UUID=902b5bdd-e2da-4ad5-b324-b483b989d68f none            swap    sw              0       0
```

该文件中每一行的内容包含6个字段, 每个字段的含义如下表:

| 字段 | 内容 | 描述 |
|:--|:--|:--|
| 1 | 设备 | 通常表示与物理设备相关的设备文件的真实名称, 比如/dev/hda1代表第一个IDE通道上的第一块分区, 也可以使用文本标签来关联设备. |
| 2 | 挂载节点 | 设备附加到文件系统树上的目录 |
| 3 | 文件系统类型 | 支持如 ext4, FAT16, NTFS等 |
| 4 | 选项 | 挂载时的选项参数, 例如只读等 |
| 5 | 频率 | 用于dump命令决定是否对该文件系统进行备份以及多久备份一次 |
| 6 | 优先级 | 用于fsck命令决定在启动时需要被扫描的文件系统的顺序 |

### 15.1.1 查看已挂载的文件系统列表 ###

### 15.1.2 确定设备名称 ###

## 15.2 创建新的文件系统 ##

### 15.2.1 用fdisk命令进行磁盘分区 ###

### 15.2.2 用mkfs命令创建新的文件系统 ###

## 15.3 测试, 修复文件系统 ##

## 15.4 格式化软盘 ##

## 15.5 直接从/向设备转移数据 ##

## 15.6 创建CD-ROM映像 ##

### 15.6.1 创建一个CD-ROM文件映像副本 ###

### 15.6.2 从文件集合中创建映像文件 ###

## 15.7 向CD-ROM写入映像文件 ##

### 15.7.1 直接挂载ISO映像文件 ###

### 15.7.2 擦除可读写CD-ROM ###

### 15.7.3 写入映像文件 ###

## 15.8 附加认证 ##
