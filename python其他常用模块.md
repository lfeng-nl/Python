## 1.pymysql

### 1.基本概念

- 游标cursor:  
  - 是一个存储在MySQL服务器上的数据库查询, 不是一条SELECT语句, 而是被该语句检索出来的结果集. 存储了游标之后, 应用程序可以根据需求滚动或浏览其中的数据;
  - 游标实际上是一种从包括多条数据记录的结果集中每次提取一条记录的机制。 
  - 游标是系统为用户开设的一个数据缓冲区，存放SQL语句的执行结果 

- 存储过程:  为以后使用而保存的一条或多条Mysql语句的集合.

## 2.collections

### 1.namedtuple

> 通过namedtuple工厂类创建一个类, 给每个index增加了.属性取值的方式;

```python
Point = namedtuple('Point', ['x', 'y'])
p0 = Point(1,2) # p0.x = 1, p0.y = 2
p1 = Point(x=3, y=4) # p1.x = 3, p1.y = 4
x, y = p0
# ...
```

### 2.defaultdict

> 传入一个可调用对象; 取值时如果key不存在则调用传入的可调用对象进行赋值并返回;  有点类似dict对象的 `setdefault`的功能;