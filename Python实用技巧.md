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
    - 正无穷: `float('inf')`
    - 负无穷: `-float('inf')`

