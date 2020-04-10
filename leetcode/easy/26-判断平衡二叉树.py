# -*- coding:utf-8 -*-
# /usr/anaconda3/bin/python3
# @ DATE: 2020/3/28
# @ Author: TomTao
# @ PRODUCT_NAME: PyCharm

"""
110. 平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 判断节点的左右子树深度是否相差在1以内
    # 和二叉树最大深度那个好像差不多
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        # 引进一个帮助函数 其实就是求最大深度的函数
        # 其实是否是真的深度是没有问题的,只要在同一层开始就好了.
        def helper(root):
            if not root:
                return 0
            depth_left = helper(root.left)
            depth_right = helper(root.right)
            return max(depth_left, depth_right) + 1

        left_ = helper(root.left)
        right_ = helper(root.right)
        return True if abs(left_ - right_) <= 1 else False


if __name__ == '__main__':
    pass
