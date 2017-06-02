# 用例图 #

## 简单例子 ##

用例是指使用小括号包围起来的文字, 也可以使用 usecase 关键字来定义用例, 使用 as 关键字来定义别名.

将以下内容保存为 [usecase01](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase01.pum):

```
@startuml

(First usecase)
(Another usecase) as (UC2)
usecase UC3
usecase (Last\nusecase) as UC4

@enduml
```

生成的效果图如下:

![usecase01.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase01.png)

## 参与者 ##

参与者使用引号包含, 也可以使用 actor 关键字来定义参与者, 使用 as 关键字来定义别名.

将以下内容保存为 [usecase02](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase02.pum):

```
@startuml

:First Actor:
:Another\nactor: as Men2
actor Men3
actor :Last actor: as Men4

@enduml
```

生成的效果图如下:

![usecase02.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase02.png)

## 描述 ##

可以使用引号来包含多行的描述文本, 也可以使用 --..==__ 等字符来定义一些分隔符.

将以下内容保存为 [usecase03](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase03.pum):

```
@startuml

usecase UC1 as "You can use
several lines to define your usecase.
You can also use separators.
--
Several separators are possible.
==
And you can add titles:
..Conclusion..
This allows large description."

@enduml
```

生成的效果图如下:

![usecase03.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase03.png)

## 基础实例 ##

可以使用 --> 字符来定义连线, 并通过 : 字符来添加文本标签.

将以下内容保存为 [usecase04](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase04.pum):

```
@startuml

User -> (Start)
User --> (Use the application) : A small label

:Main Admin: ---> (Use the application) : This is\nyet another\nlabel

@enduml
```

生成的效果图如下:

![usecase04.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase04.png)

## 扩展 ##

如果一个参与者是扩展自另一个参与者, 可以使用 <|-- 来定义.

将以下内容保存为 [usecase05](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase05.pum):

```
@startuml

:Main Admin: as Admin
(Use the application) as (Use)

User <|-- Admin
(Start) <|-- (Use)

@enduml
```

生成的效果图如下:

![usecase05.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase05.png)

## 注解 ##

可以使用 note left of, note right of, note top of, note bottom of 等关键字来定义一个关联到元素的注解.
注解也可以使用 note 关键字来定义, 通过 .. 等符号来关联到元素.

将以下内容保存为 [usecase06](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase06.pum):

```
@startuml

:Main Admin: as Admin
(Use the application) as (Use)

User -> (Start)
User --> (Use)

Admin ---> (Use)

note right of Admin : This is an example.

note right of (Use)
A note can also
be on several lines
end note

note "This note is connected\nto several objects." as N2
(Start) .. N2
N2 .. (Use)

@enduml
```

生成的效果图如下:

![usecase06.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase06.png)

## 模板 ##

可以使用 << 和 >> 符号在参与者旁边定义模板数据.

将以下内容保存为 [usecase07](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase07.pum):

```
@startuml

User << Human >>
:Main Database: as MySql << Application >>
(Start) << One Shot >>
(Use the application) as (Use) << Main >>

User -> (Start)
User --> (Use)

MySql --> (Use)

@enduml
```

生成的效果图如下:

![usecase07.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase07.png)

## 修改箭头方向 ##

默认的, 使用 -- 或 .. 符号定义的箭头方向是竖直的, 也可以使用 - 或 . 符号来定义水平的箭头. 也可以使用 < 来修改反转箭头的连接方向, 也可以使用 left, right, up 和 down 等关键字来定义方向, 可以只使用关键字的一个或二个字母.

一般来说, 应该尽量避免使用这个特性, 因为 graphviz 可以自动的做好这种方向调整.


将以下内容保存为 [usecase08](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase08.pum):

```
@startuml

:user: --> (Use case 1)
:user: -> (Use case 2)

(Use case 3) <.. :user:
(Use case 4) <- :user:

:user1: -left-> (dummyLeft)
:user1: -r-> (dummyRight)
:user1: -up-> (dummyUp)
:user1: -do-> (dummyDown)

@enduml
```

生成的效果图如下:

![usecase08.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase08.png)
