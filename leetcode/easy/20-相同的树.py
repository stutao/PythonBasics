# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 我一直在尝试yield的方式,好像没有尝试出啥东西,知道了在递归调用yield的时候要显示
# 我的想法是每次出来一个节点的值,逐一比较,不同就返回False,在这里有一个问题,
# 比如说某个节点为空,那么这个next调用是不会显示这个空的节点的.导致运行不通过.
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        x = self.preorder(p)
        y = self.preorder(q)
        try:
            while True:
                if next(x) != next(y):
                    return False
        except StopIteration:
            return True

    def preorder(self, t):
        if t is None:
            return
        yield t.val
        for i in self.preorder(t.left):
            yield i
        for x in self.preorder(t.right):
            yield x

    # 一同操作猛如虎，仔细一看题解，自己仿佛是个傻子。
    def isSameTree1(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        # and操作符 碰到False就返回
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

    # 还有一个双向队列的东西，看的不是很懂，需要继续加油

if __name__ == '__main__':
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)

    x = TreeNode(1)
    x.left = TreeNode(2)
    x.right = TreeNode(2)

    s = Solution()
    bl = s.isSameTree1(t, x)
    print(bl)
