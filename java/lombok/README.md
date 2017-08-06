# Lombok #

(Lombok)[https://projectlombok.org/] 是一个可以通过简单的注解形式来简化消除一些必须有但显得很臃肿的 Java 代码的工具, 通过使用对应的注解, 可以在编译源码的时候生成对应的方法.

## 简介 ##

在开发过程中, 通常需要定义大量的 JavaBean, 然后实现对应的构造器, getter, setter, equals, hashCode, toString 等方法, 这是大量的样板代码. 而使用 lombok 来自动生成这些样板代码就是一种能够避免这种重复劳动的方式.

### 简单例子 ###

假设我们需要实现一个 Person 类如下(不使用 lombok):

```
package com.example.lombok;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Person {
	private String id;
	private String name;

	private Logger log = LoggerFactory.getLogger(Person.class);

	public Person() {
	}

	public Person(String id, String name, Logger log) {
		super();
		this.id = id;
		this.name = name;
		this.log = log;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

}
```

使用 lombok 之后的代码如下:


```
package com.example.lombok;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Data
@Slf4j
@NoArgsConstructor
@AllArgsConstructor
public class Person {
	private String id;
	private String name;
}
```

上面的两个类的效果是相同的, 使用 lombok 可以让代码简洁很多, 同时也避免了修改字段名称时忘记修改方法名称等低级错误.

## 安装 ##

### Build Tools ###

#### Maven ####

在 pom.xml 中添加如下内容即可:

```
<dependencies>
	<dependency>
		<groupId>org.projectlombok</groupId>
		<artifactId>lombok</artifactId>
		<version>1.16.18</version>
		<scope>provided</scope>
	</dependency>
</dependencies>
```

### IDE ###

