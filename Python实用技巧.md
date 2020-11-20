# Python使用技巧

- `locals()` ：返回一个字典，包含了函数执行到该时间点时所有定义的一切变量，字典形似为，变量名称和值对应；在 Django 模版导入上下文时可能有用；(会比较大)

- 由`d = {True:'1', 1:'2', 1.0:'3'} d[True]=?`引出的问题：

  - 答案为`'3'`，`True, 1, 1.0`为相同的键值，后面的会覆盖前面的；
  - 字典判断为相同键值的条件：1.值是否相同（ `__eq__()`方法），2.哈希值是否相同（`__hash__()`方法返回相同值）；

- 字典类型加双\*\*号，可以转换为关键字参数；

  - ```python
      d = {'a':1, 'b':2}
      test(**d) --> test(a=1, b=2)
    ```

- `enumerate()`：返回一个`enumerate`对象，使用`__next__()`方法返回一个包含计数的元组

  ```python
  >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
  >>> list(enumerate(seasons))
  [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
  >>> list(enumerate(seasons, start=1))
  [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
  ```

  - **可用于遍历时同时得到其下标**

    ```python
    for index, x in enumerate(list_xx):
    ```

- python中表示正负无穷
    - 正无穷
    
        - `float('inf')`
        - `from math import inf`
    
    - 负无穷: 
    
        - `-float('inf')`
    
        - `from math import inf`

- `eval 和 exec`区别:
    - `eval`: 执行表达式并求值返回.
    - `exec`: 可以执行复杂的代码块形式字符串, 但不会有返回值.

- python 设置递归深度:

    > Python 解释器堆栈设置有最大深度。此限制可防止无限递归导致的 C 堆栈溢出和 Python 崩溃。

    - `sys.getrecursionlimit()`: 获取递归限制值， 默认值3000.

    - `sys.setrecursionlimit(10000)`: 设置递归限制值.

- `Unicode `码位与字符的转换.
    - `ord()`: 将字符转换为`Unicode` 码点的整数.
    - `chr()`: 将`Unicode` 码点的整数转换为字符.