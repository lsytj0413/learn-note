# 类图 #

## 关系 ##

可以使用 <|--, *--, o-- 这三个符号来定义类之间的关系, 其中的 -- 可以替换为 .. 来实现虚线.

将以下内容保存为 [usecase01](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/class/class01.pum):

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

![class01.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/class/class01.png)

```

newpage

```

将以下内容保存为 [usecase02](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/class/class02.pum):

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

![class02.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/class/class02.png)

## 标签 ##

可以在类关系的箭头上使用标签文本, 并且对箭头两方的类定义文本. 也可以在标签的文本中使用 < 或 > 符号定义一个箭头.

将以下内容保存为 [usecase03](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/class/class03.pum):

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

![class03.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/class/class03.png)

## 方法 ##

可以在 : 符号之后定义方法, 如果有多个方法可以在类名称之后使用大括号包含的多行文本, 其中每一行文本包含一个方法.

将以下内容保存为 [usecase04](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/class/class04.pum):

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

![class04.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/class/class04.png)

## 访问限定 ##

可以使用 -(private), #(protected), ~(package private), +(public) 来定义类中属性的访问限定类型.

将以下内容保存为 [usecase05](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/class/class05.pum):

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

![class05.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/class/class05.png)
