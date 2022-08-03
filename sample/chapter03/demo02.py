# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo01.py
# time: 2022/8/3 10:32
"""
    抽象基类(abs模块):
"""


# 我们可以去检测某个类是否有某种方法

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

    def a(self):
        pass


com = Company(["1", "2", "3"])
print(hasattr(com, "__len__"))
print(hasattr(com, "b"))  # 这就是 hasattr 的作用

from collections.abc import Sized

print(isinstance(com, Sized))  # 使用 isinstance 效果如上


# 问题:
# 我们需要强制某个子类必须实现某些方法
# 实现了一个web框架, 继承cache(redis, cache, memorychache)

# 如何去模拟一个抽象类
class CacheBase(object):
    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError


# class RedisCache(CacheBase):
#     pass
#
#
# redis_cache = RedisCache()
# redis_cache.get("A")  # 未重写方法, 会主动抛出异常,间接的实现了, 抽象类 NotImplementedError: 自定义异常
class RedisCache1(CacheBase):
    def get(self, key):
        pass

    def set(self, key, value):
        pass


redis_cache = RedisCache1()
redis_cache.get("a")  # 重写后

import abc
from collections.abc import *


# 抽象类的正确写法
class CacheBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


# cache_base = CacheBase()  # TypeError: Can't instantiate abstract class CacheBase with abstract methods get, set


class A(object):
    pass


class B(A):
    pass


b = B()
print(isinstance(b, A))  # isinstance 还可以向上找

"""抽象类, 不推荐使用, 只是为了加深理解, 多继承的方式实现功能为最佳"""
