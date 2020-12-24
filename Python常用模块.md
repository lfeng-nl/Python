# Python 常用模块

## 1.正则表达式

| 符号           | 匹配                        | 符号        | 匹配                              |
| -------------- | --------------------------- | ----------- | --------------------------------- |
| `\d`           | 匹配一个数字                | `\D`        | 匹配一个非数字                    |
| `\s`           | 匹配空白字符                | `\S`        | 匹配非空白字符                    |
| `\w`           | 字母数字字符                | `\W`        | n-m 个字符                        |
| `*`            | 匹配前一个字符 0 次或无限次 | `+`         | 匹配前一个字符 1 次或无限次       |
| `?`            | 匹配前一个字符 0 次或 1 次  | `{m}/{m,n}` | 匹配前一个字符 m 次或 m 到 n 次   |
| `[...]`        | 匹配字符集中的任何一个字符  | `.`         | 匹配任意字符（除了\n）            |
| `^`            | 匹配字符必须在开头          | `$`         | 匹配字符必须在结尾                |
| `\A`           | 匹配字符串必须在开头        | `\Z`        | 匹配字符串必须在结尾              |
| `(ab)`         | 括号中表达式作为分组        | `\<n>`      | 引用标号为 n 的分组匹配到的字符串 |
| `(?P<name>..)` | python 中，命名分组为 name  | `(?P=name)` | python 中引用 name 分组           |
|                |                             |             |                                   |

- `re`模块中的`match`方法可用于判断正则表达式是否匹配成功；
  - 成功返回一个`match`对象；
  - 失败返回`none`；

## 2.collections

### 1.namedtuple

> 通过 namedtuple 工厂类创建一个类, 给元组的每个元素增加了`.属性` 取值的方式;

```python
Point = namedtuple('Point', ['x', 'y'])
p0 = Point(1,2) # p0.x = 1, p0.y = 2
p1 = Point(x=3, y=4) # p1.x = 3, p1.y = 4
x, y = p0
# ...
```

### 2.defaultdict

> 传入一个可调用对象; 取值时如果 key 不存在则==调用传入的可调用对象进行赋值并返回==; 有点类似`dict`对象的 `setdefault`的功能;

- `dict = defaultdict(factory_function)`:

### 3.deque 双端队列

- 线程安全, 相对于`list`, 优化了定长操作和`pop, insert`的开销.
- 扩展:
    - `queue`: 实现了多生产者, 多消费者队列, 适用于消息再多线程间安全交换. 可以使用阻塞.
    - `multiprocessing.Queue`: 一个使用管道(或者是`socket`)和少量锁和信号量实现的共享队列, 可以用于多进程间的通信. 类似`queue`.

### 4.ChainMap

> 将多个可迭代对象整合到一起形成一个新的可迭代对象, 重复的项或 key 仅保留首个;

### 5.`OrderedDict`有序字典

> 记录插入顺序, 可以使用`move_to_end()`移动到头部,尾部, 或者`popitem()`, 删除头部和尾部元素

- `move_to_end(key, last=True)`: 将现有 key 移动到有序字典的任一端,`last=Flase`移动到头;
- `popitem(last=True)`: 移除并返回一个`(key, value)`键值对, 默认移除头部元素;

## 3.itertools

### 1.chain()

- 将可迭代对象串联,形成一个更大的迭代器;

## 4.`contextlib`

> 此模块为涉及 `with`语句的常见任务提供了实用的程序。
>
> 资源管理:
>
> 1.`try...finally...`, 使用完毕关闭资源;
>
> 2.`with...as: pass` : 底层通过`__enter__(), __exit__()`方法实现;

### 1.`contextmanager`

- 装饰器, 将生成器转换为一个上下文管理器;

- `yield`前的代码在`with`调用的时候执行, `yield` 的值作为 `with`接收到的数据, `yield`后的数据在`with`块执行完毕时执行;

  - ```python
    from contextlib import contextmanager

    @contextmanager
    def managed_resource(*args, **kwds):
        # 获取资源
        resource = acquire_resource(*args, **kwds)
        try:
            yield resource
        finally:
            # 释放资源
            release_resource(resource)

    >>> with managed_resource() as resource:
    ...     # 在代码块结束, 资源被释放, 即使发生异常
    ```

### 2.`closing`

- 返回一个上下文管理器, 该管理器在块完成时关闭事务;

- ```python
  from contextlib import closing

  # 在代码块结束, 自动调用 f.close() 方法, 释放资源, 而无需关系是否发生异常
  with closing(<some-module>.open(xxx)) as f:
      pass

  ```

## 5.heapq

> 堆队列算法, python 提供的是最小堆, 方便取出最小值, 使用 list 实现;

- `heapq.heappush(heap,item)`: 将值加入堆中;
- `heapq.heappop(heaap)`: 弹出并返回最小元素;
- `heapq.heapify(x)`: 将 list 原地转换为堆;

- 用法:

  ```python
  heap = []            # creates an empty heap
  heapq.heappush(heap, item) # pushes a new item on the heap
  item = heapq.heappop(heap) # pops the smallest item from the heap
  item = heap[0]       # smallest item on the heap without popping it
  heapq.heapify(x)           # transforms list into a heap, in-place, in linear time
  item = heapq.heapreplace(heap, item) # pops and returns smallest item, and adds new item; the heap size is unchanged
  ```

## 6.functools

> 调整或扩展函数和`callable`对象

- `functools.partial(func, *args, **kwargs)`: 偏函数, 基于 func 生成新函数, 固定某些参数, 从而生成一个新的函数;

## 7.bisect

> 适用于单调递增数列.

- `bisect.bisect_left(q, x)`: 返回插入位置, 使得左侧均`< x`, 右侧`>=x`

- `bisect.bisect(q, x), 等同于 bisect.bisect_right(q, x)`: 返回插入位置, 使得左侧均`<=x`, 右侧`>x`