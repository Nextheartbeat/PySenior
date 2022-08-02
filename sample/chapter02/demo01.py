# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo01.py
# time: 2022/8/2 11:13
"""
什么是魔法函数
    1. 双下划线开头, 双下划线结尾
    2. 对类进行强化, 的操作
    3. 魔法函数真的会影响Python的语法, 也让我们看清了, 类的本质
"""


# 不使用魔法函数
# class Person(object):
#     def __init__(self, employee_list):
#         self.employee_list = employee_list
#
#
# person = Person(["ls", "hcl", "ls"])
# employee = person.employee_list˚
# for em in employee:
#     print(em)

# 使用魔法函数
class Person(object):
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def __getitem__(self, item):  # 兑现序列化
        return self.employee_list[item]


person = Person(["ls", "hcl", "ls"])
print(person[:2])

for em in person:
    print(em)

"""
    __getitem__(self, item): 魔法方法
    1. 如果 for 循环类对象, 解释器会寻找 __getitem__ 方法, 如果找到, for循环会尝试便利值, 直到抛出异常循环结束
    2. 如果 类没有 __getitem__ 魔法方法, 抛出异常: TypeError: 'Person' object is not iterable (Person类 是不可迭代的)
"""