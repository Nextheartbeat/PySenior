# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo08.py
# time: 2022/8/4 14:32
"""super 真的是调用父类吗?"""

# class A(object):
#     def __init__(self):
#         print("A")
#
#
# class B(A):
#     def __init__(self):
#         print("B")
#         # super(B, self).__init__()  # python2 中的写法
#         super().__init__()


from threading import Thread


class MyThread(Thread):
    def __init__(self, name, user):
        self.user = user
        # 我们可以选择我们需要的参数, 进行传递, 避免代码重用
        super(MyThread, self).__init__(name=name)


class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super(B, self).__init__()


class C(A):
    def __init__(self):
        print("C")
        super(C, self).__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super(D, self).__init__()


if __name__ == '__main__':
    # b = B()  # B
    # 出现问题
    # 1. 既然重写了B的构造函数, 为什么还要去调用 super
    # 2. super到底执行顺序是什么样的
    d = D()  # D B C A
    """super 真的是调用父类吗?"""
    # 答案是 No super 掉用的顺序和 取决于 mro 算法 调用的顺序
    print(D.__mro__)