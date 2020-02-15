# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
"""


# 第一种办法 采用python列表的方式,
# 如果m =1 内部while只执行一次判断,算法时间复杂度O(n)
# 如果m>n 时间复杂度,内部需要循环n,单独删除就需要O(n^2)  i+1的次数是n^2*log n
def josephus_A(n, k, m):
    '''
    n个人围成一圈,从第k个人开始报数,报道m的时候退出,然后下一个人开始继续报数,直到全部退出为止
    用列表,报道m的时候元素置为0,代表退出
    :param k:
    :param m:
    :param n:
    :return:
    '''
    people = list(range(1, n + 1))

    i = k - 1  # 表示报数起始下标
    # 开始遍历所有人
    for num in range(n):
        # 表示计数
        count = 0
        while count < m:
            # 判断是否为已经退出的人
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end=',')
                people[i] = 0
            i = (i + 1) % n
            # 这个i的意思就和下面 这几个代码差不多意思 保证i在取值范围内,0~(n-1) 当i = n-1时候 i置位0
            # if i <(n-1):
            #     i +=1
            # else:
            #     i = 0
    print()  # 打印换行
    return


# 基于顺序表的方式
# 需要遍历N个元素 里边用了pop操作,时间复杂度O(n)
def josephus_L(n, k, m):
    """
    基于顺序表的方式,出列的位置直接从表中弹出
    :param n:
    :param k:
    :param m:
    :return:
    """
    people = list(range(1, n + 1))
    # i表示数组下标
    i = k - 1
    for num in range(n, 0, -1):  # num--4
        # 这里直接采用num表示表长,用倒序来读取所有数据
        # i表示报数的位置下标 报数m个从i位置开始报所以要减去1
        i = (i + m - 1) % num
        print(people.pop(i), end='\n' if num == 1 else ',')
    return


# 基于单向循环链表的方式
from SingleLink import LCList


# 这个算法复杂度 在开始建立初始表的操作为O(n)
# 后面每次都是O(1)  m*n
class JosePhusLC(LCList):
    def turn(self, m):
        for _ in range(m):
            self._rear = self._rear.next

    def __init__(self, n, k, m):
        super(JosePhusLC, self).__init__()
        # 生成一个n个数的链表
        for i in range(n):
            self.append(i + 1)
        # 先将尾结点向报数方向移动k-1次  其实开始报数的位置是_rear.next
        self.turn(k - 1)
        # 然后开始报数
        while self._rear is not None:
            # 开始转
            self.turn(m - 1)
            # 转到位置之后实行弹出头结点
            print(self.pop(0), end="\n" if self.is_empty() else ',')


if __name__ == '__main__':
    josephus_A(10, 2, 7)
    josephus_L(10, 2, 7)
    JosePhusLC(10, 2, 7)
