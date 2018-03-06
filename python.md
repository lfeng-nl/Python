本文用于记录python知识点
##1.基础

###1.数据类型

- 整数
- 浮点数
- 字符串
- 布尔：`True，False `
- 空值
- list
- tuple
- dict
- set
- 序列：主要功能是`in`和`not in`表达式和索引操作；

### 2.运算符

基本同C语言类似，存在特殊点；

-   `**`：幂运算符号；
-   `//`：取整除；
-   `/` ：精确除；
-   `<<,>>` ：左移右移，会保留符号位；
-   逻辑运算：`and, or, not`
-   `lambda表达式` ：

##2.函数
### 1.内置函数
- abs()
- max()
- int()
- float()
- str()
- bool()
### 2.定义函数
- def

- pass

- 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数；例如：
   ```python
    def f2(a, b, c=0, *, d, **kw):
   ```

- 关键字参数

- `*param`：从此处开始直到结束的所有位置参数（Positional Arguments）都将被收集并汇聚成为一个成为`param`的==元组==；例如

  - ```python
    def test(a, *b):
        print(a)
        print(b)
        
    test(1,2,3,4)
    >> 输出：1
            (2,3,4)
    ```

- 命名关键字参数`**param` ：从此处开始直到结束的所有的==关键字参数==都将被收集并汇集为一个名为`param`的==字典==；例如：

  - ```python
    def test(a, **b):
        
    ```

  - ​

  ```python
  def f(**kw):
    print(kw)
   
  f(test1=1, test2=2)			# 输出：{‘test1’:1， ‘test2':2}
  # 或者
  d = {'test1':1, 'test2':2}
  f(**d)						# 输出：{‘test1’:1， ‘test2':2}
  ```

## 3.高级特定
###1.迭代器

-   可迭代
    -   可迭代对象`collections.Iterable`：可以直接作用于`for`循环的对象，包括`list, tuple, dict, set, str, generator`等；可以用`isinstance(xxx, collections.Iterable)` 判断是否可迭代；
    -   可迭代对象需要实现`__iter__()` 方法，并返回一个迭代器；
-   迭代器 
    -   迭代器`Iterator`：可以被`next()`函数调用并不断返回下一个值的对象（生成器）；任何实现了` __next__() `方法 （python2 是 next）的对象都可以称为迭代器；同列表的区别在于，构建迭代器的时候，不像列表把所有元素一次性加载到内存，而是以一种延迟计算方式返回元素。
    -   `iter(iterable)`：将可迭代对象转变为迭代器；
    -   迭代器需要实现`__next__（）`方法；
-   迭代器和生成器：
    -   迭代器：任何实现了` __next__（） `方法 （python2 是 next）的对象都可以称为迭代器，同列表的区别在于，构建迭代器的时候，不像列表把所有元素一次性加载到内存，而是以一种延迟计算方式返回元素。
    -   生成器：生成器本身还是一个迭代器，可以理解为方便构造的特殊迭代器。
-   `for`循环的实现：

### 2.序列

序列的两个主要特点是==索引操作符==和==切片操作符==，索引可以从一个序列中抓出一个特定项目；切片操作可以获取序列的一个切片，即一部分序列；

### 3.列表生成式

-   `list(iterable)`函数，可以把一个可迭代对象转换为列表；
-   `[i for i in range(10)]`列表生成式，

### 4.生成器

生成器`generator`：通过边循环边计算生成数据，

-   1.将列表生成式的`[]`换为`()`，如`a = (i for i in range(10))` a就是一个生成器；
-   2.使用`yield ` ；
-   可以通过`for`循环或`next()`取出生成器中的数据；

###5.其他

-   特殊赋值:`a,b=b,a+b` 相当于`t=(b,a+b), a=t[0], b =t[1]`
-   切片:
    -   切片操作会在开始处返回`start`，并在`end`前结束工作，也就是说，序列切片将包括起始位置；

## 4.函数式编程

-   函数式编程的三大特性

    -   immutable data 不可变数据：默认变量不可变
    -   first class function：使函数像变量一样来使用
    -   尾递归优化：优化递归，每次递归都会重用stack

-   函数式编程的几个技术

    -   `map`&`reduce`：
    -   `pipeline`：把函数实例成一个一个的`action`，然后把`action`放到一个数组或是列表中，然后把数据传给这个`action list`；数据依次被各个函数所操作；
    -   `recursing`递归：
    -   `currying`把一个函数的多个参数分解成多个函数，然后把函数多层封装起来；
    -   `higher order function`高阶函数，可以接收另一个函数做为参数，还可以把函数作为结果返回。

-   `map(func, *iterables)`：将传入的函数以此作用到==可迭代对象==元素，并把结果作为新的==`Iterator`==返回；

-   `filter(fuction, Iterable)` 根据函数返回的`True或False`确定==可迭代对象==元素的去留（True，保留）；

-   `sorted(iterable, key, )`, 可以根据key指定的function排序，如`sorted(a, key=abs)`

### 1.闭包

-   什么是闭包？为什么需要闭包？
    -   函数和函数内部能访问到的变量（环境）的总和，就是一个闭包。
    -   闭包常常用来「间接访问一个变量」。换句话说，「隐藏一个变量」。我们需要一个全局的变量，但是该变量又不能随意暴露出来，就需要闭包。

### 2.匿名函数（lambda表达式）

-   匿名函数（lambda表达式）：只有一个表达式，返回值就是该表达式的结果。`lambda x:x*x`,分号前为函数参数，分号后表达式为函数返回值；

### 3.装饰器

-   装饰器`decorator`：1.函数也是对象，可以给变量赋值，2.装饰器就是一个返回函数的高阶函数，对参数函数进行修饰、包裹（做一些额外的工作）；

    ```python
    import functools
    # log()返回一个内部函数；
    def log(func)：
    	# 修改函数名为func, func.__name__ == func
    	@functools.wraps(func)
        def wrapper(*args, **kw):
            print('call %s'%func.__name)  # --> 添加的内容
            return func(*args, **kw)
        return wrapper
    # 需要借助python的@语法
    @log
    def now():
        pass
    # @log 放到函数定义处，相当于执行了，now=log(now),

    ```

-   `@`语法糖syntactic sugar

    ```python
    @decorator
    def func():
        pass
    # 编译器会解释为
    func = decorator(func)
    ```

-   偏函数：`functools.partial(func, *args, **keywords)` ；帮助我们创建一个新的函数，

## 5.模块

-   模块：一个.py 文件就可以称为一个模块；
-   包：含有一些模块文件和一个`__init__.py`（用于表明这个文件夹是特别的）的文件夹，；
-   包可以嵌套；
-   模块分为直接运行和导入两种情况，当模块直接运行时会把一个特殊变量`__name__`置位`__main__`;
-   作用域：模块中的有些希望仅仅在模块中使用的变量和函数，可以通过前缀`_`实现；
    -   一般`__xxx__`类型名称的变量，是特殊变量，可以被直接引用；例如`__name__, __author__`
    -   类似`_xxx`类型名称的变量，都是非公开的，不应该被直接引用。（但是可见的，引用不引用需要使用者自觉遵守）

## 6.面向对象OOP

>   OOP：Object Oriented Programming

### 1.基本语法

-   类和实例：类是创建实例的模板，而实例是一个一个具体的对象；

-   Python中类的创建：

    -   ```python
        class Student(object):
          pass
        ```

    - 通过`class`关键字定义类；
    - 通过`(object)` ：表明继承关系；
    - 后面跟类的定义；

- `__init__()`：类似C++中的构造函数；第一个参数必须是`self`；

- 在类中定义的函数，第一个参数永远都是`self`；

- 访问控制：如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线`__`，python解释器会将其名称转换为`_类名__属性名`达到隐藏的目的；

- 在python中，变量名类似`__xxxx__`，双下划线开始，双下划线结束的，是特殊变量；特殊变量可以直接访问；

- 动态语言的“鸭子类型”， 它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那他就可以被看做是鸭子。

- 使用`type()`或`isinstance(obj, class_or_tuple)`判断类型；

- 使用`dir()`

- 实例属性和类属性：

  - 实例(对象)属性：给实例对象绑定属性的方法是通过实例变量，或者通过`self`变量；

  - 类属性：直接在`class`中定义属性，这种属性归类所有；

    ```python
    class Student(object):
      	def __init(self, name):
          	self.name = name			# 实例对象属性
        class = '302'					# 类属性
    ```

### 2.高级编程

-   创建类的示例后，可以给该实例绑定任何属性和方法，绑定的属性和方法只跟这个示例有关，跟类和其他实例无关；

    ```python
    s = Stuent()
    s.name = "lfeng"		# 任意绑定属性和方法 
    ```

-   限制实例的属性：通过`__slots__`变量，通过给该变量赋值一个元组，来规定允许绑定的属性名称；只对自身起作用，对通过继承的子类不起作用；

-   直接定义的属性无法做到数据类型，数据范围等的限制，一般需要依靠`get(), set()`函数的帮助；

    -   通过`@property`装饰器可以将一个方法转换为属性调用；
    -   `@property` 还会创建另一个装饰器`@xxx.setter`；负责把`xxx`方法变成属性赋值，不定义`setter`方法，则该属性就为只读的；

-   类中的特殊属性

    -   `__init__(self,...)`：对象被创建时调用；

    -   `__del__(self)`：在对象被销毁时调用；

    -   `__str__(self)`：在类被`print()`或`str()`调用时调用；

    -   `__iter__(self)` ：如果一个类想被用于`for...in `循环，就必须实现一个`__iter__()`方法；该方法返回一个迭代对象，然后，Python的`for`循环就会不断调用该迭代对象的`__next__()` 方法拿到循环的下一个值；

        ```python
        class T(object):
          def __init__(self, begin, end):
            self.__begin = begin
            self.__end = end
          def __iter__(self):
            return self
          def __next__(self):
            if self.__a > self.b:
              raise StopIteration()
            self.__a = self.__a + 1
            return self.__a
          
          # 测试
          a = T(10, 20)
          for i in a:
            print(i)		# 打印10-->20之间的整数
        ```

    -   `__getitem__(self, key)` ：使用`x[key]`索引操作符的时候调用;

    -   `__call__` ：实例本身可以做为一个方法，直接对实例进行调用；

- 枚举类：通过`Enum`类定义的类型；

  ```python
  from enum import Enum

  Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
  # 还可以精确的控制枚举类型
  from enum import Enum, unique

  @unique
  class Weekday(Enum):
      Sun = 0 # Sun的value被设定为0
      Mon = 1
      Tue = 2
      Wed = 3
      Thu = 4
      Fri = 5
      Sat = 6
  ```

  - `@unique` 装饰器可以帮助我们检查保证没有重复值；

- `type()` ：1.查看一个类型或变量类型，2.创建一个新类型；

  ```python
  # 要创建一个class类，type()函数以此传入3个参数：
  # 1.calss的名称
  # 2.继承的父类集合，（元组）
  # 3.calss的方法名称与函数绑定

  def fd(self, name="world"):
      print('Hello, %s.'%name)
      
  Hello = type("Hello", (object,), dict(hello=fn))
  ```

- `metaclass`元类：一般都是先定义类，然后创建实例。`metaclass`允许创建类或者修改类，

## 7.错误、调试和测试

> 在函数出错时，c往往会通过返回值表示是否发生错误，这导致正确结果和错误代码混和，一旦出错，还要一级一级上报；所以一般高级语言通常都内置了一套`try...except...finally...`的错误处理机制；

- `try`来运行代码，如果发生错误，则后续代码不会继续执行，直接跳转到错误处理，即`except`语句块；
- `except`：如果没有发生错误，则此段不会执行；发生错误，会被此段捕获；
- `finally` ：如果有此段，则最后一定会执行（发生不发生异常都会执行）；
- 错误种类：错误也是`class`，所有错误类型都继承自`BaseException`，捕获时不但可以捕获指定类型，还能将子类型同时捕获；
- `logging`：模块记录错误信息；
- `raise`：抛出一个错误实例；

### 1.调试

-   `assert 表达式` ：断言，如果表达式为真，继续执行；否则抛出`AssertionError`； python可以在运行时加入大O，`python3 -O xxxx` 关闭`assert`
-   `logging`：同`assert`相比，`logging`不会抛出异常，而且可以输出到文件；
    -   有`debug,info,warning,error`由低到高几个等级；`logging.debug()， logging.info() ...`
    -   可以通过`logging.basicConfig(level=logging.INFO)`设置等级；
-   `pdb` ：python调试工具，通过`python -m pdb xxx`启动；

### 2.文档测试

>   编写注释时，明确的写出函数的期望输入和输出，然后通过Python的文档测试模块`doctest` 可以直接提取注释中的代码并执行测试

```python
def test(x):
    # 文档测试内容
    '''
    >>> test(2)
    2
    >>> test(4)
    4
    '''
    return x

# 进行文档测试
if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

### 3.单元测试

>   "测试驱动开发 TDD"；单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。这种以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例，在将来修改的时候，可以极大程度地保证该模块行为的正确性；

-   编写单元测试，需要引入python自带的`unittest`模块；

    ```python
    # 导入单元测试模块
    import unittest

    #编写测试类，需要从 unittest.TestCase 继承
    class TestDict(unittest.TestCase):
    	# 每一个测试方法必须以test开头，类似`test_xxx()`形式命名
        def test_init(self):
            d = list(range(10))
            # 判断，是否相等，TestCase内置了许多测试类型
            self.assertEqual(d[0], 0)
            self.assertEqual(d[2], 2)
    ```

-   测试方式：

    -   1.把单元测试做为脚本运行

        ```python
         if name=='main':
            unittest.main()
        ```

    -   2.在命令行通过参数`-m unittest xxxx`直接运行;

    -   测试通过或打印`ok`；失败会返回`FAIL`和错误位置；

-   `setUp(), tearDown()`：会在每次测试开始和测试结束运行；

## 8.进程和线程

### 1.多进程

- `fork()`：通过`os.fork()`创建进程，同`fork()`一致，父进程中返回子进程ID，子进程返回0；

- `multiprocessing`：模块中的`Process`类来代表一个进程对象，

  ```python
  from multiprocessing import Process
  import os

  # 子进程要执行的代码
  def run_proc(name):
      print('Run child process %s (%s)...' % (name, os.getpid()))

  if __name__=='__main__':
      print('Parent process %s.' % os.getpid())
      p = Process(target=run_proc, args=('test',))
      print('Child process will start.')
      # start()方法启动（创建子进程，去执行指定函数）
      p.start()
      # join()方法等待子进程结束，类似wait()或线程中的join
      p.join()
      print('Child process end.')
  ```

  - `Pool()` ：用于创建大量的子进程；

- 进程间通信：`multiprocessing`中的`Queue, Pipes`等；

### 2.多线程

> `_thread`和`threading`，前者是低级模块，后者是高级模块，对前者的再封装。

- 使用`Thread()`绑定线程函数，用`start()`启动，用`join()`等待；
- 通过`Lock()`创建锁， 通过`acquire()`加锁，通过`release()`释放；
- GIL：Global Interpreter Lock，任何python线程执行前，必须先获取GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行；
- `threading.local()`：

## 9.其他

### 1.IO

-   IO操作面临异常情况，无法保证所有异常下，文件都得到关闭；可以使用`with`语句；

    -   ```python
        with open('/path/to/file', 'r') as f:
            print(f.read())
        ```

-   像`open()`函数返回的这种有个`read()`方法的对象，在Python中统称为 file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object 不要求从特定类继承，只要写个`read()`方法就行。

-   `open()` 可以指定打开文件的编码方式`encoding`，默认utf-8编码；

-   `b`：表示以二进制方式读写；

-   ！！== 调用`write() `写入文件时，并不会立刻写入，而是放入缓存中，等待空闲时写入；只有调用`close()`方法，才会立刻将未写入的数据写入磁盘；

### 2.文件操作

### 3.序列化

-   程序执行过程中，所有变量都是存放在内存中的，程序执行结束，变量就会消失；我们把变量从内存中变成可存储或传输的过程称之为序列化；可以借助`pickling`

-   写入：

    -   ```python
        import pickle
        d = dict(name='Bob', age=20, score=88)
        pickle.dumps(d)

        ```

-   读取：

    -   ```python
        f = open('dump.txt', 'wb')
        pickle.dump(d, f)
        f.close()

        ```

-   当然，最好的序列化为`XML`和`JSON`