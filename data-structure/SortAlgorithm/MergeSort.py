 # -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
归并排序,

"""


def merger_sort(lst: list):
    n = len(lst)
    if n <= 1:
        return lst
    # 切分,返回有序列表
    num = n // 2
    left_ = merger_sort(lst[:num])
    right_ = merger_sort(lst[num:])
    # 初始化左右指针位置从0开始
    left_p = right_p = 0
    # 满足上面的返回一个有序列表
    res = []
    # 需要对左右指针所指的数进行大小比较,
    # 退出循环条件是当其中任何一个指针指向当前序列最后一个元素
    while left_p < len(left_) and right_p < len(right_):
        # 开始排序
        if left_[left_p] < right_[right_p]:
            res.append(left_[left_p])
            left_p += 1
        else:
            res.append(right_[right_p])
            right_p += 1
    # 当退出循环的时候,应该还有一个序列是非空的,or碰到true就返回那个
    res += left_[left_p:] or right_[right_p:]
    # 将序列结果返回
    return res


if __name__ == '__main__':
    alist = [15, 3, 8, 9, 13, 4, 7, 6]
    print('原来序列:', alist)
    r = merger_sort(alist)
    print('排序后序列r:', r)
