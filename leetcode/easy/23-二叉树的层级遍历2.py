# -*- coding:utf-8 -*-
# /usr/anaconda3/bin/python3
# @ DATE: 2020/3/19
# @ Author: TomTao
# @ PRODUCT_NAME: PyCharm


'''
给定一个二叉树，返回其节点值自底向上的层次遍历。
（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 看到树我的第一反应是递归,嗯,看了题解,递归的我有点懵.大部分采用双队列形式.
# 看书的时候层次遍历没有多看几遍尴尬了
# 我的想法是每一层标个数???自己把自己都搞蒙了.
# 选择直接看题解.
# 使用两个队列 一个队列装树的结构,一个装值
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list:
        if root is None:
            return []
        # 初始化两个队列
        queue_root = [root]
        queue_val = []
        #如果树结构还存在,那就继续走,
        while queue_root:
            n =len(queue_root)
            #按照题意是列表嵌套列表,定义一个临时列表存树节点的值
            temp_li = []
            # 遍历这个队列,对树进行拆分查看
            for _ in range(n):
                # 获取节点
                tree = queue_root.pop(0)
                # 将当前节点的值放入临时列表
                temp_li.append(tree.val)
                # 遍历树的下一层
                # 先把同层左子树放入,后面放右子树,先进先出,从左往右
                if tree.left:
                    queue_root.append(tree.left)
                if tree.right:
                    queue_root.append(tree.right)
            # 遍历结束之后我们要把临时数组给插入到结果数组去
            # 第一次是根节点,第二次是下一层的数据,每次数据处理完先保存在了临时列表中
            queue_val.insert(0,temp_li)
        return queue_val
if __name__ == '__main__':
    t = TreeNode(3)
    t.left=TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)

    s =Solution()
    li = s.levelOrderBottom(t)
    print(li)
