# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
冒泡排序 BubbleSort
相邻元素进行比较,符合条件就下移 不符合就交换
"""


def bubble_sort(lst):
    # 从第一个开始比较直到最后,每次比较可以减少一个比较的数量
    # for j in range(len(lst)-1,0,-1):
    #     # 一个一个比较
    #     for i in range(j):
    #         if lst[i] > lst[i + 1]:
    #             lst[i], lst[i + 1] = lst[i + 1], lst[i]
    # 控制次数,n个数排序n-1次
    for i in range(len(lst)-1):
        # 这个是冒泡的次数 每次冒泡好了一个之后最后那个就不要排了.
        for j in range(len(lst)-1-i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]

    print(lst)


if __name__ == '__main__':
    bubble_sort([8, 2, 6, 7, 3, 10, 9])
