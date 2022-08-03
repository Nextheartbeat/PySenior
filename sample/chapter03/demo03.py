# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo03.py
# time: 2022/8/3 10:32
"""
    isinstance和type的区别
"""


class A:
    pass


class B(A):
    pass


b = B()
print(isinstance(b, B))
print(isinstance(b, A))

# type(b) is B 等价与 id(b) == id(B), 所以不会向上找, 会存在误差
# 类也是对象, 我们可以称为模板对象
print(type(b) is B)
print(type(b) is A)
