# 类图 #

## 关系 ##

可以使用 <|--, *--, o-- 这三个符号来定义类之间的关系, 其中的 -- 可以替换为 .. 来实现虚线.

将以下内容保存为 [usecase01](./class/class01.pum):

```
@startuml

Class01 <|-- Class02
Class03 *-- Class04
Class05 o-- Class06
Class07 .. Class08
Class09 -- Class10

@enduml
```

生成的效果图如下:

![class01.png](./class/class01.png)

```

newpage

```

将以下内容保存为 [usecase02](./class/class02.pum):

```
@startuml

Class17 ..|> Class18
Class19 <--* Class20
Class21 #-- Class22
Class23 x-- Class24
Class25 }-- Class26
Class27 +-- Class28
Class29 ^-- Class30

@enduml
```

生成的效果图如下:

![class02.png](./class/class02.png)

## 标签 ##

可以在类关系的箭头上使用标签文本, 并且对箭头两方的类定义文本. 也可以在标签的文本中使用 < 或 > 符号定义一个箭头.

将以下内容保存为 [usecase03](./class/class03.pum):

```
@startuml

Class01 "1" *-- "many" Class02 : contains
Class03 o-- Class04 : aggregation
Class05 --> "1" Class06

Class Car

Driver - Car : drives >
Car *-- Wheel : have 4 >
Car -- Person : < owns

@enduml
```

生成的效果图如下:

![class03.png](./class/class03.png)

## 方法 ##

可以在 : 符号之后定义方法, 如果有多个方法可以在类名称之后使用大括号包含的多行文本, 其中每一行文本包含一个方法.

将以下内容保存为 [usecase04](./class/class04.pum):

```
@startuml

Object <|-- ArrayList

Object : equals()
ArrayList : Object[] elementData
ArrayList : size()

class Dummy {
String data
void methods()
}

class Flight {
flightNumber : Integer
departureTime : Date
}

@enduml
```

生成的效果图如下:

![class04.png](./class/class04.png)

## 访问限定 ##

可以使用 -(private), #(protected), ~(package private), +(public) 来定义类中属性的访问限定类型.

将以下内容保存为 [usecase05](./class/class05.pum):

```
@startuml

/' 使用下面的代码来隐藏访问限定的图标 '/
/' skinparam classAttributeIconSize 0 '/

class Dummy {
-field1
#field2
~method1()
+method2()
}

@enduml
```

生成的效果图如下:

![class05.png](./class/class05.png)

## 抽象和静态 ##

可以定义静态方法和抽象方法, 可以添加在行末和行尾.

将以下内容保存为 [usecase06](./class/class06.pum):

```
@startuml

class Dummy {
/' static=classifier '/
{static} String id
{abstract} void methods()
}

@enduml
```

生成的效果图如下:

![class06.png](./class/class06.png)

## 类体 ##

默认的, 类的方法和属性是会被 plantuml 分组, 但是你也可以使用 --, .., ==, __ 等符号进行手动分组.

将以下内容保存为 [usecase07](./class/class07.pum):

```
@startuml

class Foo1 {
You can use
several lines
..
as you want
and group
==
things together.
__
You can have as many groups
as you want
--
End of class
}
class User {
.. Simple Getter ..
+ getName ()
+ getAddress ()
.. Some setter ..
+ setName ()
__ private data __
int age
-- encrypted --
String password
}

@enduml
```

生成的效果图如下:

![class07.png](./class/class07.png)

## 模板信息 ##

可以在 class 关键字中定义一些模板信息, 通过 << 和 >> 符号. 可以通过 note left of, note right of, note top of, note bottom of, note left, note right, note top, note bottom 以及单独的 note 关键字来定义一些注解文本, 并通过 .. 符号关联到元素.

将以下内容保存为 [usecase08](./class/class08.pum):

```
@startuml

class Object << general >>
Object <|-- ArrayList

note top of Object : In java, every class\nextends this one.

note "This is a floating note" as N1
note "This note is connected\nto several objects." as N2
Object .. N2
N2 .. ArrayList

class Foo
note left: On last defined class

@enduml
```

生成的效果图如下:

![class08.png](./class/class08.png)

## 注解 ##

可以在注解文本中使用以下的 html 标签, 包括 \<b\>, \<u\>, \<i\>, \<s\>, \<del\>, \<strike\>, \<font color="#AAAAAA"\>, 
\<font color="colorName"\>, \<color:#AAAAAA\>, \<color:colorName\>, \<size:nn\>, \<img src="file"\> 及 \<img:file\>.

也可以在链接上使用注解, 使用 note left on link, note right on link, note top on link, note bottom on link 的关键字即可.

将以下内容保存为 [usecase09](./class/class09.pum):

```
@startuml

class Foo
note left: On last defined class

note top of Object
In java , <size :18>every </size > <u>class </u>
<b>extends </b>
<i>this </i> one.
end note

note as N1
This note is <u>also </u>
<b><color:royalBlue >on several </color >
<s>words </s> lines
And this is hosted by <img:../../img/chrome.png>
end note

class Dummy
Dummy --> Foo : A link
note on link #red: note that is red

Dummy --> Foo2 : Another link
note right on link #blue
this is my note on right link
and in blue
end note

@enduml
```

生成的效果图如下:

![class09.png](./class/class09.png)

## 抽象类和接口 ##

可以使用 abstract, abstract class 等关键字来定义抽象类, 同样的也可以使用 interface, annotation 和 enum 等关键字来定义对应的类型.

将以下内容保存为 [usecase10](./class/class10.pum):

```
@startuml

abstract class AbstractList
abstract AbstractCollection
interface List
interface Collection

List <|-- AbstractList
Collection <|-- AbstractCollection

Collection <|- List
AbstractCollection <|- AbstractList
AbstractList <|-- ArrayList

class ArrayList {
Object [] elementData
size ()
}

enum TimeUnit {
DAYS
HOURS
MINUTES
}

annotation SuppressWarnings

@enduml
```

生成的效果图如下:

![class10.png](./class/class10.png)


## non-letters ##

可以在类名的显示上使用 non-letters 字符串, 通过以下两种方式:

- 使用关键字
- 使用双引号包含文本

将以下内容保存为 [usecase11](./class/class11.pum):

```
@startuml

class "This is my class" as class1
class class2 as "It works this way too"

class2 *-- "foo/dummy" : use

@enduml
```

生成的效果图如下:

![class11.png](./class/class11.png)

## 隐藏方法或属性 ##

可以使用 hide empty members 命令来隐藏属性或方法, 如果没有属性和方法的话. 除了 empty members 还可以使用如下的命令:

- empty fields 或 empty attributes, 隐藏空的字段
- empty methods, 隐藏空的方法
- fields 或 attributes, 隐藏字段(即使字段存在)
- methods, 隐藏方法(即使存在)
- members, 隐藏字段和方法, 即使它们存在
- circle, 隐藏类名前的字符
- stereotype, 隐藏模板

也可以在 hide 或 show 关键字后使用以下命令:

- class
- interface
- enum
- <<foo1>>, 使用了 foo1模板的类
- 一个已存在的类名

可以使用多个 hide 或 show 命令.

将以下内容保存为 [usecase12](./class/class12.pum):

```
@startuml

class Dummy1 {
+myMethods()
}

class Dummy2 {
+hiddenMethod()
}

class Dummy3 <<Serializable>> {
String name
}

hide members
hide <<Serializable>> circle
show Dummy1 methods
show <<Serializable>> fields

@enduml
```

生成的效果图如下:

![class12.png](./class/class12.png)

## 泛型和特殊符号 ##

可以使用 < 和 > 字符来定义类中的泛型. 字符 C, I, E, A 是作为 class, interface, enum 和 abstract 等对象类型的标识, 用户也可以定义自己的标识字符, 通过在模板前增加一个小括号包含的字符和颜色.

将以下内容保存为 [usecase13](./class/class13.pum):

```
@startuml

class Foo<? extends Element> {
int size()
}

Foo *- Element

class System << (S,#FF7700) Singleton >>
class Date << (D,orchid) >>

@enduml
```

生成的效果图如下:

![class13.png](./class/class13.png)

## 包 ##

可以通过 package 关键字来定义一个包, 此时可以选择定义包的背景色(通过 HTML 颜色名称或颜色值). 包是可以嵌套的, 也可以定义包之间的联系.

将以下内容保存为 [usecase14](./class/class14.pum):

```
@startuml

package "Classic Collections" #DDDDDD {
Object <|-- ArrayList
}

package net.sourceforge.plantuml {
Object <|-- Demo1
Demo1 *-- Demo2
}

/' 定义包的外形 '/
/' skinparam packageStyle rectangle '/

package foo1.foo2 {
}
package foo1.foo2.foo3 {
class Object10
}
foo1.foo2 +-- foo1.foo2.foo3

@enduml
```

生成的效果图如下:

![class14.png](./class/class14.png)

## 包的风格 ##

可以对不同的包定义不同的显示风格.

将以下内容保存为 [usecase15](./class/class15.pum):

```
@startuml

scale 750 width

package foo1 <<Node>> {
class Class1
}

package foo2 <<Rectangle>> {
class Class2
}

package foo3 <<Folder>> {
class Class3
}

package foo4 <<Frame>> {
class Class4
}

package foo5 <<Cloud>> {
class Class5
}

package foo6 <<Database>> {
class Class6
}

@enduml
```

生成的效果图如下:

![class15.png](./class/class15.png)

## 名字空间 ##

可以使用 namespace 关键字来定义名字空间.

将以下内容保存为 [usecase16](./class/class16.pum):

```
@startuml

class BaseClass
namespace net.dummy #DDDDDD {
.BaseClass <|-- Person
Meeting o-- Person
.BaseClass <|- Meeting
}
namespace net.foo {
net.dummy.Person <|- Person
.BaseClass <|-- Person
net.dummy.Meeting o-- Person
}

BaseClass <|-- net.unused.Person

@enduml
```

生成的效果图如下:

![class16.png](./class/class16.png)

## 自动名字空间 ##

可以使用 set namespaceSeparator 命令来定义自动名字空间的分隔符.

将以下内容保存为 [usecase17](./class/class17.pum):

```
@startuml

set namespaceSeparator ::
/' 关闭自动名字空间 '/
/' set namespaceSeparator none '/

class X1::X2::foo {
some info
}

@enduml
```

生成的效果图如下:

![class17.png](./class/class17.png)

## lollipop interface ##

可以使用以下命令定义 lollipop interface:

- bar ()- foo
- bar ()-- foo
- foo -() bar

将以下内容保存为 [usecase18](./class/class18.pum):

```
@startuml

class foo
bar ()- foo

@enduml
```

生成的效果图如下:

![class18.png](./class/class18.png)

## 修改箭头方向 ##

默认的, 使用 -- 的箭头方向是水平的, 可以使用单个 - 符号或者 . 符号来修改为垂直方向. 也可以使用 left, right, up 和 down 等关键字来定义方向, 可以只使用关键字的一个或二个字母.

将以下内容保存为 [usecase19](./class/class19.pum):

```
@startuml

Room o- Student
Room *-- Chair

Student1 -o Room1
Chair1 --* Room1

foo -left-> dummyLeft
foo -right-> dummyRight
foo -up-> dummyUp
foo -down-> dummyDown

@enduml
```

生成的效果图如下:

![class19.png](./class/class19.png)

## 关联类 ##

将以下内容保存为 [usecase20](./class/class20.pum):

```
@startuml

class Student {
Name
}

Student "0..*" - "1..*" Course

(Student, Course) .. Enrollment

class Enrollment {
drop ()
cancel ()
}

class Student1 {
Name
}

Student1 "0..*" -- "1..*" Course1

(Student1, Course1) . Enrollment1

class Enrollment1 {
drop ()
cancel ()
}

@enduml
```

生成的效果图如下:

![class20.png](./class/class20.png)

## Skinparam ##

可以使用 skinparam 命令来修改颜色和字体, 使用方式包括以下几种:

- 在图形的定义中
- 在一个包含文件中
- 在一个配置文件中

将以下内容保存为 [usecase21](./class/class21.pum):

```
@startuml

skinparam class {
BackgroundColor PaleGreen
ArrowColor SeaGreen
BorderColor SpringGreen
BackgroundColor<<Foo>> Wheat
BorderColor<<Foo>> Tomato
}

skinparam stereotypeCBackgroundColor YellowGreen
skinparam stereotypeCBackgroundColor <<Foo>> DimGray

Class01 <<Foo>>
Class03 <<Foo>>

Class01 "1" *-- "many" Class02 : contains
Class03 o-- Class04 : aggregation

@enduml
```

生成的效果图如下:

![class21.png](./class/class21.png)

## 渐变色 ##

可以通过以下的符号分割的两个颜色来定义渐变的背景色: |, /, \, -.

将以下内容保存为 [usecase22](./class/class22.pum):

```
@startuml

skinparam backgroundcolor AntiqueWhite/Gold
skinparam classBackgroundColor Wheat|CornflowerBlue

class Foo #red-green

note left of Foo #blue\9932CC
this is my
note on this class
end note

package example #GreenYellow/LightGoldenRodYellow {
class Dummy
}

@enduml
```

生成的效果图如下:

![class22.png](./class/class22.png)

## 布局 ##

可以通过 together 关键字来让对象分布在一起.

将以下内容保存为 [usecase23](./class/class23.pum):

```
@startuml

class Bar1
class Bar2

together {
class Together1
class Together2
class Together3
}

Together1 - Together2
Together2 - Together3
Together2 -[hidden]--> Bar1
Bar1 -[hidden]> Bar2

@enduml
```

生成的效果图如下:

![class23.png](./class/class23.png)

## 拆分文件 ##

可以通过 page (hpages)x(vpages) 命令将生成的图形拆分为不同的文件, 其中 hpages 表示水平数量, vpages 表示垂直数量.

将以下内容保存为[usecase24](./class/class24.pum):

```
@startuml

' Split into 4 pages

page 2x2
skinparam pageMargin 10
skinparam pageExternalColor gray
skinparam pageBorderColor black

class BaseClass
namespace net.dummy #DDDDDD {
.BaseClass <|-- Person
Meeting o-- Person
.BaseClass <|- Meeting
}

namespace net.foo {
net.dummy.Person <|- Person
.BaseClass <|-- Person
net.dummy.Meeting o-- Person
}

BaseClass <|-- net.unused.Person

@enduml
```
