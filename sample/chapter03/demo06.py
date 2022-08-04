# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo06.py
# time: 2022/8/3 15:32
"""静态方法, 类方法以及对象方法 以及参数"""


class Date(object):

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    @classmethod
    def parse_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))

    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split("-"))
        if int(year) > 0 and int(month) <= 12 and int(month) > 0 and int(day) <= 31 and int(day) > 0:
            return True
        else:
            return False

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)


if __name__ == '__main__':
    new_day = Date(2022, 8, 3)
    print(new_day)
    new_day.tomorrow()
    print(new_day)

    # 如果添加字符串改怎么办: 2022-08-03
    date_str = "2022-08-03"
    year, month, day = tuple(date_str.split("-"))
    new_day_2 = Date(int(year), int(month), int(day))
    print(new_day_2)

    # 如果使用静态方法来实现初始化, 就很简单了, 但是存在弊端, 如果类名发生改变, return 回时调用的类名也会改变
    new_day_3 = Date.parse_from_string(date_str)
    print(new_day_3)

    # 所以衍生出了, 静态类方法
    new_day_4 = Date.parse_string(date_str)
    print(new_day_4)

    # 如果在方法中, 不需要使用类的话, 那么静态方法就会很好用
    print(Date.valid_str("2022-08-03"))