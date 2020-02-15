# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
"""

'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0。
'''


# 第一种最为简单的  转换成字符串进行
def reverse_integer_as_str(x):
    if x < 0:
        x = str(x)
        # x是否溢出就不好判断了
        return -int(x[::-1])
    else:
        x = str(x)
        return int(x[::-1])


# 可以用位移的方式
# boundry = (1<<31) -1  ...  1<<31
def reverse_integer_(x):
    q = abs(x)
    cur = 0
    while q != 0:
        cur = cur * 10 + q % 10
        q //= 10
    if not -2 ** 31 <= cur <= 2 ** 31 - 1:
        return 0
    elif x < 0:
        return -cur
    else:
        return cur


# leetcode大佬写法
def reverse_better(self, x):
    y, res = abs(x), 0
    # 则其数值范围为 [−2^31,  2^31 − 1]
    boundry = (1 << 31) - 1 if x > 0 else 1 << 31
    while y != 0:
        res = res * 10 + y % 10
        # 在里面就进行判断  说不定中途已经超过了
        if res > boundry:
            return 0
        y //= 10
    return res if x > 0 else -res


if __name__ == '__main__':
    # print(reverse_integer_(-1384889787))
    print(1<<31)
    pass
