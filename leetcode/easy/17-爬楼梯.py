# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""


# 先用暴力法试试--数学内容方式
# 算式 n = 2x+y
# n 是目标台阶,x是跳2阶的次数,y是对应跳1阶的次数.
# 最后的结果是超时了.可能排列出来的数组长度可以有个规律.

# ????还可以发现是斐波那契数列???受教了.

class Solution:
    def climbStairs(self, n: int) -> int:
        from itertools import permutations
        # if n <=1:
        #     return 1
        # x的取值范围是[0,n//2]
        x = [i for i in range((n // 2) + 1)]
        # 对应的y的值
        y = [n - 2 * i for i in x]
        res = 0
        for i in range(len(x)):
            li = [2] * x[i] + [1] * y[i]
            count = x[i] + y[i]
            res += len(set(permutations(li, count)))
        return res

    # 开始参考题解大法
    # 第一个是采用了递归树的方法.没看怎么懂,
    # https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode/

    def climbStairs1(self, n: int) -> int:
        return self.climb_Stairs(0, n)

    def climb_Stairs(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        # 相当于是每一步往下试探,climb_Stairs(i+1,n) 代表第一步走1后面的情况1步或者2步
        # 同理 可以构造出一个所有情况的树,返回所有i==n的节点数
        return self.climb_Stairs(i + 1, n) + self.climb_Stairs(i + 2, n)

    # 后面还有一个记忆递归...更懵了

    # 采用动态规划的方式--
    def climbStairs_dp(self, n: int) -> int:
        if n < 3:
            return n
        dp = [1] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    x = s.climbStairs_dp(5)
    print(x)
