# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo04.py
# time: 2022/8/3 10:32
"""类变量和实例变量(对象变量)"""


class A:
    aa = 1  # 类变量

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(2, 3)
A.aa = 11
a.aa = 12  # TODO 赋值给实例, 而不是给类 . a.aa: 在实例中找到, 就不会向上找了, A.aa 不变
print(a.x)
print(a.y)
print(a.aa)  # 实例访问 类变量向上查找

print(A.aa)
# print(A.x)  # AttributeError: type object 'A' has no attribute 'x'

"""
    类变量是所有实例共享的, 类发生修改, 实例获取类变量也会被修改
    TODO 结论: 不要随便修改类变量
"""
