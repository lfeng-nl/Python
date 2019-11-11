本文用于记录python知识点  


## 1.基础

### 1.数据类型

#### 1.数据类型基础

- 基本数据类型：`int, float, str, bool(True, False), None `
- 容器：`list, str, tuple, dict, set 等` ;

#### 2. str注意点：

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

- python的`list`实现不是链表数据结构, 而是长度可变数组(指数过分配), 插入和删除元素消耗较高(O(n)). 如果需要真正意义上的链表结构, 可以使用`collections.deque`;

- `list.append(object)`：附加单个元素到list的尾部；
- `list.extend([xx, xx])`：附加列表到元素尾部；--> 等同于  `list_a = list_a + list_b`
- `list.remove()`：移除第一非匹配到的元素；
- 列表是可变对象，可以原处修改；
- 遍历删除或添加列表元素：
  - **直接遍历，当删除或增加列表元素时，列表长度发生变化，但遍历的长度不变。会产生问题！**
  - 推荐有此需求时，遍历列表的拷贝；

#### 4.字典` dict`注意点

- `same_key in D`：键存在测试；

- `D.keys()`：-->所有键；

- `D.values()`：所有值；

- `D.items()`：键值对元组；

- `D.get('key', default=None)`：获取一个键的值，不存在不会抛出异常，返回默认值；

- `D.update(E)`: 更新D, `for k in E: D[k] = F[k]` 

- **字典是无序的，哈希表**: 只有**可哈希的**对象才可以作为字典的键, 实现`__hash__(), __eq__()`两个方法;

  > 扩展: 解决哈希冲突
  >
  > - 链接法: 映射到同一位置时,将同一位置的元素加入同一个链表;
  > - 开放定址法: 映射到同一位置时, 重新寻找位置, 每个位置最多有一个元素;(**cPython采用此方式**)


#### 5.元组 tuple

- 元组不可变，没有list的修改之类的方法；
- 元组拆包: 

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

    -   `if elif else`

- 优先级: 单目 > 双目 > 位运算 > `in, not in, is, is not` > 逻辑;

### 3.变量和对象

- **对象**: python对数据的抽象, 每个对象都有各自的编号(类似地址), 类型和值.
    - `is`运算符可以比较对象的编号是否相同;
    - `id() `返回一个表示其编号的整形数, cpython中, 就是对象的内存地址;
    - `type()`返回对象的类型;
- **变量**:
    - 是一个系统表的中的元素，拥有指向对象连接空间。
- **可变对象和不可变对象**:
    - **不可变类型有**: `int, str, tupl`, **可变类型**: `list, dict`;
    - 不可变并不严格等同于值不可变, 例如`tupl`元素为`list`对象, 元组中不
      可变的是元素的标识;
    - 不可变对象自身值或其元素值不可更改;
-  **函数参数传递**:
    - 首先要理解: **变量是对象的一个引用;**
    - 函数参数传递时, 本质上是赋值, 和**赋值操作本身就是一种名字到对象的绑定过程**;
    - 参数传递是赋值, 但是传入的实质是对象的引用;
- `==`和`is`: 
    - `==`值比较，是否相同，
    - `is`,精确比较，是否指向同一个对象；
- `isinstance(obj, class)`：对象是否是类的实例；
- `sys.getrefcount()`会返回引用计数；
- 引用是一种关系，以内存中的指针的形式实现；
- `cPython`中, 垃圾回收使用的主要算法是引用计数;
- 弱引用: 不会增加引用数量;
- 赋值和深浅复制: 
  - 赋值: 在目标和对象之间建立绑定关系;
  - 浅拷贝: `copy.copy(x)`, 构造一个新对象, 然后将原对象中找到的引用插入其中;
  - 深拷贝: `copy.deepcopy()`, 构造一个新对象, 递归地将原始对象中找到的对象的副本插入;

### 4.特殊语法

- `range(start, stop, step)`: 默认开始为`0`, 默认步长为`1`; 需要逆序时, 注意步长设置为负; 

- `for...else`: `else`段在循环自然结束, 而不是`break`时执行, 可以用于清除哨兵变量等操作;
- `with`: 上下文管理器, 可作用于含有`__enter__(self), __exit__(self，exc_type, exc_value, traceback)`的对象;
  - 执行过程: 调用`__enter__()`,任何返回值都会绑定到`as`子句 --> 执行代码块 --> 调用`__exit__()`;
  - `contextlib`模块;
- 负索引: 对于取位置元素的`a[x]`, 可以使用负数, 表示倒数位置;
- 比较运算符可以任意串联: `a ap1 b op2 c ... y onN z`等价于`a op1 b and b op2 c and ... and y opN z`;

## 2.函数

### 1.内置函数
- `abs(), max(), int(), float(), str(), bool()`
### 2.定义函数
- 在Python中定义函数，可以用==必选参数、默认参数、可变参数、关键字参数和命名关键字参数==这5种参数都可以组合使用。但是请注意，
  
- **函数定义**参数的顺序必须是：**位置参数、默认参数、可变参数(`*args`)、命名关键字参数**(`**kwargs`)；
  
- **函数调用**参数的顺序是: **位置参数在前, 关键字参数在后**;
  
   - 函数定义时的位置参数, 在调用时可以通过关键字参数形式进行传递; 但要注意匹配顺序;
   
```python
   def f(a, b, c=0, *args, **kwargs):
   # 1.通过位置分配位置参数;
   # 2.通过匹配变量名分配关键字参数;
   # 3.其他非关键字参数分配到*args元祖;
   # 4.其他关键字参数分配到**kwargs字典
   # 5.用默认值分配给在头部未得到分配的参数;
```

- 位置参数: 从左到右进行匹配;

- 关键字参数: 通过参数名进行匹配;

- 默认参数: 为没有传入值的参数定义参数值

- 可变参数: 收集任意多基于位置或关键字的参数:

  - `*arg, **kwarg`

### 3.作用域

-   `global`和`nonlocal`：
    -   `global `：用来在函数或其他==局部作用域中使用全局变量==。但是如果不修改全局变量也可以不使用global关键字。

        ```python
        def test():
            global g_TEST
            g_TEST = 10
        ```

    -   `nonlocal `：来在函数或其他作用域中使用==外层(非全局)变量==，如闭包中；
-   变量作用域：LEGB，名称查找顺序: L -> E -> G -> B
    -   L：local，局部作用域；
    -   E：enclosing，闭包作用域；
    -   G：global，全局作用域；
    -   B：builtins , 内置模块的名字空间；

### 4.匿名函数（lambda表达式）

- 匿名函数（lambda表达式）：只有一个表达式，返回值就是该表达式的结果。`lambda x，y: x*y`,分号前为函数参数，分号后表达式为函数返回值；

## 3.迭代

### 1.列表生成式

-   `list(iterable)`函数，可以把一个可迭代对象转换为列表；

-   `[exp for iter_var in iterable]`列表生成式，生成新的`list `，**其中，`iter_var `可以跟`exp`相关，也可以不相关**

    -   ```python
        [i*i for i in range(10)]
        [random.choice(range(10)) for _ in range(9)]    #后面的for循环仅表示循环多少次。_ 常用于表示临时变量
        ```

### 2.生成器

> 在`yield`表达式处暂停并返回数据,暂存函数内部数据和栈信息, 当再次使用`next`或`send`时继续执行;
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

## 4.面向对象

>   一切类(包括`type, object`)都是`type`的实例;
>
>   所有类(包括`type`)都继承于`object`;
>
>   python一切皆对象:
>
>   1.  **`type`是自身的实例**, `type`继承于`object`, 所以 type is a object; 
>   2.  所有类都是`type`的实例,  type继承于`object`, 所以 class is a object;
>   3.  所有类都继承于`object`, 所以对象 is a object;

### 1.基本语法

- Python中类的创建：

    -   ```python
        class Student(object):
          # 类属性
          c1 = 'c1'
          # 成员函数
          def __init__(self, x,y..):
            self.m1 = x
            self.m2 = y
        ...
         
        ```
        
    - 成员命名规则：

        -   `_xx `：还是`_xx `，只是表明这个成员不想被外部访问；
        -   `__xx `：最终变为 ` _ClassName__xx `，用此表示是内部成员，同时控制外部对齐访问；
        -   `__xx__` ：还是 `__xx__ `，一般是作为系统保留的具有特殊作用的变量名；

- 实例属性和类属性：

    - 实例(对象)属性：给实例对象绑定属性的方法是通过实例变量，或者通过`self`变量；

    - 类属性：直接在`class`中定义属性，这种属性归类所有；

      ```python
      class Student(object):
        	def __init__(self, name):
            	self.name = name			# 实例对象属性
          xxx = '302'					    # 类属性
      ```

    - 创建类的实例后，可以给 实例绑定任何属性和方法，绑定的属性和方法只跟这个实例对象有关，跟类和其他实例无关；

- 关于对象的一些函数:

    - 使用`isinstance() `判断对象是否为某种类型的实例；
    - 使用`dir() `获得一个对象的所有属性和方法；
    - 使用`hasattr() `判断一个对象是否具有某种属性或方法；
    - 使用`getattr(object, name[, default])`获取一个对象的属性;
    - 使用`setattr(object, name, value)`设置一个对象的属性;

-   `type()` ：1.查看一个类型或变量类型，2.创建一个新类型；通过`type()`函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用`type()`函数创建出class。

    ```python
    # 要创建一个class类，type()函数以此传入3个参数：
    # 1.calss的名称
    # 2.继承的父类集合，（元组，所以，当只有一个时写法为‘（xxx,）’）
    # 3.calss的方法名称 和 函数绑定
    
    def fn(self, name="world"):
        print('Hello, %s.'%name)
        
    Hello = type("Hello", (object,), dict(hello=fn))
    ```

-   **普通方法, 静态方法和类方法**

    -   普通方法: 第一个参数是`self`
    -   静态方法：嵌套在一个类中，用`@staticmethod`修饰, 没有`self`和`cls`参数, 几乎相当于普通函数, 只是与该类有关联; 
    -   类方法：相比于普通方法, 传递给它们的第一个参数是一个类对象而不是实例`cls`, 因此可以在方法中调用类相关的属性和方法；用`@classmethod`修饰, 可以通过类和实例调用；`@classonlymethod`: 只能通过类调用, 调用时会判断实例参数`instance`是否为`None`, 是则抛出异常;
    -   区别点：(归根是两种方法传入参数不同) 1.两者都能通过实例或类调用，2.类方法第一个参数传入类，可以在方法内调用类属性；静态方法无传入参数，无法操作类属性，通常用于设置环境变量等操作；
    -   抽象方法:  `@abc.abstractmethod`


-   `__new__(cls, *args, **kwargs)`: 负责创建实例;

    -   需要调用父类的`__new__`方法, 生成实例, 并返回;

        ```python
        def __new__(cls, *args, **kwargs):
            self = super().__new__(cls, *args, **kwargs)
            # todo
            return self
        ```

### 2.属性管理

- `@property `:

    -   将一个方法转换为属性调用；

    -   `@property ` 还会创建另一个装饰器`@属性名.setter `；负责把`xxx `方法变成属性赋值，不定义`setter `方法，则该属性就为只读的；

        ```python
        class A(object):
            
            # get方法
            @property
            def name(self):
                return self._name
            
            # set方法
            @name.setter
            def name(self, name):
                self._name = name
            
            # 属性删除
            @name.deleter
            def name(self):
                pass
        ```
- `__getattr__, __getattribute__, __getitem__`: 

    - `__getitem__`: 实现类似`obj['key']`的运算符重载;
    - `__getattr__`: 实现当属性查询失败时, 自动处理;
    - `__getattribute__`: 所有属性调用入口. 用`object.__getattribute__(self, attr)`避免循环调用; 
    
- `dir(), getattr(), hasattr(), setattr(), vars()`:

  - `dir`: 列出对象大多数属性, 默认使用`__dir__()`方法, 未提供时, 返回`__dict__`中的信息;
  - `vars()`: 返回对象的`__dict__`属性;
      - `__dir__()`: 不接受参数, 返回一个表示模块中可访问名称的字符串列表;
      - `__dict__`: 用来存储**对象**属性的一个字典, 例如在`__init__()`中定义的, 通过实例字节附加上的;
  - `getattr()`: 从对象总获取指定属性的值, 不存在时返回异常或默认值;
  - `hasattr()`: 是否存在某种属性;
  - `setattr()`: 将指定属性置为新值;
  

### 3.Python如何实现继承

> `ClassType.__mro__`返回一个元组, 就是一个简单的所有基类的线性顺序表;  称为: MRO( **Method Resolution Order** 方法解析列表)列表(子类在前);

- `super(cls, inst)`:  [参考1](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/) [参考2]( http://funhacks.net/explore-python/Class/super.html )
    - 1. 获取`inst`的MRO列表; 2.在MRO中查找`cls`的`index`, 返回下一个类`MRO[index+1]`,
    - 在方法中调用: `super().method(arg) 等同于 super(__class__, self).method(arg)`
- 混入(mixin)类是指继承两个或两个以上的类, 并将他们的特性混合在一起;
- python应避免多重继承;

### 4.特殊方法(魔术方法)

> 类中有很多类似`__xxx__`之类的函数，可以作为钩子，实现特殊的功能, 称为魔术方法；[参考](<https://docs.python.org/zh-cn/3/reference/datamodel.html#basic-customization>)

- 基础
    - `__init__(self,...)`：构造函数，对象被创建时调用；
    - `__new__(cls, ...)`: 用于创建实例并返回, 在`__init__`前被调用, 重写时需要显示调用并返回父类`__new__()`方法;
    - `__del__(self)`：在对象被销毁时调用；
    - `__str__(self)`：返回一个字符串，在实例化对象被`print()`或`str()`调用时调用；
    - `__repr__(self)`: 返回一个字符串, 在`repr()`中调用,**交互式终端中用于提示** , `__str__`不存在时替代`__str__`功能;
    - `__call__()`: 可调用;
- 运算符重载
    - `__getitem__(self, key)` ：使用`x[key]`索引操作符的时候调用;
    - `__setitem__(self, key, value)`：使用`x[key]`索引赋值;
    - `__call__` ：实例化对象本身可以做为一个方法，直接对实例进行调用；
    - `__add__(self, other)`：重载运算符`+`；此外还有`__radd__, __iadd__`
    - `__lt__(), __le__(), __eq__(), __ne__(), __gt__(), __ge__()...`
- 迭代器
    - `__iter__(self)` ：如果一个类想被用于`for...in `循环，就必须实现一个`__iter__()`方法；该方法返回一个迭代对象，然后，Python的`for`循环就会不断调用该迭代对象的`__next__()` 方法拿到循环的下一个值；
        - 可迭代对象就是含有`__iter__()`方法的对象;
    - `__next__`: 返回容器下一个元素;
- 字符串
  - `__repr__`: 使用`repr`获取对象的字符串形式时, 会调用`__repr__`方法, 例如终端里打印一个对象;
  - `__str__`: 使用`str()`函数时被调用, 当`__str__`未实现时, 会调用`__repr__`方法;
- 数值转换
  - `__abs__, __bool__, ...`
- 属性访问控制
    - `__slots__`: 显式声明数据成员；
    - `__getattr__(self, name)`: 定义当用户试图获取一个不存在的属性的行为;
    - `__getattribute__(self, name)`: 属性访问拦截器, 访问类的属性时控制被访问时的行为, **注意避免循环调用**;
    - `__setattr__(self, name, value)`: 定义属性被赋值时的行为;
    - `__dict__`:  对象的属性字典;
    - `__dir__()`:  在`dir()`被调用时调用
        - `dir()`:返回包含属性的列表, 如果对象提供`__dir__()`方法，直接使用， 除此使用`dir()`逻辑, 包含实例的属性，类的属性和递归基类的属性; 
- 上下文管理器
    - `__enter__(self)`进入上下文管理器调用;
    - `__exit__(self, exc_type, exc_value, trace)`退出上下文管理器调用;
        - `exc_type, exc_value, trace`: 可用于异常处理；
- 其他
    - `__module__`: 当前对象的类型所在模块;
    - `__class__`: 当前对象的类;
    - `__hash__`：应该同`__eq__()`一同定义， 表示可哈希；
    - `__bases__`: 由基类所组成的元组;

### 5.元类   

> **重要**: 
>
> **类是`type`的实例,  `__new__(cls)`创建实例, `__init__(self)`初始化实例;**
>
> 元类: **继承于`type`**,  元类在普通类**定义(实例化)**的时候被调用,  通过重写`__new__`方法, 控制类的定义, 增加类属性的操作;
>
> 元类本身: 1.在定义类的时候, 调用该类的元类, 2.可以拦截类的创建, 3. 修改类的属性等操作,  4.返回修改之后的类;
>
> 主要用途: 创建API, 例如 Django的ORM
>
> [参考](http://blog.jobbole.com/21351/)

- 用`class`语句创建的每个类都隐式地使用`type`作为其元类,  即类都是通过`type`构建的. `class`语句默认提供`class Test(metaclass=type):...`, *type创建类*;
- `type(name, bases, dict)`: 
    - `name` 类名, 并且会成为 [`__name__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#definition.__name__) 属性；
    - `bases` 基类, 元组类型; 并且会成为 [`__bases__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#class.__bases__) 属性；
    -  `dict` 属性, 字典类型, 并且会被复制到一个标准字典成为 [`__dict__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#object.__dict__) 属性;


- ```python
  # 元类的创建
  # 元类一般以Metaclass结尾,表明是一个元类, 元类是创建类,必须从type类型派生；
  class ListMetaclass(type): 
      # 重写 __new__ 方法, 在创建类时调用(注意,是创建类的时候);
      def __new__(cls, name, bases, attrs):
          attrs['add'] = lambda self, value: self.append(value)
          return super().__new__(cls, name, bases, attrs)
      
  # 传入metaclass时，Python解释器在创建Mylist时，要通过 ListMetaclass.__new__()来创建
  class Mylist(list, metaclass=ListMetaclass):
      pass
  # 或者使用装饰器
  @six.add_metaclass(ListMetaclass)
  class Mylist(object):
      pass
  ```
  
- `__class__`：一个实例所属的类；普通对象就是所属的类，普通类就是`type`或`元类`；
### 6.其他

-   通过槽限制属性: 通过`__slots__`变量，通过给该变量赋值一个元组，来规定允许绑定的属性名称和方法名称；*只对自身类起作用，对通过继承的子类不起作用*；

    -   ```python
        class A(object):
            # 只允许存在名为name、age的属性或方法
            __slots__ = ('name', 'age')
            pass
        ```

-   枚举类：通过`Enum `类定义的类型；`value `属性则是自动赋给成员的`int`变量；

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

    -   `@unique` 装饰器可以帮助我们检查保证没有重复值；

## 5.装饰器和闭包

### 1.装饰器

> 装饰器本质是一个返回可调用对象的可调用对象；
>
> 函数装饰器语法关键在于，`@decorator` ---> 相当于 `func = decorator(func)`;
>
> 也就是被装饰函数 = 装饰器内部的包装函数，包装函数执行额外代码后再调用原有被装饰函数；

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

-   python内置装饰函数:
    -   `property`: 将方法转换为属性;
    -   `classmethod`: 类方法;
    -   `staticmethod`: 静态方法;

### 2.闭包

- 闭包是一种函数, 它会保留定义函数时存在的自由变量的绑定, 在调用函数时, 仍可以使用这些绑定;

- 实现原理:

  - 外层嵌套作用域中定义的变量会存储在函数对象的`__closure__`属性中; 
  - 当函数被调用时, 会将`__closure__`拷贝到栈帧中使用. 
  - 由于都是引用传递, 资源不会被释放;

## 6.并发执行

### 1.多线程

> GIL：Global Interpreter Lock，全局解释器锁，语言解释器用于同步线程的一种机制，使得任何时刻仅有一个线程。
>
> cPython中依靠GIL，防止多个本地线程执行Python字节码；GIL就是一个防止多线程执行机器码的Mutex；及时有多核CPU，当同时两个线程被调用时，由于锁的存在，只能有一个线程被执行；
>
> Python的多线程在多核CPU上，只对IO密集型计算产生正面效果，对于CPU密集型多线程效率会大幅下降；
>
> python 虚拟机工作方式: 1.设置GIL, 2.切换进一个线程运行, 3.执行字节码,(或让出控制权), 4.把线程设置回睡眠状态(切出线程), 5解锁GIL, 6.重复上述
>
> 当调用扩展外部代码时, GIL会保持锁定, 直到函数执行结束;(因为没有Python字节码计数)

#### 1.基本使用法式

- 使用`t = threading.Thread(target=function, name='threadName)`创建Thread对象，将函数同线程绑定；
- 用`t.start()`启动，用`join()`等待；
- 线程的执行内容: `Thread.run()`方法,该方法会调用参数`target`, 可以重写该方法;

#### 2.守护线程

- python主线程是在所有非守护线程退出后才会退出;
- 如果主线程退出时, 不需要等待某些子线程完成, 就可以为这些子线程设置守护线程标志; 
- 当存在非守护线程未终止时, 进程不会退出;

#### 3.local()

- 很多时候线程需要有自己的私有数据, 但是, 使用局部变量又带来使用上的不方便, 所以引入`threading.local()`;
- 全局声明, 但是每个线程都会有自己的实例,互不影响;

#### 4.同步

- 锁:
  - 通过`lock = threading.Lock()`创建一个锁， 
  - 通过`lock.acquire()`加锁，通过`lock.release()`释放；acquire :获得。
- 信号量:
  - 通过`sp = threading.Semaphore(N)`创建;
  - 通过`lock.acquire()`获取，通过`lock.release()`释放；超过数量获取会阻塞; 默认初始值为1, 当`release`后, 现有值加一, 允许超过初始值;
  - 相关联: `BoundedSemaphore()`, 大致同`Semaphore`, 区别`release`不允许超过初始值; 否则会抛出`ValueError`异常;

#### 5其他

- `threading.current_thread()`: 返回当前线程对象;
- `threading.enumerate()`: 返回所有线程列表;

### 2.多进程

-   利用系统原生`fork()`
    -   `fork()`：通过`os.fork()`创建进程，同`fork()`一致，父进程中返回子进程ID，子进程返回0；

-   利用`multiprocessing `模块
    -   `multiprocessing `提供了了`Process`类来代表一个进程对象；适用方式：先创建对象，start 方法，join方法，

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

### 3.`concurrent.futures`

> 异步执行回调, 异步执行可以由`ThreadPoolExecutor`或`ProcessPoolExecutor`来实现

## 7.异常、调试和测试

>   在函数出错时，c往往会通过返回值表示是否发生错误，这导致正确结果和错误代码混和，一旦出错，还要一级一级上报；所以一般高级语言通常都内置了一套`try...except...finally...`的错误处理机制；

### 1.异常处理

-   `try `：来运行代码，如果发生错误，则后续代码不会继续执行，直接跳转到错误处理，即`except`语句块；

-   `except`：如果没有发生错误，则此段不会执行；发生错误，会被此段捕获；

-   `finally` ：如果有此段，则最后一定会执行(发生不发生异常都会执行), `try...finally`语句可用上下文管理替代；

-   `raise `：抛出异常；

-   错误种类：错误也是`class`，所有错误类型都继承自`BaseException`，捕获时不但可以捕获指定类型，还能将子类型同时捕获；

-   可以通过继承`Exception`定义异常类；

    ```python
    try:
    	pass
    except Exception1:
        # 存在指定异常时会被捕获
        pass
    except Exception2:
        pass
    else:
        # 未发生异常捕获时执行
        pass
    finally:
        # 必定执行，无论发生未发生异常
        pass
    ```

### 2.调试

-   `assert 表达式` ：断言，如果表达式为真，继续执行；否则抛出`AssertionError`； python可以在运行时加入大O，`python3 -O xxxx` 关闭`assert`
-   `logging`：同`assert`相比，`logging`不会抛出异常，而且可以输出到文件；
    -   有`debug,info,warning,error`由低到高几个等级；`logging.debug()， logging.info() ...`
    -   可以通过`logging.basicConfig(level=logging.INFO)`设置等级；
-   `pdb` ：python调试工具，通过`python -m pdb xxx`启动；

### 3.单元测试

>   "测试驱动开发 TDD"；单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。这种以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例，在将来修改的时候，可以极大程度地保证该模块行为的正确性；
>

-   概念:

    -   **测试脚手架 test fixture**: 开展测试所需的准备工作, 以及所有相关的清理操作; 
        -   例如: 创建临时或代理的数据库, 目录, 再或者启动一个服务器进程;
        -   `setUpClass(cls)`: 类方法, 运行单个类的测试之前调用的方法;
        -   `tearDownClass(cls)`:  类方法, 单个类的测试运行后调用;
        -   `setUp(self)`: 运行每个测试方法前都自动被调用;
        -   `tearDown(self)`: 运行每个测试方法后自动被调用;
    -   **测试用例**: 单元测试的基本模块, 一个独立的测试单元, 继承`TestCase`, 检查输入特定数据时的响应;
        -   可以定义若干名称以`test`开头的方法, 例如`test_xxx(self)`, 
        -   `TestCase`提供了一些方法来检测和断言故障;
            -   `assertEqual(a, b)`: 相等
            -   `assertNotEqual(a, b)`: 不等
            -   `assertTrue(x)`: True
            -   `assertFalse(x)`: False
            -   `assertIsNone(x)`: x为None
            -   `assertIsNotNone(x)`: x不为None
    -   **测试套件** `TestSuite`: 测试用例或测试套件的集合;
        -   `addTest(test)`: 添加一个测试用例到`TestSuite`; 批量添加`addTests(tests)`;
        -   `run(result)`: 运行测试套件;
    -   **测试运行器**: 用于执行和输出测试结果的组件;
        -   命令行执行: `python -m unittest test_module`
        -   `TextTestRunner`, 运行测试用例或测试套件, 结果以文本的形式打印;
    -   测试结果: `TestResult` 用于存储测试结果;

-   通常,  测试模块放置在项目的`tests`目录中;

    ```python
    # 导入单元测试模块
    import unittest
    
    #编写测试类，需要从 unittest.TestCase 继承
    class TestDict(unittest.TestCase):
        
        # 类方法, 所有测试用例调用前调用
        @classmethod
        def setUpClass(cls):
            pass
        
        # 类方法, 所有测试用例调用后调用
        @classmethod
        def tearDownClas(cls):
            pass
        
        # setUP, 可以用来完成前置工作, 每个测试用例前调用. 如果发生异常, 则测试方法不会被运行;
        def setUp(self):
            pass
        
        # tearDown, 测试结束后进行清理, 每个测试用例后调用. 如果setUp运行, 无论是否成功, 都会运行 tearDown
        def tearDown(self):
            pass
    
    	# !!! 每一个测试方法必须以test开头，类似`test_xxx()`形式命名, 内部使用TestCase提供的断言方法, 例如assertEqual 进行测试
        def test_init(self):
            d = list(range(10))
            self.assertEqual(d[0], 0)
            self.assertEqual(d[2], 2)
            
            
    if __name__ == '__main__':
        # main 使用 TextTestRunner 运行所有测试用例 
        unittest.main()
    ```

-   

## 8.性能



## 9.编码方式

### 1.字符编码   [参考1](https://www.zhihu.com/question/23374078/answer/69732605) [参考2](<http://www.ruanyifeng.com/blog/2007/10/ascii_unicode_and_utf-8.html>)

- **ASCII**，（American Standard Code for Information Interchange，美国信息交换标准代码），用8个字节来表示字符，最高位为0，共127个，用于表示英文字符和控制码；
- 扩展字符集：将127号后面的进行编码，添加特殊字符；
- 由于ASCII编码不能表示汉字，中国定制了`GB2312`编码；小于127的字符同ASCII码，两个大于127的字符连在一起，表示一个汉字；（原先`ACSII`中存在数字、标点、字母也重新进行了两字节编码，成为全角字符；原先`ASCII`中的叫半角字符）；
- **GBK**，对`GB2312`的扩展，包含`GB2312`的所有内容，同时又增加了近20000个新汉字和符号；汉字占两个字节；
- **Unicode**：对世界上大部分文字进行整理,编码,使得计算机可以使用更简单的方式处理文字. 通常用多个字节表示一个字符；会造成传输和存储的浪费；为解决浪费问题, 出现了UTF-8，UTF-16, UTF-32等编码方案；
- UTF-8，变长编码，使用1~4个字节表示一个符号；中文字符占3个字节（Unicode占2个字节）；用UTF-8 编码的文件会在打开时转为Unicode编码，保存和传输时还是UTF-8编码；
- 大小端:  大端: 高位字节排放在内存的低地址端, 小端: 低位字节排放在内存的低地址端; 

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

## II.技巧

- `locals() ` ：返回一个字典，包含了函数执行到该时间点时所有定义的一切变量，字典形似为，变量名称和值对应；在Django模版导入上下文时可能有用；(会比较大)

- 由` d = {True:'1', 1:'2', 1.0:'3'}  d[True]=?`引出的问题：
    -   答案为`'3' `，`True, 1, 1.0 `为相同的键值，后面的会覆盖前面的；
    -   字典判断为相同键值的条件：1.值是否相同（ `__eq__()`方法），2.哈希值是否相同（`__hash__()`方法返回相同值）；

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

    - **可用于遍历时同时得到其下标**

      ```python
      for index, x in enumerate(list_xx):
      ```

## III.实用函数

- `callable()`: 判断一个对象是否为可调用的, 是返回True,

- `itertools.chain()`:  将多个可迭代对象整合为一个迭代器,

## III.Python2和Python3不同点

- `print`语句
- 类, python2是旧式类, 需要显式继承`object`,  python3是新式类;
- 字符串类型: python2是`str, Unicode`, python3是`bytes, str`;

- 除法结果: python2中是整形, python3中是浮点型;