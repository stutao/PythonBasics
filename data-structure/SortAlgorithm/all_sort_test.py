# 冒泡排序
# 最差O(n^2),最好O(n)--本来就有序
def bubble_sort(alist: list):
    # 外面这层是控制次数的,序列多长就比较多少次
    for i in range(len(alist)):
        # 第一次,整个序列长度,
        # 第二次,最后一个就不再比了
        # 以此类推
        for j in range(0, len(alist) - i - 1):
            # 前后比较,大了就交换
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


# 选择排序
# 最差O(n^2),最好O(n^2)
def selection_sort(alist: list):
    # 先找到最大(小)的数,放到序列开始,
    # 然后继续比较剩下的,放到后面
    for i in range(len(alist)):
        min_index = i
        for j in range(i, len(alist)):
            # 如果有比这个数大的,就交换位置
            if alist[min_index] > alist[j]:
                alist[min_index], alist[j] = alist[j], alist[min_index]


# 插入排序
# 最差O(n^2),最好O(n)
def insert_sort(alist: list):
    # 从第一个开始向前比
    for i in range(1, len(alist)):
        j = i
        while j > 0:
            if alist[j - 1] < alist[j]:
                alist[j - 1], alist[j] = alist[j], alist[j - 1]
                j -= 1
            else:
                break


# 希尔排序
# O(nlogN)~O(n^2)
def shell_sort(alist):
    # 插入排序的改进版本
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            # 插入排序主要内容
            while i > 0:
                if alist[i] > alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2


# 快排
# O(nlogn)
def quick_sort(alist, start, end):
    # 采用递归的方式,需要一个返回条件

    if start >= end:
        return

    # 需要一个基准值
    pivot = alist[start]

    # 需要一个左右指针
    low, high = start, end

    while low < high:
        while low < high and alist[high] >= pivot:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < pivot:
            low += 1
        alist[high] = alist[low]

    alist[low] = pivot

    quick_sort(alist, start, low - 1)
    quick_sort(alist, low + 1, end)


# 归并排序
# O(nlogn)
def merge_sort(alist):
    # 采用递归需要返回条件
    if len(alist) <= 1:
        return alist

    n = len(alist)
    mid = n // 2

    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])

    # 以上是拆分过程,下面是排序过程
    # 同样需要一个左右指针,左右两个序列从零开始.
    left = right = 0
    # 需要一个结果列表保存
    res = []
    # 循环退出条件是当其中任何一个指针指向序列最后.
    while left < len(left_li) and right < len(right_li):

        if left_li[left] < right_li[right]:
            res.append(left_li[left])
            left += 1
        else:
            res.append(right_li[right])
            right += 1

    res += left_li[left:] or right_li[right:]

    return res


if __name__ == '__main__':
    from random import randint

    alist = [randint(1, 100) for i in range(randint(1, 10))]
    print('原来序列', alist)
    # bubble_sort(alist)
    # selection_sort(alist)
    # insert_sort(alist)
    # shell_sort(alist)
    # quick_sort(alist,0,len(alist)-1)
    alist = merge_sort(alist)
    print('排序后序列', alist)
