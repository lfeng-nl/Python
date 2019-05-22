# I Python高级主题

---

## 1.asyncio

> 参考: [深入理解python异步编程](<https://mp.weixin.qq.com/s?__biz=MzIxMjY5NTE0MA==&mid=2247483720&idx=1&sn=f016c06ddd17765fd50b705fed64429c>) [深入理解Python异步编程](<https://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650370139&idx=1&sn=e4402260d852facb6f3d33ec20ed2be5&chksm=be9ccb0f89eb4219d986b1f15347f226a726f0da34aecbd593c0f61038e65f48d5334aeb2ca3&mpshare=1&scene=1&srcid=&pass_ticket=gLwNW%2BUgDzD3eMKuOQblqsLb05KdJis8nSFBCKEJffXeWuJIDpxEUQiUkGl74q2y#rd>)

### 1.基础概念

- 事件循环: asyncio应用的核心, 事件循环会运行异步任务和回调, 执行网络IO,运行子进程;

    ```python
    while True:
        # self._run_one() 调用当前准备好的回调
    	self._run_once()
    	if self._stopping:
    		break
    ```

    - `_scheduled`: 存放`TimeHeadle`, 堆结构;
    - `_ready`: 存放`Headle`, 堆结构, 每次执行`_run_once()`更新`_ready`, 然后遍历并调用`handle._run()`;
    - `self._process_events()`: 处理selector事件;

### 1.协程 coroutine, [参考](https://docs.python.org/zh-cn/3.7/library/asyncio-task.html)

> 让原先需要用异步+回调方式写的代码可以用看似同步的方式写出来, 协程由于不需要线程切换开销,也不需要锁机制, 具有较高的效率.
>
> Python协程可以在多个位置上挂起和恢复执行. python最开始通过生成器[PEP342](https://www.python.org/dev/peps/pep-0342/)实现协程, 并通过[PEP380](https://www.python.org/dev/peps/pep-0380/)引入`yield from`进行增强; 后引入`PEP492`引入新的语法声明协程:`async def`, 协程函数可以包含`await, async for, sysnc with`关键字

==*python中协程最早是基于生成器实现,  使用`yield from`语句,对基于生成器的协程的支持 **已弃用** 并计划在 Python 3.10 中移除。*==

- 概念:

    - 协程, 任务, Future: 
        - 协程: 通过`async/await`语法进行声明的;
        - 任务: 用来在事件循环中运行协程;
        - Future:
    - `awaitable`: 可等待对象,  能够在`await`表达式中使用的对象.是具有`__await__()`方法的对象; 主要有三种类型:==协程, 任务, Future==;
    - ==事件循环==: 利用`select, poll, epoll`, 当资源可用时, 向应用代码发出必要的调用;
    - ==Future==:  一个数据结构, 表示还未完成打工作结构;
    - ==Task==: 是Future的一个子类, 任务所需资源可用时, 事件循环会调度任务;
    - `await`表达式: 挂起`coroutine`的执行以等待一个`awaitable`对象, 只能在`coroutine function`内使用;`
    - 
    - `async for`: 允许方便地对异步迭代器进行迭代.
    - `sysnc with`: 上下文管理器, 能够在`enter`和`exit`方法中暂停执行;
    - `asynchronous generator`: 异步生成器, 返回异步生成器迭代器,与`async def`定义的协程相似, 不同点在于包含`yield`表达式以产生可以在`async for`循环中使用的值;
    - `asynchronous generator iterator`: 异步生产器迭代器, 属于`asynchronous iterator`, 当使用`__anext__()`方法调用时会返回一个可等待对象来执行异步生成器函数的代码直到下一个`yield`表达式;

- 协程的定义:`async def func()...`

    - 协程函数内部,能够使用`await, async for, aysnc with`标识符;
    - 协程内部使用`yield from`表达式将引发`SyntaxError`
    - 调用`coroutine function`返回一个`coroutine object`对象, 协程对象属于`awaitable`对;

- 协程的运行:

    - `asyncio.run(async_function())`: 运行传入的协程对象;
    - `await async_function()`: 等待一个协程执行; 
    - `task = asyncio.create_task(async_function())`: 将协程对象转换为`asyncio.Task()`对象;

- 任务: 可以并发执行协程:

    - `asyncio.create_task()` , python3.7加入, python3.7以前可以用`asyncip.ensure_future()`函数;

    - ```python
        import asyncio
        async def nested():
            return 42
        
        async def main():
            task = asyncio.create_task(nested())
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

> 函数式编程的三大特性: 1.immutable data 不可变数据：默认变量不可变; 2.first class function：使函数像变量一样来使用; 3.尾递归优化：优化递归，每次递归都会重用stack;  关于[*尾调用和尾递归*](http://www.ruanyifeng.com/blog/2015/04/tail-call.html)

### 1.函数注解

- Python3提供的一种句法, 用于为函数声明中的参数和返回值附加元数据,声明参数和返回值类型,范围等信息:

  ```python
  # text: str类型, max_len: int, 大于0, 默认值为 80, 返回值为str类型
  def clip(text:str, max_len:'int > 0'=80) -> str:
      pass
  ```

- python对注解仅仅是将其存储在函数`__annotations__`属性中, 并不做检查, 不做强制, 不做验证;

### 2.python高阶函数

- `map(func, *iterables)`：将传入的函数以此作用到==可迭代对象==元素，并把结果作为新的==`Iterator`==返回；
- `reduce()`: 把一个函数作用在一个序列上, 这个函数必须接收两个参数, `reduce`把结果继续和序列的下一个元素做累积计算,
- `filter(fuction, Iterable)` 根据函数返回的`True或False`确定==可迭代对象==元素的去留（True，保留）；
- `sorted(iterable, key, )`, 可以根据key指定的function排序，如`sorted(a, key=abs)`

### 3.支持函数式编程的包

- `operator`: 可以导出一些运算符函数, 以便在函数式编程中使用,例如`operator.mul(a, b) === a*b`
- `functools`: 用于增强函数功能;
  - `functools.partial`: 基于一个函数创建一个新的可调用对象, 把原函数的某些参数固定.

### 4.装饰器

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
> 2.`with...as: pass` : 底层通过`__enter__(), __exit__()`方法实现;

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

## 8.Celery

> Celery是python语言实现的分布式队列服务, Celery用消息通信, 通常使用中间人(Broker)在客户端和职程间斡旋, 客户端向消息队列添加消息,之后中间人把消息派送给职程.
>
> [参考1](<https://blog.csdn.net/weixin_40475396/article/details/80439781>), 

### 1.概念

> Celery实例以app为例, 任务以add为例;

- **Application**: 一个`Celery`实例被称为一个应用`app`;
    - 定义的任务, 都会被添加到`app.tasks`中, 可以通过任务名称, 获取到需要执行的任务;
    - `app.conf`: 配置Celery的工作方式;
    - `app.on_init()`: 设置初始化时的回调;
- **Task**: 定义了调用任务时发生的事情,以及当work收到该消息时会发生什么.
    - 可以通过`app.task()`装饰器创建一个任务;
    - 每个任务都有不同的名称, 发送给`celery`的任务消息中会引用这个名称, 工作单元就是根据这个名称找到正确的执行函数;
    - `task()`装饰器可以传入参数,如`name`: 指定任务名称, `bing=True`: 该函数为任务的绑定方法, 可以接受`self`参数, 获取任务实例;
    - 推荐使用`模块名+函数名`作为Task名称;
    - `import`Task时, 名称可能因路径不同而变化, 导致与APP中记录不匹配;
    - `retry()`: 在遇到某些错误时重新执行, `bind`参数必须为`True`, 通过`self.retry()`重新执行;由认为携带的`max_retries`值确定最大尝试次数.
- **Logging**: `from celery.utils.log import get_task_logger`
- **Calling Tasks**: 调用任务的方式
    - `delay()`: 简单调用,`task.delay(...)`
    - `apply_async()`: 必须通过`(args=[arg1, arg2], kwargs={'kwarg1':'x'})`传递参数, 可以通过关键字参数实现特殊功能;
        - `link`: 执行完接着执行另一个任务, 并且, 父任务结果作为参数传递给子任务;
        - `countdown`: 延迟执行, 秒数;
        - `eta`: 不同于`countdown`在于, `eta`需要一个精确的日期和时间;
        - `expires`: 过期时间;
        - `retry`: 链接失败时是否需需要重试;
        - `retry_policy`: 重试策略;
        - `queue`: 路由到指定队列;
        - `immutable=True`: 回调时, 不带任何附加参数;
- **Signatures**: 描述单个任务调用的参数和执行选项, 
    - 创建签名: `add.s(), add.signature((xx), xxx=xx)`;
    - 使用任务的调用方式调用`.delay(), apply_async()`;
    - 使用`.si()`创建immutable签名, 相当于`immutable=True`;
    - 链式执行: `chain(s1, s2, s3)(), (s1|s2|s3)()`; 
    - 
- **Broker**: Celery中介于生产者和消费者之间的中间人. 一般采用RabbitMQ或Redis来做Broker;
- **Worker**: 任务消费者, 在后台执行队列中的任务;
    - 可以通过`celery --app=app worker -l info`启动 worker;
- 
    - 

### 2.开始

## 9.heapq

> 堆排序



# III Python代码风格

> [PEP8: Python代码样式指导](<https://www.python.org/dev/peps/pep-0008/>);
>
> 



## 1.代码检查工具

### 1.flake8 [doc](<http://flake8.pycqa.org/en/latest/>)

- 安装`pip install flake8`
- `flake8 file.py`
- 配置: 

### 2.pycodestyle [doc](<https://pycodestyle.readthedocs.io/en/latest/intro.html#id3>)

- 根据PEP8样式检查Python代码是否符合;

- 安装`pip install pycodestyle`
- `pycodestyle file.py`

### 3.Pylint [doc](<https://pylint.readthedocs.io/en/latest/>)

- 安装`pip install pylint`
- [错误参考](<http://pylint-messages.wikidot.com/all-messages>)

## 2.风格

### 1.命名风格

- 常量: 大写加下划线,`SQL_USER`
- 函数和方法: 小写加下划线`function_name`
- 私有元素: 双下环线开头;
- 参数: 小写加下划线;
- 类: 驼峰式命名;
- 模块和包: 都使用小写, 不带下划线;
- 命名指南:
    - 用`has`或`is`前缀命名布尔元素;
    - 用复数形式命名集合, 如`tables`;
    - 避免现有名称;

### 2.易错格式

- E128: 延续线下缩进视觉缩进, 该行字符太多时需要进行折叠:

  ```python
  a = test('abcdef', 'abcdef', 'abcdef', 'abcdef')
  # 括号内有内容, 缩进到括号
  a = test('abcdef',
           'abcdef', 'abcdef', 'abcdef')
  # 括号内无内容, 统一缩进
  a = test(
  	'abcdef', 'abcdef', 'abcdef', 'abcdef')
  ```

  

- E711: `if info is None:`或`if not info is None`: 跟`None`的比较应用`is`;

- 

