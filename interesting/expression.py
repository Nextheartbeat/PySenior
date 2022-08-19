# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: expression.py
# time: 2022/8/18 15:49
"""条件表达式"""


def test_value(value):
    if value < 100:
        return "The value is just right."
    else:
        return "The value is too big!"


print(test_value(55))
print("---------华丽的分割线---------")


def _test_value(value):
    return "The value is " + ("just right." if value < 100 else "too big!")


print(_test_value(55))
print("---------华丽的分割线---------")


def __test_value(value):
    """
        and: 如果左侧为True 返回右侧的值, 否则返回 False
        or:  如果左侧为True 返回左侧的值, 否则返回右侧的值
    :param value:
    :return:
    """
    return "The value is " + (value < 100 and 'just right.' or 'too big!')


print(__test_value(999))
print("---------华丽的分割线---------")
