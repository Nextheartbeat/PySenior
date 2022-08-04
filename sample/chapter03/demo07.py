# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo07.py
# time: 2022/8/4 9:32
"""数据封装和私有属性"""
from demo06 import Date


class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2022 - self.__birthday.year


if __name__ == '__main__':
    user = User(Date(1999, 2, 14))
    # print(user.__birthday)  # 我们现在是可以直接获取出生日期的, 如果想隐藏掉, 我们需要使用双下滑线
    """原理是如何实现的呢"""
    # 是把类中带有双下划线的属性前加 _classname 就像这样
    print(user._User__birthday)  # 还是可以实现的
    print(user.get_age())
