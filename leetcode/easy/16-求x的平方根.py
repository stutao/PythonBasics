# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
"""
# 不怎么知道怎么计算平方根计算方法.

class Solution:
    def mySqrt(self, x: int) -> int:
        from math import e,log
        if x < 2:
            return x

        left = int(e ** (0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right


if __name__ == '__main__':
    pass

