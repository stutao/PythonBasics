# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"

给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，
使 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

"""
# 这个是用了内置方法.看了题解了解到了多指针法,采用nums1[:]=..这个是在nums1上修改,
# 而采用nums1 = ..这样其实不是在nums1上进行修改了
class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 这个写法虽然通过了,但是不严谨,比如说可能nums1会有一些其他的噪音元素在里面.
        for index,num in enumerate(nums2[:n]):
            nums1[index+m] = num
        # 改成这行可能会好点
        nums1[:] = sorted(nums1[:m+n+1])

    # 类似于归并排序,最后给出了三个指针,两个指针用来比较大小,一个指针用来确定位置
    def merge1(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n ==0:
            # n==0的时候nums1无需改变
            pass
        elif m == 0:
            # m == 0时候 nums1=nums2
            # 切片过界不会引起IndexError
            nums1[:n] = nums2[:n]
        else:
            a,b = m-1,n-1
            k = m+n-1
            while a>=0 and b >=0:
                # 首先我们知道 nums1和nums2是有序的
                if nums1[a] < nums2[b]:
                    nums1[k] = nums2[b]
                    k -= 1
                    b -= 1
                else:
                    nums1[k] = nums1[a]
                    k -= 1
                    a -= 1
            # 如果退出循环a>0,代表b<0,也就是nums2处理完了,剩下的nums1中的内容无需改变
            if a >= 0:
                pass
            # 这里是代表nums1遍历完了,也就是说nums2剩下的直接copy到nums1中前面就好了
            if b >= 0:
                # 现在的k的位置是在最后一个比较的位置,前面k-b是等于0我愣是没想明白
                # 假设b位置走了x次,当前可以确定走完的步数是a位置是m步--因为还有个0在那里
                # 有 k = (m+n-1)-m-x = n-1-x
                # b = n-1-x
                # 所以有k==b
                # 我还做起了数学 有意思.
                nums1[k-b:k+1] = nums2[:b+1]






if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    s.merge(nums1,m,nums2,n)
    print(nums1)
