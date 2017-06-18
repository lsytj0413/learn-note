# 状态图 #

## 简单例子 ##

可以使用 [*] 符号作为开始节点和结束节点, 使用 --> 表示箭头.

将以下内容保存为 [state01](./state/state01.pum):

```
@startuml

[*] --> State1
State1 --> [*]
State1 : this is a string
State1 : this is another string

State1 -> State2
State2 --> [*]

@enduml
```

生成的效果图如下:

![state01.png](./state/state01.png)
