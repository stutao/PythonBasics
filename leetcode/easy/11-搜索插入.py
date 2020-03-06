# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"

"""

'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
'''


#
# 第一想法暴力法或者是二分查找.
class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        # 先写暴力破解的-提交通过
        # 数组有序.
        for i, n in enumerate(nums):
            if target == n:
                return i
            elif target < n:
                nums.insert(i, target)
                return i
            else:
                if i == len(nums) - 1:
                    nums.append(target)
                    return i + 1

    def searchInsert1(self, nums: list, target: int) -> int:
        # 二分查找的方式-提交通过,可是咋比前面的还慢呢..尴尬
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        # 最后的时候mid基本都是步长为1,可以看出high比low小1.
        # 再结合实际序列,low的位置就是需要的插入位置,
        # 有个问题是,insert末尾元素的时候是不是调用了append?
        nums.insert(low, target)
        return low


if __name__ == '__main__':
    s = Solution()
    li = [1, 2, 4, 5, 7, 9]
    i = s.searchInsert1(li, 0)
    print(i)
    print(li)
