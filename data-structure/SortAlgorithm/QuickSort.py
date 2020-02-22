# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
快速排序,选中一个中间值,通过两个指针向中间移动的方式,确定中间值位置.
分治思想
其实就是选一个中间值,然后比中间值小的放在左边,大的放右边.
    再继续对左右的序列按照这个方法切
"""


# 碰到的问题
# 1,一开始直接递归传递参数是lst[:low]的切片,后一直无法得出结果,
#       解决:因切片操作得到的是一个新的列表对象,并不是对原对象进行操作.
#           后选择带返回值的方式重组列表.

def quick_sort(lst: list):
    if len(lst) <= 1:
        return lst
    low = 0
    high = len(lst) - 1
    # 指定一个中间值temp
    temp = lst[0]

    while low < high:
        while low < high and lst[high] >= temp:
            high -= 1
        lst[low] = lst[high]
        while low < high and lst[low] < temp:
            low += 1
        lst[high] = lst[low]

    lst[low] = temp

    left_ = quick_sort(lst[:low])
    middle = [lst[low]]
    right_ = quick_sort(lst[low + 1:])
    return left_ + middle + right_


# 2,在1的条件下新开辟了空间存储列表,按照学习视频中的内容进行改进,
# 在传递参数的过程中指定起始位置参数,start,end,
# 感觉这个方式很通用,整体也可以适配其他的语言.
def quick_sort1(alist, start, end):
    """快速排序"""

    # 递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort1(alist, start, low - 1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort1(alist, low + 1, end)


# 3,根据分治思想,结合python特性的版本---学习自菜鸟驿站.这个好像时间复杂度要高
def quick_sort2(lst: list):
    if len(lst) <= 1:
        return lst
    mid = lst[len(lst) // 2]
    left_ = [i for i in lst if i < mid]
    middle = [i for i in lst if i == mid]
    right_ = [i for i in lst if i > mid]
    return quick_sort2(left_) + middle + quick_sort2(right_)


# 4,菜鸟驿站官方写法,采用了for循环.
def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]
    # 从序列头到序列尾.
    for j in range(low, high):
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            # 如果有小于的那就将序列左边的i位置和当前的j位置交换
            arr[i], arr[j] = arr[j], arr[i]
    # 如果遍历完了,将i之后的位置和high做交换
    # 其实这个时候,遍历完了就是找不到比pivot小的,那么pivot就是最小的.
    # 将其放在i+1的位置,这样i+1的位置就是下一次的基准位置,将位置返回.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quick_sort3(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort3(arr, low, pi - 1)
        quick_sort3(arr, pi + 1, high)


if __name__ == '__main__':
    alist = [12, 3, 8, 9, 13, 4, 7, 6]
    print('原来序列:', alist)
    r = quick_sort(alist)
    print('有序序列r:', r)
    r1 = quick_sort2(alist)
    print('有序序列r1', r1)
    quick_sort3(alist, 0, len(alist) - 1)
    print('对alist直接排列', alist)
