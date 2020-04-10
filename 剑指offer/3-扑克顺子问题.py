# -*- coding:utf-8 -*-
# /usr/anaconda3/bin/python3
# @ DATE: 2020/4/1
# @ Author: TomTao
# @ PRODUCT_NAME: PyCharm

"""
一副牌 2-13表示2-K, 1表示A,
随机选择5个,是顺子的返回True,否则返回False
大小王可以当任何数,值为-1
"""


def isContinue(lst: list):
    # 首先要有
    if not lst:
        return False
    # 排序,在原数组上排序
    lst.sort()
    # 看有几个零
    isZero = 0
    for i in lst:
        if i == 0:
            isZero += 1
    # 将剩下的截取出来
    lst_ = lst[isZero:]
    # 引入坡度的概念.
    # 相邻两个数值的差再减一
    # 怎么理解呢 如果是顺子 相邻的数值本来就差一
    # 相邻数值的差减去1就是他们两的中间空缺,将所有数据空缺算出来
    # 参考网站的理解是说按照平时铺砖盖楼梯的时候,如果一阶多放了一块,那就需要一个王来救
    # 然后对比王的数量就知道是否可以组成顺子.
    gapNum = 0
    for j in range(len(lst_) - 1):
        if lst_[j + 1] == lst[j]:
            return False
        gapNum += lst_[j + 1] - lst[j] - 1
    return True if gapNum == isZero else False


if __name__ == '__main__':
    pass
