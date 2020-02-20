# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
选择排序,
我们假设左边是有序的,从第一个开始慢慢向后比较.
"""


def selection_sort(lst: list):
    for i in range(len(lst)):
        # 从0位置开始慢慢向后比较
        min_index = i
        for j in range(i + 1, len(lst)):  # 有序数组之后的片段.
            # 当出现比最小位置还要小的时候,将最小下标重新赋值
            if lst[min_index] > lst[j]:
                min_index = j
        # 比较完之后,将最小的位置和当前位置交换.
        lst[min_index], lst[i] = lst[i], lst[min_index]

    print(lst)


# 升降序模式
def selection_sort1(lst: list, order=1):
    # order=1,升序,order=-1降序
    n = len(lst)
    for i in range(n):
        q = i
        j = i + 1
        while j < n:
            if (lst[q] > lst[j] and order == 1) or (lst[q] < lst[j] and order == -1):
                q = j
            j += 1
        lst[q], lst[i] = lst[i], lst[q]
    print(lst)


if __name__ == '__main__':
    selection_sort([15, 3, 8, 9, 13, 4, 7, 6])
    # selection_sort1([15, 3, 8, 9, 13, 4, 7, 6],1)
