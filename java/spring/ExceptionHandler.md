# 错误处理 #

通过 @ControllerAdvice, 可以将对于控制器的全局配置放在同一个位置, 注解了 @Controller的类的方法可以使用 @ExceptionHandler, @InitBinder, @ModelAttribute注解到方法上.
这对所有注解了 @RequestMapping的控制器内的方法有效.

@ExceptionHandler: 用于处理控制器内的异常

@InitBinder: 用于设置WebDataBinder, 自动绑定前台请求参数到Model中

@ModelAttribute: 绑定键值对到Model中

## 异常处理 ##

### 定义全局异常处理 ###

```
package com.tuya;

import org.json.JSONException;
import org.json.JSONObject;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;


@ControllerAdvice
public class ExceptionHandlerAdvice {

		@ExceptionHandler(value = Exception.class)
		public ResponseEntity<Object> exception(Exception exception) throws JSONException {
			JSONObject jsonObject = new JSONObject();
			
			jsonObject.put("status", 999);
			jsonObject.put("msg", "未知错误");
			
			return new ResponseEntity<Object>(jsonObject.toString(4), HttpStatus.OK);
		}
}
```

### 添加pom配置 ###

```
		<dependency>
			<groupId>org.json</groupId>
			<artifactId>json</artifactId>
			<version>20160810</version>
		</dependency>
```
