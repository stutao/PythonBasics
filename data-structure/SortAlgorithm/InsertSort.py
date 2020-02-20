# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
插入排序,
我们假设左边的都是有序的,从第一个开始,然后将后面的值与前面的有序序列进行比较.
"""


def insert_sort(lst: list):
    for i in range(1, len(lst)):
        # 从i开始向前比较
        j = i
        # 当达到边界是退出循环
        while j > 0:
            # 如果比较出现更(小)大的交换位置,知道没有或者到边界
            if lst[j] > lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
                j -= 1
            else:
                break


def insert_sort1(lst: list):
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1, len(lst)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if lst[j] > lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
            else:
                break


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert_sort1(alist)
    print(alist)
