# Python 装饰器

## 1.闭包

> 闭包指延伸了作用域的函数, 即, 在函数体中引用, 但是不在函数体内定义的非全局变量.
>
> 自由变量(free variable): 指未在本地作用域中绑定的变量.

### 1.C 语言中函数的调用

- 通过栈帧实现.
  - 通过栈传递参数, 存储返回信息, 保存寄存器值.
  - 函数执行完毕, 从栈中弹出返回信息和寄存器值.

### 2.Python 中函数的调用

- 解释器抽象出`PyFrameObject`对象, 模拟栈帧.

### 3.闭包的实现

```python
def make_averager():
  series = []

  # 闭包
  # series 自由变量
  def averager(new_value):
    series.append(new_value)
    total = sum(series)
    return total/len(series)

  return averager
```

- `averager.__code__.co_freevars`: 存储所有自由变量的名称.
- `averager.__closure__`: 保存自由变量的绑定, 与名称顺序一致.

  - 当函数被调用时, 会将`__closure__`拷贝到**栈帧**中使用.
  - 由于都是引用传递, 资源不会被释放;
  - `cell`: 用于实现由多个作用域引用的变量.

- `nonlocal` 声明:
  - 把变量标记为自由变量.

## 2.装饰器

> 装饰器本质是一个返回可调用对象的可调用对象；
>
> 函数装饰器语法关键在于，`@decorator` ---> 相当于 `func = decorator(func)`;
>
> 也就是被装饰函数 = 装饰器内部的包装函数，包装函数执行额外代码后再调用原有被装饰函数；

### 1.普通装饰器实现

- 装饰函数

  ```python
  def decorator(F):
      return F

  @decorator
  def func():
      ...
  # 相当于 func = decorator(func)
  ```

- 装饰类, 可以用装饰器实现扩展类的功能

  ```python
  @decorator
  class C:
      ...
  # 等同于
  class C:
      C = dcecorator(C)
  ```

- 装饰函数编写:

  ```python
    import functools
    # log()返回一个内部函数；
    def log(func)：
      # 修改函数名为func, func.__name__ == func
      @functools.wraps(func)
        def wrapper(*args, **kw):
            print('call %s'%func.__name)  # --> 包装函数添加的内容
            return func(*args, **kw)
        return wrapper
    # 需要借助python的@语法
    @log
    def now():
        pass
    # @log 放到函数定义处，相当于执行了，now=log(now),
  ```

- python 内置装饰函数:
  - `property`: 将方法转换为属性;
  - `classmethod`: 类方法;
  - `staticmethod`: 静态方法;

### 2.参数化装饰器
