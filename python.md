本文用于记录python知识点  


## 1.基础

### 1.数据类型

#### 1.数据类型基础

- 基本数据类型：`int, float, str, bool(True, False), None `
- 容器：`list, str, tuple, dict, set 等` 可以实现==`in`和`not in `==表达式和==索引==操作；

#### 2.str注意点：

- `s = r'\temp\spam'`：Raw字符串，注意，`\`不能出现在最后一位；
- `r_s = s[::-1]`：逆序；
- `s.replace('pa', 'xxx')`：替换；
- `s.endswith('span')`：判断结束字符；
- `s.startswith()`: 判断开始字符; 参数可以为`tuple`, 表示为其中之一;
- `','.join(s)`：用自身分割；
- `s.split(',')`：用字符分割，返回列表；
- `s * 2`：重复
- 字符串为不可变对象，禁止在原处修改！
- 字符串存在编码方式的问题，详见第9章：编码方式；

#### 3.`list`注意点：

- `list.append(object)`：附加单个元素到list的尾部；
- `list.extend([xx, xx])`：附加列表到元素尾部；--> 等同于  `list_a = list_a + list_b`
- `list.remove()`：移除第一非匹配到的元素；
- 列表是可变对象，可以原处修改；
- 遍历删除或添加列表元素：
  - ==直接遍历，当删除或增加列表元素时，列表长度发生变化，但遍历的长度不变。会产生问题！==
  - 推荐有此需求时，遍历列表的拷贝；

#### 4.字典 dict注意点

- `same_key in D`：键存在测试；
- `D.keys()`：-->所有键；
- `D.values()`：所有值；
- `D.items()`：键值对元组；
- `D.get('key', default=None)`：获取一个键的值，不存在不会抛出异常，返回默认值；
- ==字典是无序的，哈希表==；

#### 5.元组 tuple

- 元组不可变，没有list的修改之类的方法；

#### 6.文件

- 打开方式：`b`：可以处理二进制，`+`：同时为输入和输出打开，`r+、w+`：都是为读写打开，不同点`w+`当文件不存在时会创建，`w`也会创建；
- 文本文件，python会转为常规`str`字符串，自动执行Unicode编码；
- 二进制文件会表示为一个特殊的`bytes`字符串类型，

#### 7.其他

- None：表示为空，一个特殊的对象，类型为`Nonetype`，表示数据为空，对应的布尔值为False；



### 2.运算符和语句

基本同C语言类似，存在特殊点；

- 赋值：
  - 序列赋值：任何序列都可按位置赋值给变量；`  a, b = [1, 2], a, *b = [1,2,3]`;
  - 增强赋值语句：例如`a += 12, b += [1,2,3]`, python 中任何二元表达式运算符都有增强赋值语句；
  - 对于列表，增强赋值语句相当于`list_a.extend(list_b)`，实际也会转换为`extend`调用；
  - 特殊赋值:`a,b=b,a+b `，交换`a,b `的值； 

- `**`：幂运算符号；

- `//`：取整除；

- `/` ：精确除（即使能够整除得到的也是浮点数）；

- `<<,>>` ：左移右移，会保留符号位；

- 逻辑运算：`and, or, not`

- `lambda表达式` ：`a = lambda x: x**2`

- python条件判断：

    -   可以使用`10 < a < 20 `这种方式；

    -   ````
        if ...:
        	pass
        elif ...:
        	pass
        else:
        	pass
        ````


### 3.变量和对象

- ==变量==事实上是到==对象==内存空间的一个指针！
- ==变量==是一个系统表的元素，拥有指向对象连接空间。
- ==对象==是分配的一块内存，有足够的空间去表示他们所代表的值；
- 每一个==对象==都有两个标准的头部信息，一个是类型标识符，另一个是引用计数；
- `==`值比较，是否相同，
- `is`,精确比较，是否指向同一个对象；
- `isinstance(obj, class)`：对象是否是类的实例；
- `sys.getrefcount()`会返回引用计数；
- 类型的概念是存在于对象中，而不是变量名中；变量是通用的，只是在特定的时间点，简单的引用了一个特定的对象而已；
- 引用是一种关系，以内存中的指针的形式实现；

## 2.函数

### 1.内置函数
- `abs(), max(), int(), float(), str(), bool()`
### 2.定义函数
- 在Python中定义函数，可以用==必选参数、默认参数、可变参数、关键字参数和命名关键字参数==这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数；例如：
   ```python
    def f(a, b, c=0, *d, **kw):
   ```

- 可变参数：`*param`：

  - 用于函数定义：从此处开始直到结束的所有==位置参数==（Positional Arguments）都将被收集并汇聚成为一个成为`param`的==元组==；例如

    - ```python
      def test(a, *param):
          print(a)
          print(param)
          
      test(1,2,3,4)
      >> 输出：1
              (2,3,4)
      
      ```

  - 用于函数调用时：`test(*tup_p)`，将一个元组扩展为参数列表：

    - ```python
      param = (1,2,3)
      test(*param) <==等同于==> test(1,2,3)
      ```

- 命名关键字参数`**param` ：

  - 用于函数定义：从此处开始直到结束的所有的==关键字参数==都将被收集并汇集为一个名为`param`的==字典==；例如：

    - ```python
      def test(**kw):
          print(kw)
       
      test(p1=1, p2=2)			# 输出：{'test1':1， 'test2':2}
      >>> {'p1:1, p2:2'}
      ```

  - 用于函数调用：将字典类型解析为关键字参数：

    - ```python
      param = {'p1':1, 'p2':2}
      
      test(**param)   <====等同于====>  test(p1=1, p2=2)
      ```


### 3.作用域

-   `global`和`nonlocal`：
    -   `global `：用来在函数或其他==局部作用域中使用全局变量==。但是如果不修改全局变量也可以不使用global关键字。

        ```python
        def test():
            global g_TEST
            g_TEST = 10
        ```

    -   `nonlocal `：来在函数或其他作用域中使用==外层(非全局)变量==，如闭包中；
-   变量作用域：LEGB，L>E>G>B
    -   L：local，函数内部作用域；
    -   E：enclosing，函数内部与内嵌函数之间；
    -   G：global，全局作用域；
    -   B：`build-in`内置作用域；

### 4.闭包

- 什么是闭包？为什么需要闭包？

    - 函数和函数内部能访问到的变量（环境）的总和，就是一个闭包。

    - 闭包常常用来「间接访问一个变量」。换句话说，「隐藏一个变量」。我们需要一个类似全局的变量，但是该变量又不能随意暴露出来，就需要闭包。

    - 例如，利用闭包实现计数器：

        ```python
        def createCounter():
            r = 0
            def f():
                nonlocal r
                r += 1
                return r
            return f
        
        f1 = createCounter()
        f2 = createCounter()
        f1()  #-->返回 1
        f1()  #-->返回 2
        f1()  #-->返回 3
        f2()  #-->返回 1
        f1()  #-->返回 4
        ```

### 5.匿名函数（lambda表达式）

- 匿名函数（lambda表达式）：只有一个表达式，返回值就是该表达式的结果。`lambda x，y: x*y`,分号前为函数参数，分号后表达式为函数返回值；

## 3.迭代

### 1.列表生成式

-   `list(iterable)`函数，可以把一个可迭代对象转换为列表；

-   `[exp for iter_var in iterable]`列表生成式，生成新的`list `，==其中，`iter_var `可以跟exp相关，也可以不相关==

    -   ```python
        [i*i for i in range(10)]
        [random.choice(range(10)) for _ in range(9)]    #后面的for循环仅表示循环多少次。_ 常用于表示临时变量
        ```

### 2.生成器

> 在`yield`表达式处暂停并返回数据,暂存函数内部数据和栈信息, 当再次使用`next或send`时继续执行;
>
> `send`: 发送一个参数到generator, 该参数作物`yield`表达式的值,并返回下一个值;
>
> [参考](https://docs.python.org/3.7/reference/expressions.html#yieldexpr)

- 创造生成器的方式:

  - 1.使用列表生成器：将列表生成式的`[]`换为`()`，如`a = (i for i in range(10))` a就是一个生成器；

  - 2.使用`yield `： 

    ```python
    def test(max):
       	a=0
        while a < max:
            yield a
            a = a + 1
    ```

- 可以通过`for`循环或`next()`取出生成器中的数据, 每次取一个值, 最终抛出`StopIteration`的异常;4.yield表达式

### 3.迭代器

- 可迭代对象

    - 可迭代对象`collections.Iterable`：可以直接作用于==`for`==循环的对象，包括`list, tuple, dict, set, str, generator, 迭代器, 生成器 `等；可以用`isinstance(xxx, collections.Iterable)` 判断是否可迭代；

    - 可迭代对象需要实现`__iter__()` 方法，并返回一个迭代器；

    - `iter(iterable)`：将可迭代对象转变为迭代器，内部就是调用`__iter__() `完成的；

    - 

- 迭代器 

    -   迭代器`Iterator`：可以被`next()`函数调用并不断返回下一个值的对象（生成器）；任何实现了` __next__() `方法 （python2 是 next）的对象都可以称为迭代器，`__next__() `实现两个功能，1.为下次调用`next() `修改好状态，2.返回当前调用的生成结果； 同列表的区别在于，构建迭代器的时候，不像列表把所有元素一次性加载到内存，而是以一种延迟计算方式返回元素。
    -   `Iterator`继承于`Iterable`，并实现了`__next__()`方法；
    -   迭代器需要实现`__next__（）和__iter__()`方法；`__iter __() `返回本身， `__next__() `返回容器内下一个值；
    -   `next() `迭代器边界会抛出`StopIteration `异常；

- 生成器：

    -   一种特殊的迭代器，不需要显示的定义`__next__() 和__iter__() `方法，只需要借助`yield `关键字，或把列表生成式的`[ ] `换为`( ) `;
    -   状态挂起：和返回值并退出的常规函数不同，生成器函数自动在生成值的时刻挂起并继续函数的执行。（在下次取值的时候才进行下次的运算）。
    -   yield：语句挂起该函数并向调用者返回一个值，但是，保留足够的状态使得函数能够从它离开的地方继续。

- 迭代器和生成器：

    -   迭代器：任何实现了` __next__（） `方法 （python2 是 next）的对象都可以称为迭代器，同列表的区别在于，构建迭代器的时候，不像列表把所有元素一次性加载到内存，而是以一种延迟计算方式返回元素。
    -   生成器：生成器本身还是一个迭代器，可以理解为方便构造的特殊迭代器。
    -   生成器是单迭代器对象，只支持一次活跃迭代。

- `for`循环的实现：

    - `iter()`返回的迭代器-->`__iter__()`;
    - 循环调用`next()`;

### 4.其他

-   切片：`[start_index : end_index : step] `
    -   `start_index `表示起始索引；
    -   `end_index `表示结束索引；
    -   `step `表示步长，步长不能为0，且默认值为1，为`-1 `可以逆序切片；

## 4.模块

### 1.模块定义

- 模块：每一个`.py `文件都可以称为一个模块；

- 包：含有一些模块文件和一个`__init__.py`（用于表明这个文件夹是特别的）的文件夹，；

    -   ```
        package_name
        ├─ __init__.py
        ├─ abc.py
        └─ xyz.py
        ```

- 包可以嵌套；

- 模块的标准写法：

    -   ```python
        #!/usr/bin/env python3
        # -*- coding: utf-8 -*-

        ' 模块注释 '

        __author__ = 'xxx'

        import xxxx
        ...
        ```

- 模块分为直接运行和导入两种情况，当模块直接运行时会把一个特殊变量`__name__ `赋值为`__main__ `;

- 最小化`from *`的破坏：`_X`和`__all__`：

    -   作用：防止`from *`导出包中所有对象名；
    -   `_x`指明不希望被`from *`导出的对象名；
    -   `__all__ = ['xx', 'xx']`，指明希望通过`from *`语句导出的对象名；


-   访问控制：
    -   一般`__xxx__ `类型名称的变量，是系统保留特殊变量，可以被直接引用；例如`__name__, __author__ ` 
    -   类似`_xxx, __xxx `类型名称的变量，约定都是非公开的，不应该被直接引用；但并无访问权限控制，可以直接访问到，仅作为遵守规范；
-   变量：`__file__`，该变量自动的被设置为代码所在的python模块的文件名，`os.path.dirname(__file__)`自动获取自身的路径；

### 2.模块使用

- import工作步骤：1.找到模块文件；2.编译成位码；3.执行模块代码创建其所定义的对象；
- 模块文件的选择：除了一般的py文件，包，还可以导入：1.编译扩展模块（c,c++编写的)，使用动态连接，如`.so, .dll, .pyd`； 2.c编写的编译好的内置模块，并通过静态链接至python； 3.zip文件组件，导入时会自动解压缩；等等；
- `import, from`：是可执行语句，类似`def`，都是隐性赋值语句，所以，只有在对应的import语句执行后，才可使用；
- 命名空间：模块就是命名空间，存在于模块之内的变量名就是模块对象的属性；
  - 模块语句会在首次导入时执行；
  - 文件顶层赋值变量的语句，会建立模块对象的属性，赋值的变量名会存储在模块的命名空间内；
  - 命名空间能通过属性`__dict__,或 dir(M)`获取；
- 重载模块：模块只有在首次导入时会加载，后续导入不会重复加载，只能重新导入；`imp.reload(M)`；
  - 重载模块只能做到覆盖，新增；不能做到删除；

### 3.pip使用

-   第三方模块：通过`pip`安装，同时安装`python2`和`python3`需要用`pip2和pip3`区分；

    -   模块的搜索路径：通过`sys.path`查看。

    -   `pip `使用方法：

        ```shell
        # 安装
        pip install [options] SomePackage

        # 查看SomePackage的信息（文件信息）
        pip show [-f] SomePackage

        # 查看所有安装包信息（）
        pip list [-o|-u]

        # 卸载
        pip uninstall [options] <package>
        ```

### 4.包

- 基础：包导入语句的路径中 ==每个目录==内都必须有一个`__init__.py`文件；
  - 通常情况， `__init__.py`文件扮演了包初始化的钩子、替目录产生模块命名空间以及使用目录导入时实现`from *`；
  - 1.python首次导入某个目录时，会自动执行该目录下的`__init__.py`文件中的所有程序代码，
  - 2.可以在`__init__.py`内使用`__all__`列表来定义目录以from * 语句导入时，需要导入什么；


- 包的搜索路径：`sys.path`，查看python包搜索的路径；
- 修改搜索路径：
  - 1.直接修改`sys.path: sys.path.append('/usr/....``')`
  - 2.设置环境变量`PYTHONPATH`，该环境变量会自动添加到搜索路径中`export PYTHONPATH=xxx`。
  - 3.在已有的搜索路径下添加`.pth`文件：内容`import site; site.addsitedir('/usr/...')`

### 5.高级话题

- `_X`：指明在`from *`不需要导入的变量名；仅在`from *`时有效；
- `__name__ 和 __main__`：如果文件是以顶层程序文件执行，在启动时，`__name__`就会设置为字符串`__main__`；如果是被导入，`__name__`就会改设为客户端所了解的模块名；
- 以名称字符串导入模块：`exec('import ' + modname)`；
- `from `复制变量名，而不是连接；

## 5.面向对象OOP

>   OOP：Object Oriented Programming

### 1.基本语法

- 类和实例：类是创建实例的模板，而实例是一个一个具体的对象；

- Python中类的创建：

    -   ```python
        class Student(object):
          def __init__(self, x,y..):
            self.m1 = x
            self.m2 = y
            ...
        ```

    - 通过`class `关键字定义类；
    - 通过`(object) ` ：表明继承关系；
    - 通过`__init__(self, ...) `构造类的对象；

- `__init__() `：类似C++中的构造函数；第一个参数必须是`self `，指向实例化对象本身；

- 成员命名规则：

    -   `_xx `：还是`_xx `，只是表明这个成员不想被外部访问；
    -   `__xx `：最终变为 ` _ClassName__xx `，用此表示是内部成员，同时控制外部对齐访问；
    -   `__xx__` ：还是 `__xx__ `，一般是作为系统保留的具有特殊作用的变量名；

- 动态语言的“鸭子类型”， 它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那他就可以被看做是鸭子;

- 使用`isinstance() `判断对象是否为某种类型的实例；

- 使用`dir() `获得一个对象的所有属性和方法；

- 使用`hasattr() `判断一个对象是否具有某种属性或方法；

- 实例属性和类属性：

  - 实例(对象)属性：给实例对象绑定属性的方法是通过实例变量，或者通过`self`变量；

  - 类属性：直接在`class`中定义属性，这种属性归类所有；

    ```python
    class Student(object):
      	def __init__(self, name):
          	self.name = name			# 实例对象属性
        class = '302'					# 类属性
    ```

  - 当成员函数的第一个参数不是`self `时，则这个成员函数属于类而不属于事例对象；

- `getattr(), setattr()`:

    - `getattr(object, name[, default])`: 获取对象属性值;
    - `setattr(object, name, value)`: 设置对象属性值;

### 2.高级编程

>  类属性查找策略:
>
> 1.如果attr是一个Python自动产生的属性，找到！(优先级非常高！)
>
> 2.查找`obj.__class__.__dict__`，如果attr存在并且是data descriptor，返回data descriptor的`__get__`方法的结果，如果没有继续在`obj.__class__`的父类以及祖先类中寻找data descriptor
>
> 3.在`obj.__dict__`中查找，这一步分两种情况，第一种情况是obj是一个普通实例，找到就直接返回，找不到进行下一步。第二种情况是obj是一个类，依次在obj和它的父类、祖先类的`__dict__`中查找，如果找到一个descriptor就返回descriptor的`__get__`方法的结果，否则直接返回attr。如果没有找到，进行下一步。
>
> 4.在`obj.__class__.__dict__`中查找，如果找到了一个descriptor(插一句：这里的descriptor一定是non-data descriptor，如果它是data descriptor，第二步就找到它了)descriptor的`__get__`方法的结果。如果找到一个普通属性，直接返回属性值。如果没找到，进行下一步。
>
> 5.很不幸，Python终于受不了。在这一步，它raise AttributeError

- `__getattr__`：正常情况下, 当我们调用类的方法或属性时,如果不存在,就会报错, `__getattr__`可以实现当属性查询不到时会被`__getattr__`捕获，通常需要返回一个值或抛出`AttributeError`异常；

- 创建类的示例后，可以给 ==实例==绑定任何属性和方法，绑定的属性和方法只跟这个实例对象有关，跟类和其他实例无关；

- 给所有类绑定方法：

    -   ```python
        def test(self):
            pass
        ClassName.test = test
        ```

- 限制实例的属性和方法名：通过`__slots__`变量，通过给该变量赋值一个元组，来规定允许绑定的属性名称和方法名称；==只对自身类起作用，对通过继承的子类不起作用==；

    -   ```python
        class A(object):
            # 只允许存在名为name、age的属性或方法
            __slots__ = ('name', 'age')
            pass
        ```

- 描述器Descriptor:

    - 包含`__get__(self, instance, owner), __set__, __delete__`的类的实例;

    - 一个属性的访问通过描述器的`__get__, __set__`等实现;

    - 也常会用`@property`属性化用法;

        ```python
        class P():
            def __get__():
                pass
            
         class T():
            a = P()
        ```

- 直接定义的属性无法做到数据类型，数据范围等的限制，一般需要依靠`get(), set()`函数的帮助；

    -   通过`@property `装饰器可以将一个方法转换为属性调用；

    -   `@property ` 还会创建另一个装饰器`@xxx.setter `；负责把`xxx `方法变成属性赋值，不定义`setter `方法，则该属性就为只读的；

        ```python
        class A(object):
            
            @property
            def name(self):
                return self._name
            
            @name.setter
            def name(self, name):
                self._name = name
        ```

- 枚举类：通过`Enum `类定义的类型；`value `属性则是自动赋给成员的`int`变量；

  ```python
  from enum import Enum
  Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
  Month.Jan.value 
  >> 1

  # 还可以精确的控制枚举类型
  from enum import Enum, unique

  @unique     #帮助检查保证没有重复值
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

- `type()` ：1.查看一个类型或变量类型，2.创建一个新类型；通过`type()`函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用`type()`函数创建出class。

  ```python
  # 要创建一个class类，type()函数以此传入3个参数：
  # 1.calss的名称
  # 2.继承的父类集合，（元组，所以，当只有一个时写法为‘（xxx,）’）
  # 3.calss的方法名称 和 函数绑定

  def fn(self, name="world"):
      print('Hello, %s.'%name)
      
  Hello = type("Hello", (object,), dict(hello=fn))
  ```

- 静态方法和类方法

    - 静态方法：嵌套在一个类中，用`@staticmethod`修饰, 没有`self`和`cls`参数, 几乎相当于普通函数, 只是与该类有关联; 
    - 类方法：相比于普通方法, 传递给它们的第一个参数是一个类对象而不是实例`cls`, 因此可以在方法中调用类相关的属性和方法；用`@classmethod`修饰, 可以通过类和实例调用；`@classonlymethod`: 只能通过类调用, 调用时会判断实例参数`instance`是否为`None`, 是则抛出异常;
    - 区别点：(归根是两种方法传入参数不同)1.两者都能通过实例或类调用，2.静态方法第一个参数传入类，可以在方法内调用类属性；类方法无传入函数，无法操作类属性，通常用于设置环境变量等操作；

- `__new__(), __init__()`:

    - `__new__()`: 在`__init__`之前被调用的特殊方法, 是用来创建对象并返回的方法;
    - `__init__`: 只是用来将传入的参数初始化给对象,

- `__get__, __getattr__, __getattribute__, __getitem__`: 

    - `__getitem__`: 实现类似`obj['key']`的调用;
    - `__getattr__`: 实现当属性查询失败时, 自动处理;
    - `__getattribute__`: 无条件实现属性调用, 所有属性调用入口. 用`object.__getattribute__`避免循环调用; 

###  3.运算符重载

> 类中有很多类似`__xxx__`之类的函数，可以作为钩子，实现特殊的功能或对运算符实现重载；

- `__init__(self,...)`：构造函数，对象被创建时调用；

- `__del__(self)`：在对象被销毁时调用；

- `__str__(self)`：返回一个字符串，在实例化对象被`print()`或`str()`调用时调用；

- `__iter__(self)` ：如果一个类想被用于`for...in `循环，就必须实现一个`__iter__()`方法；该方法返回一个迭代对象，然后，Python的`for`循环就会不断调用该迭代对象的`__next__()` 方法拿到循环的下一个值；

  - 可迭代对象就是含有`__iter__()`方法的对象

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

- `__getitem__(self, key)` ：使用`x[key]`索引操作符的时候调用;

- `__setitem__`：分片

- `__call__` ：实例化对象本身可以做为一个方法，直接对实例进行调用；

- `__add__(self, other)`：重载运算符`+`；此外还有`__radd__, __iadd__`

- `__bool__, __len__, __lt__, __gt__`

### 4.python如何实现继承

> 对于每一个定义的类, python 会计算出一个 方法解析顺序列表(MRO), 这个MRO就是一个简单的所有基类的线性顺序表; 可用 `ClassType.__mro__` 查看,_返回一个元组_. 
>
> super() 会遍历 MRO 列表, 
>
> `super(type, [object-or-type])`: type 用来定位当前 MRO 的index, 并返回mro[index + 1] 作为搜索类表, object-or-type 用来生成 MRO, 

- 关于`super()`, 可参考 [super](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/), 

### 5.其他对象中的重要属性

- `__module__`: 表示当前操作的对象所在模块, 
- 

## 6.装饰器和元类

### 1.装饰器

> 装饰器自身是一个返回可调用对象的可调用对象；
>
> 函数装饰器语法关键在于，@decorator ---> 相当于 `func = decorator(func)`;
>
> 也就是被装饰函数 = 装饰器内部的包装函数，包装函数执行额外代码后再调用原有被装饰函数；

- 函数装饰器

    ```python
    def decorator(F):
        return F
    
    @decorator
    def func(): 
        ...
    # 相当于 func = decorator(func)
    ```
    - 装饰函数编写:

      - ```python
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

- 类装饰器

    - ```python
        @decorator
        class C:
            ...
        # 等同于
        class C:
            C = dcecorator(c)
        ```

    - 可以用装饰器实现扩展类的功能

    - ```python
      def log_getattribute(cls):
          orig_getattribute = cls.__getattribute__
          
          def new_getattribute(self, name):
              print('getting: ', name)
              return orig_getattribute(self,name)
          cls.__getattribute__ = new_getattribute
          return cls
      
      @log_getattribute
      class A:
          def __init__(self, x):
              self.x = x
              
      ```


### 2.元类   [参考](http://blog.jobbole.com/21351/)

> 元类就是用来创建类的“东西”, 像类是用来创建实例一样, 元类就是用来创建类的.例如`type`就是一个内建的元类,
>
> 元类本身: 1.拦截类的创建, 2. 修改类, 3.返回修改之后的类;
>
> 主要用途: 创建API, 例如 Django的ORM, 
>
> `__new__(cls, name, bases, attrs, **kwargs)`方法接收到的参数依次是：
>
> 1. cls, 当前元类, 只有此项是指当前元类；
> 2. name, 要创建的类的名字；
> 3. bases, 要创建的类所继承的父类集合；
> 4. attrs, 要创建的类的属性和方法集合（不包括继承的）。

- 例: 元类的创建


- ```python
  # 元类一般以Metaclass结尾,表明是一个元类, 元类是创建类,必须从type类型派生；
  class ListMetaclass(type): 
      # 重写 __new__ 方法, 在创建类时调用(注意,是创建类的时候);
      def __new__(cls, name, bases, attrs):
          attrs['add'] = lambda self, value: self.append(value)
          return type.__new__(cls, name, bases, attrs)
      
  # 传入metaclass时，Python解释器在创建Mylist时，要通过 ListMetaclass.__new__()来创建
  class Mylist(list, metaclass=ListMetaclass):
      pass
  # 或者使用装饰器
  @six.add_metaclass(ListMetaclass)
  class Mylist(object):
      pass
  # 或者(python3中取消了)
  class Mylist(list):
      __metaclass__ = ListMetaclass
  ```

- `__class__`：一个实例所属的类；普通对象就是所属的类，普通类就是`type`或`元类`；

### 3.管理属性

- `__getattr__, __setattr__`：将定义属性和获取和赋值指向通用的处理器方法；

- `property()`：把特定属性访问定位到get和set处理器函数，也叫特性；

  - ```python
    attribut = property(fget, fset, fdel, doc),
    ```


## 7.异常、调试和测试

> 在函数出错时，c往往会通过返回值表示是否发生错误，这导致正确结果和错误代码混和，一旦出错，还要一级一级上报；所以一般高级语言通常都内置了一套`try...except...finally...`的错误处理机制；

### 1.异常处理

- `try `：来运行代码，如果发生错误，则后续代码不会继续执行，直接跳转到错误处理，即`except`语句块；

- `except`：如果没有发生错误，则此段不会执行；发生错误，会被此段捕获；

- `finally` ：如果有此段，则最后一定会执行（发生不发生异常都会执行）；

- `raise `：抛出异常；

- 错误种类：错误也是`class`，所有错误类型都继承自`BaseException`，捕获时不但可以捕获指定类型，还能将子类型同时捕获；

- 自定义异常：`Exception()`,

- `logging`：模块记录错误信息；

- `raise`：抛出一个错误实例；

  ```python
  try:
  	pass
  except Exception1:
      pass
  except Exception2:
      pass
  else:
      pass
  finally:
      pass
  ```

- `with/as` 环境管理：

  - with/as 语句的设计是作为try/finally用法模式的替代方案。

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

*利用系统原生`fork()`*

- `fork()`：通过`os.fork()`创建进程，同`fork()`一致，父进程中返回子进程ID，子进程返回0；

*利用`multiprocessing `模块*

- `multiprocessing `提供了了`Process`类来代表一个进程对象；适用方式：先创建对象，start 方法，join方法，

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

- 进程间通信：`multiprocessing`中的`Queue, Pipes`等；
- `Pool()` ：用于创建大量的子进程；

### 2.多线程

> GIL：Global Interpreter Lock，全局解释器锁，语言解释器用于同步线程的一种机制，使得任何时刻仅有一个线程。
>
> Cpython中依靠GIL，防止多个本地线程执行Python字节码；GIL就是一个防止多线程执行机器码的Mutex；及时有多核CPU，当同时两个线程被调用时，由于锁的存在，只能有一个线程被执行；
>
> Python的多线程在多核CPU上，只对IO密集型计算产生正面效果，对于CPU密集型多线程效率会大幅下降；
>
> python 虚拟机工作方式: 1.设置GIL, 2.切换进一个线程运行, 3.执行字节码,(或让出控制权), 4.把线程设置回睡眠状态(切出线程), 5解锁GIL, 6.重复上述
>
> 当调用扩展外部代码时, GIL会保持锁定, 直到函数执行结束;(因为没有Python字节码计数)

#### 1.基本使用法式

- 使用`t = threading.Thread(target=function, name='threadName)`创建Thread对象，将函数同线程绑定；
- 用`t.start()`启动，用`join()`等待；
- 锁:
  - 通过`lock = threading.Lock()`创建一个锁， 
  - 通过`lock.acquire()`加锁，通过`lock.release()`释放；acquire :获得。
- 信号量:
  - 通过`sp = threading.Semaphore(N)`创建;
  - 通过`lock.acquire()`获取，通过`lock.release()`释放；超过数量获取会阻塞; 默认初始值为1, 当`release`后, 现有值加一, 允许超过初始值;
  - 相关联: `BoundedSemaphore()`, 大致同`Semaphore`, 区别`release`不允许超过初始值; 否则会抛出`ValueError`异常;

#### 2.Thread.run() 和 Thread.start()

- `start()`: 启动线程的唯一方式; 每个线程只能启动一次, 其中会检查相应的标志位, 满足后会调用`_thread.start_new_thread`创建线程, 并传入`_bootstrap()`, 初始化相应标志和环境并调用 `Thread.run()`;
- `run()`: 默认会调用传入的`target`参数指定的方法, 创建`Thread`子类可以重写该方法; 
- !!! ==注意启动线程唯一方式 `start()`==

#### 3.local()

- 很多时候线程需要有自己的私有数据, 但是, 使用局部变量又带来使用上的不方便, 所以引入`threading.local()`;
- 全局声明, 但是每个线程都会有自己的实例,互不影响;

## 9.编码方式

### 1.字符编码   [参看](https://www.zhihu.com/question/23374078/answer/69732605)

- ASCII，（American Standard Code for Information Interchange，美国信息交换标准代码），用8个字节来表示字符，最高位为0，共127个，用于表示英文字符和控制码；
- 扩展字符集：将127号后面的进行编码，添加特殊字符；
- 由于ASCII编码不能表示汉字，中国定制了GB2312编码；小于127的字符同ASCII码，两个大于127的字符连在一起，表示一个汉字；（原先ACSII中存在数字、标点、字母也重新进行了两字节编码，成为全角字符；原先ASCII中的叫半角字符）；
- GBK标准，对GB2312的扩展，包含GB2312的所有内容，同时又增加了近20000个新汉字和符号；汉字占两个字节；
- Unicode：通常用两个字节表示一个字符；会造成浪费；
-  Unicode在网络传输中，出现了UTF-8，UTF-16两个标准，即分别每次传输8位和16位；
- UTF-8，变长编码，使用1~4个字节表示一个符号；中文字符占3个字节（Unicode占2个字节）；用UTF-8 编码的文件会在打开时转为Unicode编码，保存和传输时还是UTF-8编码；

### 2.python字符编码

- 在python3中，字符串是以Unicode编码的，`ord()`：获取字符的整数表示，`chr()`：把编码转换为字符；

  ```python
  # 下面内容等价
  '\u4e2d\u6587'
  '中文' --> Unicode 编码，每个中文占2个字节
  ```

- python3中的字符串类型为`str`，当需要在网络上传输，或保存到硬盘上时，就要把`str`转为`bytes `(用带`b`的前缀的单引号或双引号表示 ) `b'abc'`;

- `str`的`encode()`方法可以编码为指定的bytes；

  ```python
  # 比如需要网路传输时，采用utf-8编码
  >>> '中文'.encode('utf-8')   --> 按照utf-8 方式编码
  b'\xe4\xb8\xad\xe6\x96\x87'  --> utf-8 编码，汉字占三个字节
  ```

- `bytes` 转为`str`用`decode()`方法；

  ```python
  >>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')   --> 按照utf-8 方式解码
  '中文'
  ```

## I其他

### 1.IO

-   IO操作面临异常情况，无法保证所有异常下，文件都得到关闭；可以使用`with`语句；

    -   ```python
        with open('/path/to/file', 'r') as f:
            print(f.read())
        ```

-   像`open()`函数返回的这种有个`read()`方法的对象，在Python中统称为 file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object 不要求从特定类继承，只要写个`read()`方法就行。

-   `open()` 可以指定打开文件的编码方式`encoding`，默认utf-8编码；

-   `b`：表示以二进制方式读写；

-   ！！ ==调用`write() `写入文件时，并不会立刻写入，而是放入缓存中，等待空闲时写入；只有调用`close()`方法，才会立刻将未写入的数据写入磁盘；== 

### 2.文件操作

### 3.序列化

-   程序执行过程中，所有变量都是存放在内存中的，程序执行结束，变量就会消失；我们把变量从内存中变成可存储或传输的过程称之为序列化；可以借助pickling

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

### 4.正则表达式

| 符号     | 匹配                      | 符号   | 匹配             |
| -------- | ------------------------- | ------ | ------------------------------- |
| `\d`     | 匹配一个数字              | `\D`   | 匹配一个非数字                  |
| `\s`     | 匹配空白字符              | `\S`   | 匹配非空白字符                  |
| `\w`     | 字母数字字符             | `\W`   | n-m个字符                       |
| `*`      | 匹配前一个字符0次或无限次 | `+`  | 匹配前一个字符1次或无限次 |
| `?`      | 匹配前一个字符0次或1次 | `{m}/{m,n}` | 匹配前一个字符m次或m到n次 |
| `[...]` | 匹配字符集中的任何一个字符 | `.` | 匹配任意字符（除了\n） |
| ``^``    | 匹配字符必须在开头        | `$`    | 匹配字符必须在结尾              |
| ``\A``   | 匹配字符串必须在开头      | `\Z`   | 匹配字符串必须在结尾            |
| ``(ab)`` | 括号中表达式作为分组      | `\<n>` | 引用标号为n的分组匹配到的字符串 |
| `(?P<name>..)` | python中，命名分组为name | `(?P=name)` | python 中引用name分组 |
|  |  |  |  |

-   `re `模块中的`match `方法可用于判断正则表达式是否匹配成功；
    -   成功返回一个`match `对象；
    -   失败返回`none `；

### 5.JSON
- `json.dumps()、json.loads()`：dict 和 str相互转化；

     - `json.dumps()`

          ```python
          >> d = {'name':'lfeng', 'email':'lfengnl@163.com'}
          >> s = json.dumps(d)
          # s = '{"name": "lfeng", "email": "lfengnl@163.com"}'
          ```

     - `json.loads()`：将str类型的数据转为dict；

       ```python
       >>> d = json.loads('{"name": "lfeng", "email": "lfengnl@163.com"}')
       {"name": "lfeng", "email": "lfengnl@163.com"}
       ```

- `json.dump()、json.load()`：dict 和 json 文件 相互转化；

  - `json.dump()`：将dict类型的数据转为str，并写入到json文件中；

    ```python
    json.dump(d, open('test.json', "w")) 
    ```

  - `json.load()`：从 json 文件中读取数据并转为`dict`；

    ```python
    d = json.load(open('test.json'))
    ```

- 注意，在与前端交互时，有时接收到的数据类型为`bytes`，需要转换为`str`：

  ```python
  data = json.loads(request.body.decode('utf-8'))
  ```

### 6.log



## II.技巧

- `locals() ` ：返回一个字典，包含了函数执行到该时间点时所有定义的一切变量，字典形似为，变量名称和值对应；在Django模版导入上下文时可能有用；(会比较大)

- 由` d = {True:'1', 1:'2', 1.0:'3'}  d[True]=?`引出的问题：
    -   答案为`'3' `，`True, 1, 1.0 `为相同的键值，后面的会覆盖前面的；
    -   字典判断为相同键值的条件：1.`值是否相同（ __eq__()`方法），2.哈希值是否相同（`__hash__()`方法返回相同值）；

- 字典类型加双**号，可以转换为关键字参数；

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

    - ==可用于遍历时同时得到其下标==

      ```python
      for index, x in enumerate(list_xx):
      ```

## III.实用函数

- `callable()`: 判断一个对象是否为可调用的, 是返回True,

- `itertools.chain()`:  将多个可迭代对象整合为一个迭代器,
- 