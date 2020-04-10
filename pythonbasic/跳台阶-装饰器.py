# -*- coding:utf-8 -*-
# /usr/anaconda3/bin/python3
# @ DATE: 2020/4/2
# @ Author: TomTao
# @ PRODUCT_NAME: PyCharm

# 补充代码，完成以下题目：
# 一个台阶总共有n级，如果一次可以跳1级，也可以跳2级。求总共有多少总跳法。
#  
#  
from functools import wraps


def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap

@memo
def jump(n):
    if (n <= 0):
        return 0
    elif (1 == n):
        return 1
    elif (2 == n):
        return 2
    return jump(n - 1) + jump(n - 2)
