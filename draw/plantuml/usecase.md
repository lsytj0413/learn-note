# 用例图 #

## 简单例子 ##

用例是指使用小括号包围起来的文字, 也可以使用 usecase 关键字来定义用例, 使用 as 关键字来定义别名.

将以下内容保存为 [usecase01](./usecase/usecase01.pum):

```
@startuml

(First usecase)
(Another usecase) as (UC2)
usecase UC3
usecase (Last\nusecase) as UC4

@enduml
```

生成的效果图如下:

![usecase01.png](./usecase/usecase01.png)

## 参与者 ##

参与者使用引号包含, 也可以使用 actor 关键字来定义参与者, 使用 as 关键字来定义别名.

将以下内容保存为 [usecase02](./usecase/usecase02.pum):

```
@startuml

:First Actor:
:Another\nactor: as Men2
actor Men3
actor :Last actor: as Men4

@enduml
```

生成的效果图如下:

![usecase02.png](./usecase/usecase02.png)

## 描述 ##

可以使用引号来包含多行的描述文本, 也可以使用 --..==__ 等字符来定义一些分隔符.

将以下内容保存为 [usecase03](./usecase/usecase03.pum):

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

![usecase03.png](./usecase/usecase03.png)

## 基础实例 ##

可以使用 --> 字符来定义连线, 并通过 : 字符来添加文本标签.

将以下内容保存为 [usecase04](./usecase/usecase04.pum):

```
@startuml

User -> (Start)
User --> (Use the application) : A small label

:Main Admin: ---> (Use the application) : This is\nyet another\nlabel

@enduml
```

生成的效果图如下:

![usecase04.png](./usecase/usecase04.png)

## 扩展 ##

如果一个参与者是扩展自另一个参与者, 可以使用 <|-- 来定义.

将以下内容保存为 [usecase05](./usecase/usecase05.pum):

```
@startuml

:Main Admin: as Admin
(Use the application) as (Use)

User <|-- Admin
(Start) <|-- (Use)

@enduml
```

生成的效果图如下:

![usecase05.png](./usecase/usecase05.png)

## 注解 ##

可以使用 note left of, note right of, note top of, note bottom of 等关键字来定义一个关联到元素的注解.
注解也可以使用 note 关键字来定义, 通过 .. 等符号来关联到元素.

将以下内容保存为 [usecase06](./usecase/usecase06.pum):

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

![usecase06.png](./usecase/usecase06.png)

## 模板 ##

可以使用 << 和 >> 符号在参与者旁边定义模板数据.

将以下内容保存为 [usecase07](./usecase/usecase07.pum):

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

![usecase07.png](./usecase/usecase07.png)

## 修改箭头方向 ##

默认的, 使用 -- 或 .. 符号定义的箭头方向是竖直的, 也可以使用 - 或 . 符号来定义水平的箭头. 也可以使用 < 来修改反转箭头的连接方向, 也可以使用 left, right, up 和 down 等关键字来定义方向, 可以只使用关键字的一个或二个字母.

一般来说, 应该尽量避免使用这个特性, 因为 graphviz 可以自动的做好这种方向调整.

将以下内容保存为 [usecase08](./usecase/usecase08.pum):

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

![usecase08.png](./usecase/usecase08.png)

## 布局方向 ##

默认的画布布局方向是从上到下, 关键字为 top to bottom, 可以使用 left to right 关键字来将布局方向修改为从左到右.

将以下内容保存为 [usecase09](./usecase/usecase09.pum):

```
@startuml

/' 
 ' 'default
 ' top to bottom direction
 '/

left to right direction
user1 --> (Usecase 1)
user2 --> (Usecase 2)

@enduml
```

生成的效果图如下:

![usecase09.png](./usecase/usecase09.png)

## Skinparam ##

可以使用 skinparam 命令来修改颜色和字体, 使用方式包括以下几种:

- 在图形的定义中
- 在一个包含文件中
- 在一个配置文件中

将以下内容保存为 [usecase10](./usecase/usecase10.pum):

```
@startuml

skinparam handwritten true

skinparam usecase {
BackgroundColor DarkSeaGreen
BorderColor DarkSlateGray

BackgroundColor<< Main >> YellowGreen
BorderColor<< Main >> YellowGreen

ArrowColor Olive
ActorBorderColor black
ActorFontName Courier

ActorBackgroundColor<< Human >> Gold
}

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

![usecase10.png](./usecase/usecase10.png)

## 完整实例 ##

将以下内容保存为 [usecase11](./usecase/usecase11.pum):

```
@startuml

left to right direction
skinparam packageStyle rectangle

actor customer
actor clerk

rectangle checkout {
customer -- (checkout)
(checkout) .> (payment) : include
(help) .> (checkout) : extends
(checkout) -- clerk
}

@enduml
```

生成的效果图如下:

![usecase11.png](./usecase/usecase11.png)
