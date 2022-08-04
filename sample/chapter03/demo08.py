# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo08.py
# time: 2022/8/4 9:32
"""python对象的自省机制"""


# 自省是通过一定的机制查询到对象的内部结构

class Person:
    """人类"""
    name = "user"


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == '__main__':
    user = Student("tju")

    # 通过 __dict__ 查询属性: 是有 C语言编写, cpython 编译, 由于比较重要, 所以解释器对此进行了优化
    print(user.__dict__)
    # 我们也可以通过 字典添加的方式 操作 __dict__
    user.__dict__["school_addr"] = "天津"
    print(user.school_addr)
    print(user.name)
    print(Person.__dict__)
    """
    {
    '__module__': '__main__', 
    '__doc__': '人类',  doc: : """"""中注释
    'name': 'user', 
    '__dict__': <attribute '__dict__' of 'Person' objects>, 
    '__weakref__': <attribute '__weakref__' of 'Person' objects>  weakref: 弱引用
    }
    """
    # TODO 还有比 __dict__ 更加强大的函数
    print(dir(user))  # 可以查看类中的所有属性

    a = [1, 2]
    # print(a.__dict__)  # AttributeError: 'list' object has no attribute '__dict__'
    print(dir(a))
