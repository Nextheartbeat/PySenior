# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: all_is_object.py
# time: 2022/8/2 11:13
"""python 中一切皆对象"""


def ask(name="bobby"):
    print(name)


class Person(object):
    def __init__(self):
        print("bobby")


def decorator_func():
    """
        TODO  函数可以返回函数, 是装饰器的原理
    :return: ask()
    """
    print("dec start")
    return ask


if __name__ == '__main__':
    my_func = ask
    my_func("wjw")
    print("---------->华丽的分割线<----------")
    my_class = Person
    my_class()
    print("---------->更加华丽的分割线<----------")
    object_list = []
    object_list.append(ask)
    object_list.append(Person)
    for item in object_list:
        print(item())
    print("---------->比更加华丽还华丽的分割线<----------")
    my_ask = decorator_func()
    my_ask("tom")
