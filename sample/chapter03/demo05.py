# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo05.py
# time: 2022/8/3 10:32
"""类属性和实例属性以及查找顺序-MRO算法"""

# class A:
#     name = "A"
#
#     def __init__(self):
#         self.name = "obj"
#
#
# a = A()
# print(a.name)

"""
    python 2.2 之前对于继承的优先算法采用的是 DFS: 深度优先算法
    python 2.3 采用的是: BFS: 广度优先算法
    python 2.3 之后采用 C3 算法
"""


# class D:
#     pass
#
#
# class C(D):
#     pass
#
#
# class B(D):
#     pass
#
#
# class A(C, D):
#     pass


# 完美的 菱形继承关系, 我们可以通过 __mro__ 查看继承的查找顺序
# print(A.__mro__)  # (<class '__main__.A'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)


class D:
    pass


class E:
    pass


class B(D):
    pass


class C(E):
    pass


class A(B, C):
    pass


print(A.__mro__)
# (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>,
# <class '__main__.C'>, <class '__main__.E'>, <class 'object'>)

"""结论: C3算法, 完美的解决了, 多继承中查找顺序问题"""
