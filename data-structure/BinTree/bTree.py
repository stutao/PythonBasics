# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
"""


class BinTNode(object):
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right


# 统计二叉树中节点的个数
def binTNodeNum(t):
    if t is None:
        return 0
    else:
        return 1 + binTNodeNum(t.left) + binTNodeNum(t.right)


# 计算二叉树节点上的值
def sum_BinTNode(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BinTNode(t.left) + sum_BinTNode(t.right)


# 遍历节点
def preorder(t):
    if t is None:
        return
        # 先根遍历
    print(t.data, end=' ')
    preorder(t.left)
    preorder(t.right)


# 中序遍历
def inorder(t):
    if t is None:
        return
    inorder(t.left)
    print(t.data, end=" ")
    inorder(t.right)


# 后根遍历
def lastorder(t):
    if t is None:
        return
    lastorder(t.left)
    lastorder(t.right)
    print(t.data, end=" ")


# 打印树节点,^表示空
def print_BinTNode(t):
    if t is None:
        print("^", end="")  # 空树输出^
        return
    print("(" + str(t.data), end='')
    print_BinTNode(t.left)
    print_BinTNode(t.right)
    print(")", end="")


if __name__ == '__main__':
    # 构造三个节点的二叉树,t表示根节点
    t = BinTNode('A',
                 BinTNode('B',
                          BinTNode('D',
                                   right=BinTNode('H')),
                          right=BinTNode('E',
                                         right=BinTNode('I'))
                          ), right=BinTNode('C',
                                            BinTNode('F',
                                                     BinTNode('J'),
                                                     BinTNode("K")),
                                            BinTNode('G')))
    # print(binTNodeNum(t))
    # print(sum_BinTNode(t))
    # print('先根')
    # preorder(t)
    # print()
    # print('中根')
    # inorder(t)
    # print()
    # print("后根")
    # lastorder(t)

    print_BinTNode(t)
