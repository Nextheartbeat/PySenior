# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo010  .py
# time: 2022/8/10 20:32
"""django rest framework 中对多继承使用的经验"""
# mixin 模式的特点
# 1. 功能单一
# 2. 不和基类关联, 可以和任意基类组合, 基类可以不和 mixin 关联就可以初始化成功
# 3. 在mixin中, 不要使用 super 用法, 使用 super 会按照 MRO 算法产生顺序关系
# 4. 设计之初可以 以 Mixin 结尾
