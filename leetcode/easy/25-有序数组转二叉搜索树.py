# -*- coding:utf-8 -*-
# /usr/anaconda3/bin/python3
# @ DATE: 2020/3/23
# @ Author: TomTao
# @ PRODUCT_NAME: PyCharm

"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

"""


# 二叉搜索树 就是左孩子节点比根节点小,右孩子节点比根节点大

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 一通操作猛如虎 执行代码超时了 还不知道对不对.简直菜到抠脚.
    def sortedArrayToBST(self, nums: list):
        # 要求是高度平衡,我们可以从中间位置入手.
        # 我想法就是 左边子树只有左子树,因为有序..右边同理.
        # 对于左右子树高度差的绝对值为1 我没搞懂.
        n = len(nums)
        left_ = right_ = n // 2
        root = TreeNode(nums[left_])
        left_root = right_root = root
        while left_ >= 0 and right_ <= n - 1:
            if left_ > 0:
                left_ -= 1
                left_root.left = TreeNode(nums[left_])
                left_root = left_root.left
            if right_ < n - 1:
                right_ += 1
                right_root.right = TreeNode(nums[right_])
                right_root = right_root.right
        return root

    # MMY 我还是看题解吧.学习学习解题思路
    def sortedArrayToBST1(self, nums: list):
        # 借助一个帮助函数确定每个根节点和左右子树
        def helper(left, right):
            # 如果序列不满足 直接返回
            if left > right:
                return None
            # 将每次数组的中间位置当做树的根节点
            n = (left + right) // 2
            # 确定根节点
            root = TreeNode(nums[n])
            # 采用递归确定左子树往后的排序
            root.left = helper(left, n - 1)
            # 同理确定右子树往后
            root.right = helper(n + 1, right)
            # 将节点树返回
            return root

        # 初始传入序列下标
        return helper(0, len(nums) - 1)


if __name__ == '__main__':
    pass
