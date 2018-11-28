## 1.pymysql

### 1.基本概念

- 游标cursor:  
  - 是一个存储在MySQL服务器上的数据库查询, 不是一条SELECT语句, 而是被该语句检索出来的结果集. 存储了游标之后, 应用程序可以根据需求滚动或浏览其中的数据;
  - 游标实际上是一种从包括多条数据记录的结果集中每次提取一条记录的机制。 
  - 游标是系统为用户开设的一个数据缓冲区，存放SQL语句的执行结果 
- 存储过程:  为以后使用而保存的一条或多条Mysql语句的集合.

### 2.使用过程

```python
db = pymysql.connect(xxx)
cursor = db.cursor()
cursor.execute('select xxx')
data = cursor.fetchall()
cursor.execute('updata')
db.commit()
cursor.close()
db.close()
```

## 2.collections

### 1.namedtuple

> 通过namedtuple工厂类创建一个类, 给元组的每个元素增加了`.属性` 取值的方式;

```python
Point = namedtuple('Point', ['x', 'y'])
p0 = Point(1,2) # p0.x = 1, p0.y = 2
p1 = Point(x=3, y=4) # p1.x = 3, p1.y = 4
x, y = p0
# ...
```

### 2.defaultdict

> 传入一个可调用对象; 取值时如果key不存在则==调用传入的可调用对象进行赋值并返回==;  有点类似`dict`对象的 `setdefault`的功能;

- `dict = defaultdict(factory_function)`: 

###  3.deque 双端队列

### 4.ChainMap 

> 将多个可迭代对象整合到一起形成一个新的可迭代对象, 重复的项或key仅保留首个;

## 3.threading

> 一些背景知识:
>
> 1. 守护进程: 在后台运行, 不受任何终端控制的进程.
>
> 2. 守护线程:  主线程不需要等待其执行完毕才退出,  例如后台的垃圾回收线程, 等待客户端连接的线程等, 
>
> 3. GIL 全局解释器锁: Python代码的执行环境是Python虚拟机进行控制, Python在主循环中同时只能有一个控制线程在执行, 尽管python解释器可以运行多个线程, 但是在任意给定时刻只有一个线程会被解释器执行, Python多线程执行步骤:
>
>    1. 设置GIL;
>    2. 切换线程;
>    3. 执行;
>    4. 切出线程;
>    5. 解锁GIL;
>    6. 重复步骤1;
>
>    所以, I/O密集型的Python程序要比计算密集型的代码能更好的利用多线程环境;

## 4.itertools

### 1.chain()

- 将可迭代对象串联,形成一个更大的迭代器;

## 5.contextlib 

> python资源管理: 
>
> 1.`try...finally...`, 使用完毕关闭资源;
>
> 2.`with...: pass` : 底层通过`__enter__(), __exit__()`方法实现;

- `@contextmanager`: 装饰一个生成器, `yield`前的代码在`with`调用的时候执行, `yield` 的值作为 `with`接收到的数据, `yield`后的数据在`with`块执行完毕时执行;

  - ```python
    @contextmanager
    def tag(name):
        print('<%s>' % name)
        yield 'hello world'
        print('</%s>' % name)
    
    with tag('h1') ad f:
        print(f) 
    # >>> <h1>
    # >>> hello
    # >>> </h1>
    ```

- `closing()`: 查看源码

## 6.SQLAlchemy

> ORM: Object Relational Mapping, 对象关系映射, 把关系数据库的表结构映射到对象上;
>
> SQLAlchemy 是知名的ORM工具之一

- 连接
  - `engine = create_engine('mysql://root:passwd@localhost:3306/test')` 
  - 参数结构`dialect[+driver]://user:password@host/dbname[?key=value..]` 

- 声明映射

  - 使用数据库前, 需要先声明表结构对应的类;

  - `Base = sqlalchemy.ext.declarative.declarative_base()`: `declarative_base`生成一个基类; 通过基类定义表对应的数据结构

    - ```python
      from sqlalchemy.ext.declarative import declarative_base
      from sqlalchemy import String, Integer, Column
      
      Base = declarative_base()
      class User(Base):
          __tablename__ = 'user'
          id = Column(Integer, primary_key=True)
          name = Column(String)
      ```

    - 

## 7.Pillow

