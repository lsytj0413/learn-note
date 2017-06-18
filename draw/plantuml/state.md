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

## 组合 ##

使用 state 关键字和 {} 来定义组合的状态.

将以下内容保存为 [state02](./state/state02.pum):

```
@startuml

scale 360 width
[*] --> NotShooting

state NotShooting {
[*] --> Idle
Idle --> Configuring : EvConfig
Configuring --> Idle : EvConfig
}

state Configuring {
[*] --> NewValueSelection
NewValueSelection --> NewValuePreview : EvNewValue
NewValuePreview --> NewValueSelection : EvNewValueRejected
NewValuePreview --> NewValueSelection : EvNewValueSaved

state NewValuePreview {
State1 -> State2
}

}

@enduml
```

生成的效果图如下:

![state02.png](./state/state02.png)
