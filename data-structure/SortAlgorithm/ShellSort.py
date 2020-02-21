# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
希尔排序,
定义一个间隔,按照间隔进行插入排序
"""


def shell_sort(lst: list):
    n = len(lst)
    # 定义一个间隔
    gap = n // 2

    # 插入排序核心内容
    # i = 1
    # if lst[i] > lst[i-1]:
    #     lst[i],lst[i-1] = lst[i-1],lst[i]
    #     i -= 1
    # 控制循环
    while gap > 0:
        for i in range(gap, n):
            # 第一个位置从i=gap开始,然后一直往后+1,与前i-gap位置进行比较.
            for j in range(i, 0, -gap):
                if lst[j] < lst[j - gap]:
                    lst[j], lst[j - gap] = lst[j - gap], lst[j]
            # 采用while感觉更直观一点.
            # while i > 0:
            #     if lst[i] > lst[i - gap]:
            #         lst[i], lst[i - gap] = lst[i - gap], lst[i]
            #         i -= gap
            #     else:
            #         break
        gap //= 2


if __name__ == '__main__':
    alist = [15, 3, 8, 9, 13, 4, 7, 6]
    print('原来序列:', alist)
    shell_sort(alist)
    print('排序后序列:', alist)
