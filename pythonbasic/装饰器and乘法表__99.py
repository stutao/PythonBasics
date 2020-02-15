# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
"""
# 本质是函数，内层函数返回，可以用warps装饰内函数，让其__name__还是原来的

from functools import wraps

def deco(func):
    print("装饰外部函数")
    # @wraps(func)
    @wraps(func)
    def inner():
        func()
        return "内部函数"
    return inner


@deco
def myfunc():
    print("myfunc")


# myfunc = deco(myfunc)

t = myfunc.__name__
print(t)

if __name__ != '__main__':
    # for实现99乘法表
    for i in range(1,10):
        for j in range(1,i+1):
            print(f'{j}*{i}={i*j}',end=" ")
        print()

    # 递归实现99乘法表
    def multiplication_table(n):
        # 如果小于1,结束递归
        if n < 1:
            return
        # 将数字先进行锐减入栈到1,后续开始出栈,
        multiplication_table(n - 1)
        # n的取值从1开始到9
        for m in range(1, n + 1):
            print("%d*%d=%d" % (m, n, m * n), end="\t")
        print()

    multiplication_table(9)
    # 一行代码实现99乘法表
    # print('\n'.join(['\t'.join(["%2s*%2s=%2s" % (j, i, i * j)
    #                             for j in range(1, i + 1)]) for i in range(1, 10)]))
