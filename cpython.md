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
>     // 对象长度
>     Py_ssize_t ob_size;
> } PyVarObject;
> 
> ```

### 1.对象基础

#### 1.引用计数

> 通过 `Py_INCREF(op)` 和`Py_DECREF(op)`增加和减少引用计数

- `Py_DECREF(op)`: 减少引用计数, 当引用计数减少到0时, 调用`op->tp_dealloc`销毁对象;

#### 2.类型

- ```c
    typedef struct _typeobject {
        PyObject_VAR_HEAD
        // 类型名
        const char *tp_name;
        // 需要初始空间信息
        Py_ssize_t tp_basicsize, tp_itemsize;
    
        /* 实现标准操作的方法 */
    
        // 对象销毁函数
        destructor tp_dealloc;
    
        // 结构体, 包含一系列的数的操作, 加减乘除等
        PyNumberMethods *tp_as_number;
        // 结构体, 包含一系列的可迭代对象的操作, 长度, 替换, 取元素等
        PySequenceMethods *tp_as_sequence;
        PyMappingMethods *tp_as_mapping;
        ...
    } PyTypeObject;
    ```

- `PyObject`通过`struct _typeobject *ob_type;`定义对象的类型名称, 基本操作等;

- `PyTypeObject`最上部, 保存`PyObject_VAR_HEAD`, 是一个`PyVarObject`结构体, 表示类型也是一个对象;

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

### 2.内置类型

#### 1.整型

#### 2.List

#### 3.Dict

*******

## I.C语言回顾

- **函数指针**: `void (*pf)(char *)`, `pf`是一个指向函数的指针, 函数需要一个`char *`参数, 返回`void`类型;
- 