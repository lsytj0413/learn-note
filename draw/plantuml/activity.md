# 活动图 #

## 简单例子 ##

使用 * 符号来表示活动图的起始点和结束点, 可以使用 (*top) 符号来让起始点出现在图的顶点. 使用 --> 符号来表示箭头.

将以下内容保存为 [activity01](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity01.pum):

```
@startuml

(*) --> "First Activity"
"First Activity" --> (*)

@enduml
```

生成的效果图如下:

![activity01.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity01.png)

## 文本标签 ##

默认的, 一个箭头是从最后一个使用的 activity 开始的, 而且可以在箭头上使用文本标签.

将以下内容保存为 [activity02](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity02.pum):

```
@startuml

(*) --> "First Activity"
-->[You can put also labels] "Second Activity"
-->(*)

@enduml
```

生成的效果图如下:

![activity02.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity02.png)

## 改变箭头方向 ##

可以使用 -> 来表示竖向箭头, 也可以使用以下示例中的方法修改箭头的方向.

将以下内容保存为 [activity03](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity03.pum):

```
@startuml

(*) -up-> "First Activity"
-right-> "Second Activity"
--> "Third Activity"
-left-> (*)

@enduml
```

生成的效果图如下:

![activity03.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity03.png)

## 分支 ##

可以使用 if, then, else 等关键字来定义分支.

将以下内容保存为[activity04](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity04.pum):

```
@startuml

(*) --> "Initialization"

if "Some Test" then
-->[true] "Some Activity"
--> "Another Activity"
-right-> (*)
else
-->[false] "Something else"
-->[Ending process] (*)
endif

@enduml
```

生成的效果图如下:

![activity04.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity04.png)

默认的, 一个分支的开始是从最后一个活动的 activity 开始的, 但是也可以使它从一个另外的 activity 开始. 而且分支也可以嵌套.

将以下内容保存为[activity05](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity05.pum):

```
@startuml

(*) --> if "Some Test" then

-->[true] "activity 1"

if "" then
-> "activity 3" as a3
else
if "Other test" then
-left-> "activity 5"
else
--> "activity 6"
endif
endif

else

->[false] "activity 2"

endif

a3 --> if "last test" then
--> "activity 7"
else
-> "activity 8"

endif

@enduml
```

生成的效果图如下:

![activity05.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity05.png)

## 同步 ##

可以使用 === 字符来定义同步方法.

将以下内容保存为[activity06](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity06.pum):

```
@startuml

(*) --> ===B1===
--> "Parallel Activity 1"
--> ===B2===

===B1=== --> "Parallel Activity 2"
--> ===B2===

--> (*)

@enduml
```

生成的效果图如下:

![activity06.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity06.png)

## 长描述 ##

在定义一个 activity 节点的时候可以添加多行的描述, 也可以通过 as 关键字给节点一个短的名称, 以便之后引用.

将以下内容保存为[activity07](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity07.pum):

```
@startuml

(*) -left-> "this <size:20>activity</size>
is <b>very</b> <color:red>long2</color>
and defined on several lines
that contains many <i>text</i>" as A1

-up-> "Another activity\n on several lines"

A1 --> "Short activity <img:../../img/chrome.png>"

@enduml
```

生成的效果图如下:

![activity07.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity07.png)

## 注解 ##

可以使用 note left, note right, note top 或者 note bottom 等关键字来定义 activity 节点的注解, 如果需要对开始节点定义注解, 可以在图形定义的开头使用注解. 也可以使用 endnote 关键字来定义多行注解.

将以下内容保存为[activity08](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity08.pum):

```
@startuml

(*) --> "Some Activity"
note right: This activity has to be defined
"Some Activity" --> (*)

note left
This note is on
several lines
end note

@enduml
```

生成的效果图如下:

![activity08.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity08.png)

## 分区 ##

可以使用 partition 关键字来定义不同的分区, 每个分区都可以定义使用 html 颜色值或名称来定义背景色. 默认的, 一个 activity 节点是被自动的放在最后一个使用的分区中.

将以下内容保存为[activity09](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity09.pum):

```
@startuml

partition Conductor {
(*) --> "Climbs on Platform"
--> === S1 ===
--> Bows
}

partition Audience #LightSkyBlue {
=== S1 === --> Applauds
}

partition Conductor {
Bows --> === S2 ===
--> WavesArmes
Applauds --> === S2 ===
}

partition Orchestra #CCCCEE {
WavesArmes --> Introduction
--> "Play music"
}

@enduml
```

生成的效果图如下:

![activity09.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity09.png)