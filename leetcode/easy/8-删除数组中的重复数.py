# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"

删除重复数字,返回操作后的数组长度,并在O(1)的额外空间下完成原数组的修改,

看了题目发现可以不要考虑最后的数组是什么样得?
比如开始是[1,2,2,3,3,4,5,5,6],
最后可以是[1,2,3,4,5,6,.....]后面的可以不要管是什么?这样我或许可以再挣扎一下
"""
# # 暴力解法...还用了in 比较low 花了3000多ms,继续修改
# class Solution:
#     def removeDuplicates(self, nums: list) -> int:
#         for i in range(len(nums)):
#             x = nums.pop()
#             if x not in nums:
#                 nums.insert(0,x)
#         return len(nums)

#借鉴题解大神双指针写法,附加自己理解,
# 在本解法中,pos是一个慢指针,呈现跳跃性,for是一个快指针,随着遍历数组的速度进行
# 本解法应该是只适合有序数组的时候.从pos指针所指的位置占位可以看出,并不要考虑后面会有相同的可能.
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        # 我们现在不要管数组是否符合条件,先把重复啥的搞定
        # 先遍历
        # 既然是要从开头开始把整个数组重新改变,那需要一个起始位置
        pos = 0
        for i in nums:
            if nums[pos] != i:
                # 如果这个位置的值和nums其他位置的所有值都不一样,那么代表这个位置的值是需要的
                # 这个时候我们将指针pos的值加1操作,继续对后续的数字进行对比
                pos += 1
                # 这步操作的意思是将pos的位置用不同元素进行占用.这个感觉只适合当前有序排列数组的情况下.
                nums[pos] = i

        return len(nums) and pos + 1





if __name__ == '__main__':
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    n = s.removeDuplicates(nums)
    print(n)
    print(nums)


