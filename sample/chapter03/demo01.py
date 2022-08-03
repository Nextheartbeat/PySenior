# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo01.py
# time: 2022/8/3 9:51
"""
    鸭子类型和多态: 当看到一只鸟走起来像鸭子, 游泳起来像鸭子, 叫起来也像鸭子, 那么这只鸟就可以被称为鸭子
"""


class Cat(object):
    def say(self):
        print("i am a cat")


class Dog(object):
    def say(self):
        print("i am a dog")


class Duck(object):
    def say(self):
        print("i am a duck")


animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()
# 这就是多态

a = ["1", "2"]
b = ["2", "1"]
name_tuple = ("3", "4")
name_set = set()
name_set.add("5")
name_set.add("6")

a.extend(b)
print(a)
a.extend(name_tuple)
print(a)
a.extend(name_set)
print(a)
""" 
    Extend list by appending elements from the iterable. 
    通过从可迭代对象中追加元素来扩展列表
"""


class Person(object):
    def __init__(self, person_list):
        self.person_list = person_list

    def __getitem__(self, item):
        return self.person_list[item]


a = ["1", "2"]
person = Person(["3", "4", "5"])
a.extend(person)
print(a)
"""由此体现出 Python 与 静态语言的区别"""
