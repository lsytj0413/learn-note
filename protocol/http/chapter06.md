# 第6章: HTTP首部 #

## 6.1 HTTP报文首部 ##

![HTTP报文结构](./images/image06-01.png)

HTTP协议的请求和响应报文中必定包含 HTTP 首部.

### HTTP请求报文 ###

![请求报文](./images/image06-02.png)

### HTTP响应报文 ###

![响应报文](./images/image06-03.png)

## 6.2 HTTP首部字段 ##

### 6.2.1 HTTP首部字段传递重要信息 ###

使用首部字段是为了给浏览器和服务器提供报文主体大小, 所使用的语言和认证信息等内容.

### 6.2.2 HTTP首部字段结构 ###

HTTP 首部字段由字段名和字段值组成, 格式如下:

```
首部字段名: 字段值
```

单个首部字段可以有多个值.

### 6.2.3 4种HTTP首部字段类型 ###

#### 通用首部字段 ####

请求和响应都会使用的首部.

#### 请求首部字段 ####

请求使用的首部.

#### 响应首部字段 ####

响应使用的首部.

#### 实体首部字段 ####

针对请求和响应报文的实体部分使用的首部.

### 6.2.4 HTTP/1.1首部字段一览 ###

#### 通用首部字段 ####

| 首部字段名 | 说明 |
|:--|:--|


### 6.2.5 非HTTP/1.1首部字段 ###

### 6.2.6 end-to-end首部和hop-by-hop首部 ###

## 6.3 HTTP/1.1通用首部字段 ##

### 6.3.1 cache-control ###

### 6.3.2 connection ###

### 6.3.3 date ###

### 6.3.4 pragma ###

### 6.3.5 trailer ###

### 6.3.6 transfer-encoding ###

### 6.3.7 upgrade ###

### 6.3.8 via ###

### 6.3.9 warning ###

## 6.4 请求首部字段 ##

### 6.4.1 accept ###

### 6.4.2 accept-charset ###

### 6.4.3 accept-encoding ###

### 6.4.4 accept-language ###

### 6.4.5 authorization ###

### 6.4.6 expect ###

### 6.4.7 from ###

### 6.4.8 host ###

### 6.4.9 if-match ###

### 6.4.10 if-modified-since ###

### 6.4.11 if-none-match ###

### 6.4.12 if-range ###

### 6.4.13 if-unmodified-since ###

### 6.4.14 max-forwards ###

### 6.4.15 proxy-authorization ###

### 6.4.16 range ###

### 6.4.17 referer ###

### 6.4.18 te ###

### 6.4.19 user-agent ###

## 6.5 响应首部字段 ##

### 6.5.1 accept-ranges ###

### 6.5.2 age ###

### 6.5.3 etag ###

### 6.5.4 location ###

### 6.5.5 proxy-authenticate ###

### 6.5.6 retry-after ###

### 6.5.7 server ###

### 6.5.8 vary ###

### 6.5.9 www-authenticate ###

## 6.6 实体首部字段 ##

### 6.6.1 allow ###

### 6.6.2 content-encoding ###

### 6.6.3 content-language ###

### 6.6.4 content-length ###

### 6.6.5 content-location ###

### 6.6.6 content-md5 ###

### 6.6.7 content-range ###

### 6.6.8 content-type ###

### 6.6.9 expires ###

### 6.6.10 last-modified ###

## 6.7 为Cookie服务的首部字段 ##

### 6.7.1 set-cookie ###

### 6.7.2 cookie ###

## 6.8 其他首部字段 ##

### 6.8.1 x-frame-options ###

### 6.8.2 x-xss-protection ###

### 6.8.3 dnt ###

### 6.8.4 p3p ###

