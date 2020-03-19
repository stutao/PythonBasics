# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"

给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
"""


# 我感觉这个和是否相同的树的问题差不多,只不过当前是比较左子树和右子树的值是否相等
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        # 我太想当然了 直接就这么写上去了,代表我对树的理解还不够
        # return self.isSymmetric(root.left) == self.isSymmetric(root.right)
        # 观察了题解,我的思路是没错的 就是对树的理解不够
        # 引入一个帮助函数 将root看做是左右两棵树
        def help_(left_, right_):
            if left_ == None and right_ == None:
                # 如果左右两边都为空子树,返回True
                return True
            # 过了上一个条件,下面这个条件就可以直接这么写了
            if left_ == None or right_ == None:
                return False
            # 如果数值不相等
            if left_.val != right_.val:
                return False
            return help_(left_.left, right_.right) and help_(left_.right, right_.left)

        return help_(root, root)

    # 迭代写法
    def isSymmetric2(self, root: TreeNode) -> bool:
        # 空树也是对称的
        if not root:
            return True
        # 引入一个栈
        stack_ = [root.left, root.right]
        while stack_:
            right_ = stack_.pop()
            left_ = stack_.pop()
            if right_ == None and left_ == None:
                # 如果都为空,代表树遍历完了,直接往下一个遍历就好
                continue
            if right_ == None or left_ == None:
                return False
            if right_.val != left_.val:
                return False
            stack_.extend([left_.left, right_.right, left_.right, right_.left])
        return True


if __name__ == '__main__':
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(2)

    s = Solution()
    print(s.isSymmetric(t))
