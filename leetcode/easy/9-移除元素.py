# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
给一个无序数组和值,删除数组中和这个值相同的元素,O(1)额外空间--原地修改.并返回新长度,
和删除重复数的题目一样不要考虑数组之后的长度.-同时不考虑元素顺序
如[1,1,2,3,4,5,4] val=4
返回5,数组前5个是[1,1,2,3,5,.......]
"""


# 这个数组是无序的,
# 思路,直接暴力法,是否可以找到对应数值的下标做删除,
# 这里就不能使用列表的remove方法了,不然就没有意义了.同时remove也只是移除出现的第一个元素
# 运行之后发现未通过,主要问题出在pop上,每次pop之后原数组会改变,相应的数据对应的下标也出现了错误.
# 如[0,1,2,2,3,0,4,2],val=2 本解法输出结果[0,1,2,3,0,4] 实际需要的结果为[0,1,3,0,4]


# class Solution:
#     def removeElement(self, nums: list, val: int) -> int:
#         if len(nums) <= 1:
#             return len(nums)
#         for i in range(len(nums) - 1):
#             if nums[i] == val:
#                 # 感觉这里pop有一个O(n)了,前面循环又有一个.性能估计就不好了
#                 nums.pop(i)
#         return len(nums)


# 改进一下用别的办法,试试看可不可以再次使用双指针的方法,成功通过 根据题解还可以再改进
# class Solution:
#     def removeElement(self, nums: list, val: int) -> int:
#         pos = 0
#         for n in nums:
#             if n != val:
#                 nums[pos] = n
#                 pos += 1
#         return len(nums) and pos

# 可以不考虑元素的顺序,按照题解思路和最后位置交换顺序?
# 发现还没前面那个快..,尴尬了,感觉有很多其他关系啊 相同代码提交好几次好几次不一样的
class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        # pos = len(nums)
        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         nums[i] = nums[pos-1]
        #         pos -= 1
        # return len(nums) and pos
        # 一开始很困惑为什么这两个不一样
        # 有点蒙了 后来发现这个在while里面如果有了相等的元素换位了之后,还会再次遍历一遍.
        # 而for就不管了 直接会开始+1操作,
        i = 0
        pos = len(nums)
        while i < pos:
            if nums[i] == val:
                nums[i] = nums[pos - 1]
                pos -= 1
            else:
                i += 1
        return len(nums) and pos


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    print(s.removeElement(nums, val=2))
    print(nums)
