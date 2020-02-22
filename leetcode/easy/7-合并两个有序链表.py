# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"

将两个有序链表合并为一个新的有序链表并返回。
新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# Definition for singly-linked list.
# 想到用递归,但不是很熟悉,,参考大佬写法
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 首先,l1,l2都要有值
        if l1 and l2:
            # 如果l1.val>l2.val,代表l1,因为题目是从小到大,l2和l1交换
            if l1.val > l2.val: l1, l2 = l2, l1
            # 如果前面if通过,现在l1其实是原来的l2,
            # 然后继续比较l1.next和刚刚的l2,因为不知道l2是否比next的还小
            l1.next = self.mergeTwoLists(l1.next, l2)
        # 因为现在其中有一个会一直next往下走,l1,l2不知道哪个在更新.
        # python中or运算,从左往右,碰到True就返回,and是碰到false
        return l1 or l2

    # 这个比较好理解
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)

    l2 = ListNode(1)
    l2.next = ListNode(2)
    l2.next.next = ListNode(3)
    p = s.mergeTwoLists2(l1, l2)
    while True:
        if p.next:
            print(p.val, end="->")
            p = p.next
        else:
            print(p.val)
            break
