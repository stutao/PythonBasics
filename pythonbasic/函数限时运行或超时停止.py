# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"

面试的一家安全公司抛出的题
一个函数,只能运行五秒,怎么解决.

网上查资料,看到了timeout-decorator的包,试一下并看一下源码
"""

import time
from timeout_decorator import timeout


# 默认情况 限制当前进程当前函数
# windows中会报错AttributeError: module 'signal' has no attribute 'SIGALRM'
# 需要在linux下运行
@timeout(3)
def time_test():
    time.sleep(5)
    return 5


'''
默认情况下，timeout_decorator运用信号量来限制给定函数的执行时间。
如果你的函数不是在main线程中(例如是一个web应用的worker线程)执行，那么这个方法就不行了。
对这种情况有一个替代的超时策略---通过使用多进程。
为了使用它，只要将use_signals=False添加到timeout decorator函数中。
'''


@timeout(3, use_signals=False)
def mytest():
    time.sleep(5)
    return 5


if __name__ == '__main__':
    time_test()
