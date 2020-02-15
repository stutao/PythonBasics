# -*- coding:utf-8 -*-
__author__ = "TomTao"

from SingleLink import Node, LListRear


class DLNode(Node):
    def __init__(self, elem, prev=None, next_=None):
        super(DLNode, self).__init__(elem, next_)
        self.prev = prev


# 现在的一个节点有对应的 头结点指针_head,尾结点指针_rear,上一个节点指针prev,下一个节点指针next
class DLlist(LListRear):
    def __init__(self):
        super(DLlist, self).__init__()

    def prepend(self, elem):
        '''
        在首节点插入元素
        :param elem:
        :return:
        '''
        # 创建节点,并且next指定为self._head
        p = DLNode(elem, None, self._head)
        #    判断是否为空 为空价将rear指向当前节点
        # 为什么prepend判断空表先更新_rear的指向?
        # # 个人观点,以为prepend最后一步肯定是会对头结点引用进行更改的,所以在空表的时候先改变头结点? append同理
        if self._head is None:
            self._rear = p
        else:
            # 不为空  | prev | elem |  next  |
            # 指定第二位节点的prev引用
            p.next.prev = p
        # 随后 更改_head的引用在p
        self._head = p

    def append(self, elem):
        '''
        在某位插入节点
        :param elem:
        :return:
        '''
        p = DLNode(elem, self._rear, None)
        # 判断是否空表,空表设置头结点引用
        if self._head is None:
            self._head = p
        else:
            # 不为空 设置next的引用
            p.prev.next = p
        self._rear = p

    def pop(self, index=None):
        """
        弹出元素
        :param index:
        :return:
        """
        # 判断是否空表
        # print(index)
        if (index != 0) & (index is not None):
            raise ValueError("参数错误")
        elif self._head is None:
            raise ValueError("IS Empty")
        # 判断是否只有一个元素
        elif self._head.next is None:
            self._head = self._rear = None
        elif index == 0:
            # 弹出首位元素
            p = self._head
            # _head指向下一个
            e = p.elem
            self._head = p.next
            p.next.prev = None
            return e
        else:
            # index =None 弹出末尾元素
            p = self._rear
            e = p.elem
            # _rear 指向前一个
            self._rear = p.prev
            # 改变next引用
            p.prev.next = None
            return e


# 双向循环列表
class DLCycleLink(DLlist):
    # 其他的完全可以参考这个头节点插入来写.
    def prepend(self, elem):
        # 先判断是否为空
        p = DLNode(elem, None, self._head)
        if self._head is None:
            self._head = self._rear = p
            p.next = p.prev = p
        else:
            # 首先将头结点指向p 尾结点的next引用指向p
            self._head = p
            self._rear.next = p
            # 改变原一号位prev的引用
            p.next.prev = p
            # 改变当前位置的prev引用到末尾
            p.prev = self._rear

    def append(self, elem):
        pass

    def pop(self, index=None):
        pass

    def printall(self):
        # 首先判断是否为空
        if self._head is None:
            return
        # 在头节点标记指针P
        p = self._head
        # 如果指针的next域是_head头结点,那就退出循环
        while True:
            print(p.elem, end=" ")
            if p.next is self._head:
                break
            p = p.next


if __name__ == '__main__':
    dllist = DLCycleLink()

    for i in range(7):
        dllist.prepend(i)
    dllist.printall()
