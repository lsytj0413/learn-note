# LogBack日志配置 #

## 添加依赖 ##

```
		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>slf4j-api</artifactId>
			<version>1.7.7</version>
		</dependency>
		<dependency>
			<groupId>ch.qos.logback</groupId>
			<artifactId>logback-core</artifactId>
			<version>1.1.3</version>
		</dependency>
		<dependency>
			<groupId>ch.qos.logback</groupId>
			<artifactId>logback-access</artifactId>
			<version>1.1.3</version>
		</dependency>
		<dependency>
			<groupId>ch.qos.logback</groupId>
			<artifactId>logback-classic</artifactId>
			<version>1.1.3</version>
		</dependency>
```

## 日志配置 ##

在 src/main/resources目录下, 新建logback.xml, 配置如下:

```
<?xml version="1.0" encoding="UTF-8"?>
<configuration scan="true" scanPeriod="1 seconds">
	<contextListener class="ch.qos.logback.classic.jul.LevelChangePropagator">
		<resetJUL>true</resetJUL>
	</contextListener>

	<jmxConfigurator />
	<appender name="console" class="ch.qos.logback.core.ConsoleAppender">
		<encoder>
			<pattern>logbak: %d{HH:mm:ss.SSS} %logger{36} -%msg%n</pattern>
		</encoder>
	</appender>
	<logger name="org.springframework.web" level="DEBUG" />
	<root level="info">
		<appender-ref ref="console" />
	</root>
</configuration>
```
