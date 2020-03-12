# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 采用最简单的方法来做..时间效率不高,需要全部扫描一遍.
# 题解基本也是这写法 我也写的来了??开心啊!!!
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # next和val相同的时候 就指向next.next
        if head is None or head.next is None:
            return head
        p = head
        while p.next is not None:
            if p.next.val == p.val:
                p.next = p.next.next
            else:
                p = p.next
        return head


if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(1)
    l.next.next = ListNode(1)
    l.next.next.next = ListNode(2)
    l.next.next.next.next = ListNode(2)
    l.next.next.next.next.next = ListNode(3)
    p = l
    while p.next is not None:
        print(p.val, end="->")
        p = p.next
    print(p.val)
    s = Solution()
    j = s.deleteDuplicates(l)
    p = j
    while p.next is not None:
        print(p.val, end="->")
        p = p.next
    print(p.val)
