# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: type_object_class.py
# time: 2022/8/2 11:13
"""type, object和class的关系"""

a = 1
print(type(1))
print(type(int))

b = "abc"
print(type(b))
print(type(str))

"""
    结论: type->int->1 (字符串同理)
         type->class->object
"""


class Person:
    pass


per = Person()
print(type(per))
print((type(Person)))  # 同理
"""type 生成了一个类的对象"""


class MyPerson(Person):
    """继承 Person"""
    pass


print(Person.__bases__)
print(MyPerson.__bases__)
"""
    .__bases__: 查看当前类的基类
    object 是最顶层的基类, 所有的类推到最后都是 Object 类
"""
# TODO: 离谱的事情出现了: type也是一个类, 同时type也是一个对象
print(type.__bases__)  # type的基类是 Object
print(type(object))  # Object 的类型是 type

# 问题出现了, 那 Obejct 的基类是什么呢
print(object.__bases__)  # 万物鼻祖, 没有爹
