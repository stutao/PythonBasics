# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

"""

# 我真的是没想出来..看题解用动态规划,,什么叫动态规划我还一脸懵
# 先把答案转化一下成为python理解一下
class Solution:
    def maxSubArray(self, nums: list) -> int:
        if not nums:
            return 0
        # for i in range(1, len(nums)):
        #     nums[i] = nums[i] + max(nums[i - 1], 0)
        # return max(nums)
        # 用ans来存储一个初始值,
        ans = nums[0]
        # 用sum_来保存和
        sum_ = 0
        # 接下去就是题解说的神奇的正数增益
        for num in nums[1:]:
            # 如果目前的sum_是>0的,加上后面一个数可能变大,也可能变小
            if sum_ > 0:
                sum_ += num
            else:
                # 如果现在sum_是<0的,那么意味着最大序列可能在后面,将当面num赋值sum_
                sum_ = num
            # 比较ans和sum_的值,取到求中的最大值,每次循环都比较一遍,
            # 保证最后保存的是其中的更大的值
            ans = max(ans,sum_)
        return ans




if __name__ == '__main__':
    s =Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums))
