# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: while_optimize.py
# time: 2022/8/18 15:49
"""
while循环优化
    通常, while 被用于检查循环过程中可能发生的条件, 一旦条件计算为 false , 就可以跳出循环体,
当条件太复杂而无法提取为单个表达式时, 或由于异常而导致循环被破坏时,
更有意义的做法是始终保持while表达式为true, 并且在适当的时候使用 break 语句来结束循环
    尽管任何计算结果为 true 的表达式都会产生预期的效果, 但也可以使用特定的值来表示,
从而使其变的更好, Python 知道真值将始终计算为 true , 因此在后台进行了一些额外的优化来加速循环,
从本质上讲, 甚至不需要没次都检测条件, 而只是无限期地在循环中执行代码, 直至遇到异常, break 语句或 return 语句
"""


def echo():
    """Returns everything you type nutil you press Ctrl-C"""

    while True:
        try:
            print(input('Type Something or CTRL C to exit: '))
        except KeyboardInterrupt:
            print()  # Make sure the prompt appears on a new line
            print("bye for now ...")
            break


if __name__ == '__main__':
    echo()
