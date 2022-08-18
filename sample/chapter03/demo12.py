# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo12.py
# time: 2022/8/12 20:32
"""contextlib 简化上下文管理器"""
import contextlib


@contextlib.contextmanager
def file_open(file_name):
    print("file_open:", file_name)  # __enter__: 作用一样
    yield {"data": "data"}
    print("file end")  # __exit__: 作用一样


with file_open("bobby.txt") as f:
    print(f)
    print("file processing")

"""
执行结果:
file_open: bobby.txt
file processing
file end
巧妙的利用了 生成器的特性
"""