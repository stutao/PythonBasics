# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

"""
# 做完发现这个还挺简单的,,就是可能性能上跟不上.难道我开始进步了,很嗨.
class Solution:
    def plusOne(self, digits: list) -> list:
        # 是不是可以尝试先把完整的数字算出来?
        # 这个办法就比较麻烦了.
        n = len(digits)
        sum_ = 0
        for i in range(n):
            sum_ += digits[n-1-i]*(10**i)
        sum_ +=1
        return [int(x) for x in str(sum_)]

    def plusOne2(self, digits: list) -> list:
        # 尝试直接计算,反向操作一下
        n = len(digits)-1
        pos = n
        while pos >= 0:
            if digits[pos]==9:
                digits[pos] = 0
                pos -= 1
            else:
                digits[pos] +=  1
                break
        if pos==-1:
            digits.insert(0,1)
        return digits


if __name__ == '__main__':
    s =Solution()
    li = s.plusOne2([9,9,9,9,9,9])
    print(li)