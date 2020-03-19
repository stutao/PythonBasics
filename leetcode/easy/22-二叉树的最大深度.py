# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

"""


# 总感觉,碰到树的题目应该就是要用递归方式,或者迭代
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 我刚开始写的那个按照的思路是 如果有左右子树那就返回1,没有就返回0
        # 然后要有一个值保存,然后就和下面这样了,在后面那个+=累加1,
        # 一通操作猛如虎,一运行,莫得感情,全错.
        #  出现的问题,我自己定位是赋值为0这里,然后就是对递归的迷茫.
        # num_left = 0
        # num_right = 0
        # # 递归,需要指定递归结束条件
        # if not root:
        #     return 0
        # # # 然后写相关计算
        # if root.left or root.right:
        #     return 1
        # num_left += self.maxDepth(root.left)
        # num_right += self.maxDepth(root.right)
        # return max(num_left, num_right)

        # 看了题解之后改写
        # 结束条件
        if not root:
            return 0
        # 这两个参数我的理解是因为这个函数是有返回值的
        # 其实运行的时候一直是向下拆分.
        # 直到碰到结束条件,然后开始往回走,
        # 也就是,到了最后那个return了,max函数选择其中最大的值+1,
        # 为什么加1呢,每次回退一层加1吧?我这么想的.
        # 然后这个时候的num_left,num_right就有数了.
        num_left = self.maxDepth(root.left)
        num_right = self.maxDepth(root.right)
        return max(num_left, num_right) + 1

        # 借助栈的方式来做
        # 相比较而言 这个会更直观,更好理解一些.
    def maxDepth_by_stack(self, root: TreeNode) -> int:
        stack_ = []
        # 如果不是空树,将树存入栈
        if root is not None:
            # 第一个是层数,第二个是当前节点
            stack_.append((1, root))
        # 从等于0开始可以包括root为空的时候
        depth = 0
        while stack_:
            # 将当前的层数,节点对象都拿出来
            current_dep, root = stack_.pop()
            if root is not None:
                depth = max(depth, current_dep)
                # 然后继续往下走,将当前层数+1 和下一层节点放入栈
                stack_.append((current_dep + 1, root.left))
                stack_.append((current_dep + 1, root.right))
        return depth


if __name__ == '__main__':
    pass
