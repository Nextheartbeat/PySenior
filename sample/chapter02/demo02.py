# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo02.py
# time: 2022/8/2 11:13
"""魔法函数一览: 后续代码会有详细样例
    非数学运算:
        1.字符串表示:
            __repr__
            __str__
        2.集合序列相关:
            __len__
            __getitem__
            __setitem__
            __delitem__
            __contains__
        3.迭代相关
            __iter__
            __next__
        4.可调用的
            __call__
        5.with上下文管理器
            __enter__
            __exit__
        6.数值转换
            __abs__
            __bool__
            __int__
            __float__
            __hash__
            __index__
        7.元类相关
            __new__
            __init__
        8.属性相关
            __getattr__, __setattr__
            __getattribute__, __setattribute__
            __dir__
        9.属性描述符
            __get__, __set__, __delete__
        10.协程
            __awaite__, __aiter__, __anext__, __aenter__, __aexit__

    数学运算(比较离谱, 不搞算法整的很少用到):
        1. 一元运算符: __neg__(-), __pos__(+), __abs__
        2. 二元运算符: __it__(<), __le__<=, __eq__==, __ne__!=, __gt__>, __ge__>=
        3. 算数运算符: __add__+, __sub__, __mul__*, __truediv__/, __floordiv__//,
                     __mod__%, __divmod__ 或 divmod(), __pow__或 pow(), __round__ 或 round()
        4. 反向算数运算符: __radd__, __rsub__, __rmul__, __rmul__, __rtruediv__, __rfloordiv__, __rmod__,
                        __rdivmod__, __rpow__
        5. 增量赋值算术运算符: __iadd__, __isub__, __imul__, __itruediv__, __ifloordiv__, __imod__, __ipow__
        6. 位运算符: __invert__~, __lshift__<<, __rshift__>>, __and__&, __or__|, __xor__^
        7. 反向位运算符: __rlshift__, __rrshift__, __rand__, __rxor__, __ror__
        8. 增量赋值位运算符: __ilshift__, __irshift__, __iand__, __ixor__, __ior__
"""


# 字符串表示:
#   __str__: 功能与 Java中的 toString() 一致
#   __repr__: 同理, 在 IDEA 中体现效果不好, 但在解释器中可直接输出对象


class Person(object):
    def __init__(self, em_list):
        self.em_list = em_list

    # def __str__(self):
    #     return "[" + ",".join(self.em_list) + "]"

    def __repr__(self):
        return "[" + ",".join(self.em_list) + "]"


person = Person(["ls", "zs", "hcy"])
print(person)  # [ls,zs,hcy] 如果没有 __str__ 输出内存地址: <__main__.Person object at 0x7fa38521bfd0>


# 数学运算符: __abs__(绝对值的转换)
#           __add__(对象相加)
class Nums(object):
    def __init__(self, num):
        self.num = num

    def __abs__(self):
        return abs(self.num)


my_num = Nums(1)
print(my_num.__abs__())
print(abs(my_num))  # 同上


class MyVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return MyVector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return "x: {x}, y: {y}".format(x=self.x, y=self.y)


first_vec = MyVector(1, 2)
secoud_vec = MyVector(2, 3)
print(first_vec+secoud_vec)
