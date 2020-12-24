# Python 函数

> Python 中, 函数也是对象. 函数对象本身是`function`类的实例.

## 1.函数

### 1.函数参数

- 位置参数: 按照定义从位置左到右进行匹配;
- 关键字参数: 需要通过参数名进行匹配;
- 函数定义时的位置参数, 在调用时可以通过关键字参数形式进行传递;
- 默认参数: 为没有传入值的参数定义参数值.
- 可变参数`*args, **kwargs`: 收集任意多的基于位置或关键字的参数.
  - `*args`: 收集所有未匹配的位置参数.
  - `**kwargs`: 收集所有未匹配的关键字参数.
- **仅限关键字参数**: 调用时只能通过关键字参数指定, 在有`*`的参数后面.

  ```python
  def f(a, *, b):
    return a, b

  # b 为_仅限关键字参数_, 必须通过关键字参数形式传递.
  f(1, b=2)
  ```

- 函数调用过程参数匹配的顺序:

  ```python
    def f(a, b, c=0, *args, **kwargs):
    # 1.通过位置分配位置参数;
    # 2.通过匹配变量名分配关键字参数;
    # 3.其他非关键字参数分配到*args元祖;
    # 4.其他关键字参数分配到**kwargs字典
    # 5.用默认值分配给在头部未得到分配的参数;
  ```

### 2.作用域

- `global`和`nonlocal`：

  - `global`：用来在函数或其他==局部作用域中使用全局变量==。但是如果不修改全局变量也可以不使用 global 关键字。

    ```python
    def test():
        global g_TEST
        g_TEST = 10
    ```

  - `nonlocal`：来在函数或其他作用域中使用==外层(非全局)变量==，如闭包中；

- 变量作用域：LEGB，名称查找顺序: L -> E -> G -> B
  - L：local，局部作用域；
  - E：enclosing，闭包作用域；
  - G：global，全局作用域；
  - B：builtins , 内置模块的名字空间；

### 3.函数注解

> Python3 提供的一种句法, 用于为函数声明中的参数和返回值附加元数据,声明参数和返回值类型,范围等信息:

```python
# text: str类型, max_len: int, 大于0, 默认值为 80, 返回值为str类型
def clip(text:str, max_len:'int > 0'=80) -> str:
    pass
```

- python 对注解仅仅是将其存储在函数`__annotations__`属性中, 并不做检查, 不做强制, 不做验证;

## 2.可调用对象

- 可调用对象: 可以使用调用运算符`()`的对象, 可以使用`callable()`函数判断. Python 中定义了 7 种可调用对象.
  - 用户定义的函数: `def`或`lambda`表达式创建.
  - 内置函数: 使用 C 语言实现的函数.
  - 内置方法: 使用 C 语言实现的方法, 如`dict.get()`
  - 方法: 类的定义体重定义的函数.
  - 类: 调用时会运行类的`__new__`方法创建一个实例, 然后运行`__init__`方法, 初始化实例.
  - 类的实例: 如果类定义了`__call__`方法, **它的实例可以作为函数调用**.
  - 生成器函数: 使用`yield`关键字的函数或方法. 返回的是生成器对象.

## 3.Python 函数式编程

> 函数式编程的三大特性: 1.immutable data 不可变数据：默认变量不可变; 2.first class function：使函数像变量一样来使用; 3.尾递归优化：优化递归，每次递归都会重用 stack; 关于[_尾调用和尾递归_](http://www.ruanyifeng.com/blog/2015/04/tail-call.html)

### 1.python 高阶函数

> 高阶函数: 接受函数为参数, 或者把函数作为结果返回的函数.

- `map(func, *iterables)`：将传入的函数作用到**可迭代对象**的元素，并把结果作为新的`Iterator`返回;
  - `map(lambda x : x*2, data_list)`
- `filter(fuction, Iterable)` 根据函数返回的`True/False`确定**可迭代对象元素的去留**(True，保留);
  - `filter(lambda x: x.endswith(','), data_list)`
- `all(iterable)`: 全为`True`, 结果才为`True`;
- `any(iterable)`: 只有有一个元素为`True`, 结果为`True`;
- `zip(iter1, [, iter2])`: 接收多个序列并将它们的元素组合成元组;
- `reduce()`: 把一个函数作用在一个序列上, 这个函数必须接收两个参数, `reduce`把结果继续和序列的下一个元素做累积计算,
- `sorted(iterable, key, )`, 可以根据 key 指定的 function 排序，如`sorted(a, key=abs)`
    - `key`:
        - 自定义函数, 接收元素, 返回参与排序的值.
        - `operator.itemgetter(x)`: 通过`[]`取每个排序元素的指定`item`比较. 
        - `operator.attrgetter('xxx')`: 使用每个排序元素的指定属性进行排序. 
        - `operator.methodcaller('xxx')`: 使用每个排序元素的指定方法进行排序.
    - 旧式的排序:
        - `functolls.cmp_to_key`:  `key=cmp_to_key(lambda x, y: return x < y)`

### 2.匿名函数（lambda 表达式）

- 匿名函数（lambda 表达式）：只有一个表达式，返回值就是该表达式的结果。`lambda x，y: x*y`,分号前为函数参数，分号后表达式为函数返回值；

- Python 中的匿名函数本身比较弱. 使用较少, 本身只是`def`的语法糖.

### 3.支持函数式编程的包

- `operator`: 可以导出一些运算符函数, 以便在函数式编程中使用,例如`operator.mul(a, b) === a*b`
- `functools`: 用于增强函数功能;
  - `functools.partial`: 基于一个函数创建一个新的可调用对象, 把原函数的某些参数固定.

## 4.单一调度泛型函数

> 泛型函数: 由多个函数组成, 为不同的类型实现相同的操作.
>
> 在调度期间应使用那些实现由调度算法确定. 当根据单个参数的类型选择实现时, 称为单一调度.
>
> [参考](https://www.python.org/dev/peps/pep-0443/)

- Python代码的常见反模式时检查接收的参数的类型, 以便决定如何处理对象.
  
- *anti-pattern 反面模式 在实践中经常出现但又低效或是有待优化的设计模式*
  
- 使用`@singledispatch`修饰, 可以定义泛型函数.
  - 通过`register()`, 注册不同类型的函数实现
  - 未注册类型会调用原有定义执行

  ```python
  from functools import singledispatch
  @singledispatch
  def fun(arg):
    print(arg)

  @fun.register(int)
  def _(arg):
    pass

  @fun.register(list)
  def _(arg):
    pass
  
  def str_fun(arg):
    pass

  fun.register(str, ftr_fun)
  ```

## 5.常用内置函数

- `ord`: 返回单个`Unicode`字符对应的值(兼容ASCII)
- `hex()`: 将整数转换为以`0x`为前缀的字符串.

