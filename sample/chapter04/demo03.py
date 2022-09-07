# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo03.py
# time: 2022/9/7 14:51
"""
    序列的 +, += 和 extend 的区别
"""

my_list = []
my_list.append(1)
my_list.append("a")
print(my_list)

# + : 类型要一致才能相加
a = [1, 2]
c = a + [3, 4]
print(c)

# +=: 就地加 原理: __iadd__ 序列类型:
a += (3, 4)  # 任意序列类型
a.extend(range(3))
print(a)
