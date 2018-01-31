本文用于记录python知识点
##1.数据类型
- 整数
- 浮点数
- 字符串
- 布尔
- 空值
- list
- tuple
- dict
- set
- 序列：主要功能是`in`和`not in`表达式和索引操作；
- ​

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

- 关键字参数

- `*param`：从此处开始直到结束的所有位置参数（Positional Arguments）都将被收集并汇聚成为一个成为"param"的元组；

- 命名关键字参数`**param` ：从此处开始直到结束的所有的==关键字参数==都将被收集并汇集为一个名为"param"的字典；

  ```python
  def f(**kw):
    print(kw)
   
  f(test1=1, test2=2)			# 输出：{‘test1’:1， ‘test2':2}
  # 或者
  d = {'test1':1, 'test2':2}
  f(**d)						# 输出：{‘test1’:1， ‘test2':2}
  ```

## 3.高级特定
- 切片:
  - 切片操作会在开始处返回`start`，并在`end`前结束工作，也就是说，序列切片将包括起始位置；
- 迭代:
  - 能用`for`循环的对象都为可迭代的（`iterable`）；
  - ​
- 列表生成式:
  - `list(iterable)`函数，可以把一个可迭代对象转换为列表；
  - `[i for i in range(10)]`列表生成式，
- 生成器`generator`：通过边循环边计算生成数据，
  - 1.将列表生成式的`[]`换为`()`，如`a = (i for i in range(10))` a就是一个生成器；
  - 2.使用`yield ` ；
  - 可以通过`for`循环或`next()`取出生成器中的数据；
- 迭代器:
  - 可迭代对象`Iterable`：可以直接作用于`for`循环的对象，包括`list, tuple, dict, set, str, generator`等；可以用`isinstance(xxx, Iterable)`
  - 迭代器`Iterator`：可以被`next()`函数调用并不断返回下一个值的对象（生成器）；
  - `iter(iterable)`：将可迭代对象转变为迭代器；
- 特殊赋值:`a,b=b,a+b` 相当于`t=(b,a+b), a=t[0], b =t[1]`
- 迭代器和生成器：
  - 迭代器：任何实现了` __next__ `方法 （python2 是 next）的对象都可以称为迭代器，同列表的区别在于，构建迭代器的时候，不像列表把所有元素一次性加载到内存，而是以一种延迟计算方式返回元素。
  - 生成器：生成器本身还是一个迭代器，可以理解为方便构造的特殊迭代器。

## 4.函数式编程

-   一些点
    -   变量可以指向函数；
    -   函数名也是变量名；
-   高阶函数：函数可以接收另一个函数做为参数，还可以把函数作为结果返回。
-   `map()`
-   `filter(fuction, iterable)` 根据函数返回的`True或False`确定可迭代对象元素的去留（True，保留）；
-   `sorted(iterable, key, )`, 可以根据key指定的function排序，如`sorted(a, key=abs)`
-   函数作为返回值： 
-   匿名函数（lambda表达式）：只有一个表达式，返回值就是该表达式的结果。
-   装饰器：
-   匿名函数：

## 5.模块

-   模块：一个.py 文件就可以称为一个模块；
-   包：含有一些模块文件和一个`__init__.py`（用于表明这个文件夹是特别的）的文件夹，；
-   包可以嵌套；
-   模块分为直接运行和导入两种情况，当模块直接运行时会把一个特殊变量`__name__`置位`__main__`;
-   作用域：模块中的有些希望仅仅在模块中使用的变量和函数，可以通过前缀`_`实现；
    -   一般`__xxx__`类型名称的变量，是特殊变量，可以被直接引用；例如`__name__, __author__`
    -   类似`_xxx`类型名称的变量，都是非公开的，不应该被直接引用。（但是可见的，引用不引用需要使用者自觉遵守）

## 6.面向对象

- ```python
  class Student(objext):
    pass
  ```

  - 通过`class`关键字定义类；
  - 通过`( )` ：表明该类从哪继承；

- `__init__()`：类似C++中的构造函数；第一个参数必须是`self`；

- 访问控制：如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线`__`，python解释器会将其名称转换为`_类名__属性名`达到隐藏的目的；

- 在python中，变量名类似`__xxxx__`，双下划线开始，双下划线结束的，是特殊变量。特殊变量可以直接访问；

- 动态语言的“鸭子类型”， 它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那他就可以被看做是鸭子。

- 使用`type()`或`isinstance(obj, class_or_tuple)`判断类型；

- 使用`dir()`

- 实例属性和类属性：

  - 实例属性：给实例对象绑定属性的方法是通过实例变量，或者通过`self`变量；

  - 类属性：直接在`class`中定义属性，这种属性归类所有；

    ```python
    class Student(object):
      	def __init(self, name):
          	self.name = name			# 实例对象属性
        class = '302'					# 类属性
    ```

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
- `logging`模块记录错误信息；
- `raise`：抛出一个错误实例；
- ​