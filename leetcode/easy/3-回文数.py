# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
"""

'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:
你能不将整数转为字符串来解决这个问题吗？

'''

# 总体思路和第二题整数反转基本相同

# 可以显示声明形参类型和函数返回值类型了
# 字符串的处理方式有多个
# 方法一:x[::-1] 和 x 的比较
# 方法二: 反转每一位数 进行比较 如下x[0] == x[-1] x=x[1:-1]

def ishuiwen(x: int) -> bool:
    # 最简单的方式 将x转变为字符串
    if x < 0:
        return False
    elif 0 < x < 10:
        return True
    else:
        x = str(x)
        while len(x)>=1:
            if x[0] == x[-1]:
                x = x[1:-1]
            else:
                return False
        return True
# 整数题解方式
# 方法一:官方题解  '12321'截取后面一半进行反转 与前面一半做对比
        # 主要差别在比较上
        # cur=0
        # while x > cur:
        #     cur = cur*10 + y%10
        #     x //= 10
        # 解释:x<cur的时候 那就是要么位数相等实际比cur小,要么就是位数少了一位
# 方法二:如下所示
def ishuiwen_int(x:int) ->bool:
    if x<0:
        return False
    elif 0< x <10:
        return True
    else:
        cur,y=0,x
        while y != 0:
            cur = cur*10 + y%10
            y //= 10
        return cur==x

if __name__ == '__main__':
    print(ishuiwen_int(322222223))