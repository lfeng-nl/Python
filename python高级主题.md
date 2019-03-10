# I Python高级主题

---

## 1.异步IO

### 1.协程 coroutine, [参考](https://docs.python.org/zh-cn/3.7/library/asyncio-task.html)

> 让原先需要用异步+回调方式写的代码可以用看似同步的方式写出来, 协程由于不需要线程切换开销,也不需要锁机制, 具有较高的效率.
>
> Python协程可以在多个位置上挂起和恢复执行. python最开始通过生成器[PEP342](https://www.python.org/dev/peps/pep-0342/)实现协程, 并通过[PEP380](https://www.python.org/dev/peps/pep-0380/)引入`yield from`进行增强; 后引入`PEP492`引入新的语法声明协程:`async def`, 协程函数可以包含`await, async for, sysnc with`关键字

==*python中协程最早是基于生成器实现,  使用`yield from`语句,对基于生成器的协程的支持 **已弃用** 并计划在 Python 3.10 中移除。*==

- 概念:

    - `await`表达式: 挂起`coroutine`的执行以等待一个`awaitable`对象, 只能在`coroutine function`内使用;`
    - `awaitable`: 可等待对象,  能够在`await`表达式中使用的对象.可以是`coroutine`或是具有`__await__()`方法的对象; 主要有三种类型:==协程,任务,Future==;
    - `async for`: 允许方便地对异步迭代器进行迭代.
    - `sysnc with`: 上下文管理器, 能够在`enter`和`exit`方法中暂停执行;
    - `asynchronous generator`: 异步生成器, 返回异步生成器迭代器,与`async def`定义的协程相似, 不同点在于包含`yield`表达式以产生可以在`async for`循环中使用的值;
    - `asynchronous generator iterator`: 异步生产器迭代器, 属于`asynchronous iterator`, 当使用`__anext__()`方法调用时会返回一个可等待对象来执行异步生成器函数的代码直到下一个`yield`表达式;

- 定义:`async def func()...`

    - 协程函数内部,能够使用`await, async for, aysnc with`标识符;
    - 协程内部使用`yield from`表达式将引发`SyntaxError`
    - 调用`coroutine function`返回一个`coroutine object`对象, 协程对象属于`awaitable`对象,;

- 协程的运行:

    - `asyncio.run(async_function())`: 运行传入的协程对象;
    - `await async_function()`: 等待一个协程执行; 
    - `task = asyncio.create_task(async_function())`: 将协程对象转换为`asyncio.Task()`对象;

- 任务: 可以并发执行协程:

    - `asyncio.create_task()` , python3.7以前可以用`asyncip.ensure_future()`函数;

    - ```python
        import asyncio
        async def nested():
            return 42
        
        async def main():
            task = asyncio.reeate_task(nested())
            await task
        ```

    - `cancel()`: 请求取消`Task`对象

    - `add_done_callback()`: 添加一个回调;

- `Future`对象:

    - 低层级的可等待对象, 表示一个异步操作的最终结果.

        ```python
        async def main():
            await function_that_returns_a_future_object()
        ```

- 并发运行任务:

    - ```python
        async def test(name, number):
            await asyncio.sleep(number)
            print('Task %s ok!' % name)
            
        async def main():
            await asyncio.gater(
            	test('A', 4),
                test('B', 3),
                test('C', 2),
                test('D', 1),
            )
        ```

- `asyncip.wait_for()`: 等待超时;

- 异步迭代器: 可以在其`__anext__`方法中调用异步代码, 由 [**PEP 492**](https://www.python.org/dev/peps/pep-0492) 引入。

    - 可以在`async for`语句中使用;
    - 实现了 `__aiter__()`和 `__anext__()` 方法的对象。`__anext__` 必须返回一个 `awaitable`

## 2.Python函数式编程

- 函数式编程的三大特性
    - immutable data 不可变数据：默认变量不可变
    - first class function：使函数像变量一样来使用
    - 尾递归优化：优化递归，每次递归都会重用stack
- 函数式编程的几个技术
    - `map`&`reduce`：
    - `pipeline`：把函数实例成一个一个的`action`，然后把`action`放到一个数组或是列表中，然后把数据传给这个`action list`；数据依次被各个函数所操作；
    - `recursing`递归：
    - `currying`把一个函数的多个参数分解成多个函数，然后把函数多层封装起来；
    - `higher order function`高阶函数，可以接收另一个函数做为参数，还可以把函数作为结果返回。
- `map(func, *iterables)`：将传入的函数以此作用到==可迭代对象==元素，并把结果作为新的==`Iterator`==返回；
- `filter(fuction, Iterable)` 根据函数返回的`True或False`确定==可迭代对象==元素的去留（True，保留）；
- `sorted(iterable, key, )`, 可以根据key指定的function排序，如`sorted(a, key=abs)`

# II Python常用模块

-----

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

### 

