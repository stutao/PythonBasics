# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
"""
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''
class Solution(object):
    def twoSum(self, nums, target):
         # 原来参考的解法,执行结果出错,[3,3]在枚举的时候,其实字典中只有一个键值对.
        # 如果长度比1小,不存在结果
        # if len(nums)<=1:
        #     return []
        # # 通过hashmap映射结果
        # nums_index_map = {}
        # for index,num in enumerate(nums):
        #     nums_index_map[num] = index
        # for i in nums_index_map.keys():
        #     # 如果找到值并且下标不一样则返回
        #     if (target-i in nums_index_map) & (nums_index_map[i] != nums_index_map[target-i]):
        #         return [nums_index_map[i],nums_index_map[target-i]]
        #     else:
        #         continue
        # else:
        #     return []

         # 参考解法
        hashmap = {}
        for index,num in enumerate(nums):
            another_num= target-num
            # 在枚举过程中直接判断,如果出现重复,自然也可以直接返回相互的下标
            if another_num in hashmap:
                return [hashmap[another_num],index]
            hashmap[num]=index
        return []