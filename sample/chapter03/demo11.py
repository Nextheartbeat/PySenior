# !/usr/bin/env python3.9
# encoding: utf-8
# author: nextHeartbeat
# software: pycharm
# file: demo011.py
# time: 2022/8/10 20:32
"""python中的上下文管理器"""

# 首先我们需要重温一下 try except else finally
try:
    print("code started")
    raise KeyError
except KeyError as e:
    print("key error")
# 我们预估到异常, 进行提前捕获, 如果未预测到异常呢?
print("---------------华丽的分割线---------------")
try:
    print("code started")
    # raise IndexError
except KeyError as e:
    print("key error")
else:
    # else: 如果未发现异常, 会执行
    print("other error")
finally:
    # finally: 不管前面如何都会执行 TODO: 那么finally 存在的意义是什么呢
    print("finally")
print("---------------华丽的分割线---------------")


# 如果说我们需要打开一个文件使用 open 实时上 是否出现报错, 我们都需要将资源释放掉, 我们无需在每一环后都添加 .close
#  try except else finally 的执行顺序
def exec_try():
    try:
        print("code started")
        raise IndexError
        return 1
    except KeyError as e:
        print("key error")
        return 2
    else:
        # else: 如果未发现异常, 会执行
        print("other error")
        return 3
    finally:
        # finally: 不管前面如何都会执行                   TODO: 那么finally 存在的意义是什么呢
        print("finally")
        return 4


print(exec_try())  # 4
"""
    为什么会是 4 而 不是 2 呢? 原因: 从上到下一次执行, 执行过程中 return 会被加到堆栈中去, 直到最后 finally 执行结束, 函数返回时, 
    会从栈顶开始找, 一次向下, 如果吧 finally 中 return注释掉, 则会返回 2
"""

print("---------------华丽的分割线---------------")


# TODO 上面的这些, 不重要, 看这里
# TODO 上下文管理器
# 上下文管理器协议: 所谓上下文管理, 也就是说, 在执行开始, 以及执行结束, 分别做的处理, 可以当做, TODO 加载资源, 和资源释放
# 魔法函数: __enter__ __exit__
class Sample(object):
    def __enter__(self):
        print("enter")  # 资源加载
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def do_something(self):
        print("doing something")  # 资源释放


with Sample() as sample:
    sample.do_something()
