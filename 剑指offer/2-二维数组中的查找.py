# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"

在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


# 暴力法-最简单的办法,时间效率低下.
def findNum(lst, num):
    # lst是一个二维列表,
    # [
    #     [1,2,7,8],
    #     [2,5,9,11],
    #     ...
    # ]
    # 在lst中找num

    for line in lst:
        if num in line:
            return True
    return False


# 大佬解法,采用矩阵标志数
# 按照题意,左下角数为当前列最大,当前行最小,
# 右上角数为当前行最大,当前列最小.
def findNum1(lst, num):
    # 从左下角开始
    i, j = len(lst) - 1, 0
    # 先保证不越界.
    while i >= 0 and j < len(lst[0]):
        if lst[i][j] > num:
            i -= 1
        elif lst[i][j] < num:
            j += 1
        else:
            return True
    return False

    # #还有大佬是采用异常捕获的方式,我感觉这个不错,省去了while的判断
    # try:
    #     i, j = 0, len(matrix[0]) - 1
    #     while True:
    #         if matrix[i][j] < target:
    #             i += 1
    #         elif matrix[i][j] > target:
    #             j -= 1
    #         else:
    #             return True
    # except IndexError:
    #     return False



if __name__ == '__main__':
    pass
