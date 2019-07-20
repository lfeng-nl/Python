## 1.对象

> 对象的基础是类型`PyObject`, 但是多有对象都不是由其直接实现, 而是由类似`PyVarObject`这样的结构, 但是所有对象都可以强制转换为`PyObject 类型`,  也是一种继承机制;
>
> python所有对象, 都可以转换为`PyObject`进行传递, 调用(多态)
>
> ```c
> /* object.h */
> typedef struct _object {
>     _PyObject_HEAD_EXTRA
>     // 引用计数
>     Py_ssize_t ob_refcnt;
>     // 类型相关
>     struct _typeobject *ob_type;
> } PyObject;
> 
> /* 可变长对象 */
> typedef struct {
>     PyObject ob_base;
>     // 对象长度, 例如int类型, 记录需要 digit 个数
>     Py_ssize_t ob_size;
> } PyVarObject;
> 
> ```

### 1.对象基础

#### 1.引用计数

> 通过 `Py_INCREF(op)` 和`Py_DECREF(op)`增加和减少引用计数

- `Py_DECREF(op)`: 减少引用计数, 当引用计数减少到0时, 调用`op->tp_dealloc`函数, 销毁对象;

#### 2.类型

- ```c
    typedef struct _typeobject {
        PyObject_VAR_HEAD
        // 类型名
        const char *tp_name;
        // 需要初始空间信息, tp_basicsize: 对象需要的基本大小, tp_itemsize: 元素大小
        Py_ssize_t tp_basicsize, tp_itemsize;
    
        /* 实现标准操作的方法 */
    
        // 析构函数
        destructor tp_dealloc;
    
        // 结构体, 包含一系列的数的操作, 加减乘除等
        PyNumberMethods *tp_as_number;
        // 结构体, 包含一系列的可迭代对象的操作, 长度, 替换, 取元素等
        PySequenceMethods *tp_as_sequence;
        PyMappingMethods *tp_as_mapping;
        ...
        // 对象销毁函数
        vectorcallfunc tp_vectorcall;
} PyTypeObject;
    ```
    
- `PyObject`通过`struct _typeobject *ob_type;`定义对象的类型, 指定类型名称, 基本操作等;

- 地址最前, 保存`PyObject_VAR_HEAD`, 是一个`PyVarObject`结构体, 表示类型也是一个对象;

    - 对象的类型(如`str`)作为一个对象, 也会有类型, 会指向`PyType_Type`;

    - `PyType_Type`既是一个对象, 又是一个类型,  其类型指向自身, 实现如下:

    - ```c
        /* typeobject.c */
        PyTypeObject PyType_Type = {
        	// 初始化类型对象 PyVarObject 相当于: { {引用计数=1, 类型->PyType_Type}, 长度=0}
            PyVarObject_HEAD_INIT(&PyType_Type, 0)
            // 类型名
            "type",
        }
        ```

- `PyTypeObject`包还含若干函数指针, 最终会指向对象的对应操作的函数或`null`;

    - 如数类型的操作加减乘除, 迭代类型的操作, 遍历, 查找, 替换, 取元素等;
    
- `tp_dealloc`和`tp_free`:

    - `tp_dealloc`:
    - `tp_free`:低层级对象销毁函数;

### 2.内置类型

> 内置类型定义在"Objects"文件夹内, 

#### 1.整型

> ob_size: 绝对值表示需要的 ob_digit 个数, 负数: ob_size < 0, 零: ob_size == 0;
>
> ob_digit: 数值信息, 不含符号位, 长度由 ob_size决定, 符号由ob_size符号决定;

```c
// int 对象结构
struct _longobject {
    PyObject_VAR_HEAD
    digit ob_digit[1];
};
typedef struct _longobject PyLongObject;

// int 类型
PyTypeObject PyLong_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    "int",                                      /* tp_name */
    // 结构成员相对于结构开头的字节偏移量, 整体对象需要空间
    offsetof(PyLongObject, ob_digit),           /* tp_basicsize */
    // 元素需要空间
    sizeof(digit),                              /* tp_itemsize */
    ...
    // 数学方法
    &long_as_number,                            /* tp_as_number */
    // 哈希方法
    (hashfunc)long_hash,                        /* tp_hash */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE |
        Py_TPFLAGS_LONG_SUBCLASS,               /* tp_flags *

    long_new,                                   /* tp_new */
    PyObject_Del,                               /* tp_free */
};
```

- 空间申请: `_PyLong_New(size)`, 按照`PyLongObject`大小 + 指定数量的`digit` 申请空间;
- 数据储存: 数值15位位单位切割, 保存在一个`digit`中, `digit`为 2个字节, 最高位空出;
  - *为什么最高位空出*? 
    1. 相加时, 最高位保存进位;
    2. 相乘时, 结果可以保存到`long int`中;
- 关键函数:
  - 数学方法: 加减乘除, 会对运算进程优化, 例如乘法: 当`ob_size`均小于等于1时(结构可以存放在`long`或`long long`中), 直接相乘, 其余使用`Karatsuba `乘法;
  - 转为字符串: `long_to_decimal_string`;
  - 哈希函数: `long_hash`;
- python会将-5~256的小整数直接创建保存, 避免频繁申请回收, 保存在`static PyLongObject small_ints[NSMALLNEGINTS + NSMALLPOSINTS];`数组中;  通过`get_small_int()`直接获取小整数对象;

#### 2.str

> 

```c
// unicode字符串对象
typedef struct {
    PyCompactUnicodeObject _base;
    union {
        void *any;
        Py_UCS1 *latin1;
        Py_UCS2 *ucs2;
        Py_UCS4 *ucs4;
    } data;                     /* Canonical, smallest-form Unicode buffer */
} PyUnicodeObject;

PyTypeObject PyUnicode_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    "str",                        /* tp_name */
    sizeof(PyUnicodeObject),      /* tp_basicsize */
    0,                            /* tp_itemsize */
    /* Slots */
    (destructor)unicode_dealloc,  /* tp_dealloc */
    0,                            /* tp_vectorcall_offset */
    0,                            /* tp_getattr */
    0,                            /* tp_setattr */
    0,                            /* tp_as_async */
    unicode_repr,                 /* tp_repr */
    &unicode_as_number,           /* tp_as_number */
    &unicode_as_sequence,         /* tp_as_sequence */
    &unicode_as_mapping,          /* tp_as_mapping */
    (hashfunc) unicode_hash,      /* tp_hash*/
    0,                            /* tp_call*/
    (reprfunc) unicode_str,       /* tp_str */
    PyObject_GenericGetAttr,      /* tp_getattro */
    0,                            /* tp_setattro */
    0,                            /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE |
    Py_TPFLAGS_UNICODE_SUBCLASS,   /* tp_flags */
    unicode_doc,                  /* tp_doc */
    0,                            /* tp_traverse */
    0,                            /* tp_clear */
    PyUnicode_RichCompare,        /* tp_richcompare */
    0,                            /* tp_weaklistoffset */
    unicode_iter,                 /* tp_iter */
    0,                            /* tp_iternext */
    unicode_methods,              /* tp_methods */
    0,                            /* tp_members */
    0,                            /* tp_getset */
    &PyBaseObject_Type,           /* tp_base */
    0,                            /* tp_dict */
    0,                            /* tp_descr_get */
    0,                            /* tp_descr_set */
    0,                            /* tp_dictoffset */
    0,                            /* tp_init */
    0,                            /* tp_alloc */
    unicode_new,                  /* tp_new */
    PyObject_Del,                 /* tp_free */
};
```



#### 3.List

```c
// list对象
typedef struct {
    PyObject_VAR_HEAD
    /* 指向PyObject数组的指针 */
    PyObject **ob_item;

    /* allocated:申请的总空间,  ob_size 表示当前已使用空间 */
    Py_ssize_t allocated;
} PyListObject;

PyTypeObject PyList_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    "list",
    sizeof(PyListObject),
    // 
    (destructor)list_dealloc,                   /* tp_dealloc */
	// 迭代相关函数
    &list_as_sequence,                          /* tp_as_sequence */
    &list_as_mapping,                           /* tp_as_mapping */
    PyObject_HashNotImplemented,                /* tp_hash */
    
    (initproc)list___init__,                    /* tp_init */
    PyType_GenericAlloc,                        /* tp_alloc */
    PyType_GenericNew,                          /* tp_new */
    PyObject_GC_Del,                            /* tp_free */
};
```



#### 4.Dict

*******

## I.C语言回顾

- **函数指针**: `void (*pf)(char *)`, `pf`是一个指向函数的指针, 函数需要一个`char *`参数, 返回`void`类型;

- 类型长度:

	| 类型          | 32位 | 64位 |
  | ------------- | ---- | ---- |
  | **char**      | 1    | 1    |
  | **short**     | 2    | 2    |
  | **int**       | 4    | 4    |
  | **long**      | 4    | 8    |
  | **long long** | 8    | 8    |
  | **float**     | 4    | 4    |
  | **double**    | 8    | 8    |
  | **point**     | 4    | 8    |

    