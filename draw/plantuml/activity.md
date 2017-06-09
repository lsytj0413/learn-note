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
```

生成的效果图如下:

![activity02.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/activity/activity02.png)
