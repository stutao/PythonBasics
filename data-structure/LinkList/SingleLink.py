# -*- coding:utf-8 -*-
__author__ = "TomTao"


# 节点类
class Node(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


# 基础链表类
class LList(object):
    """
    需要有一个指针的概念,我们这里将p当做指针
    """

    # 初始化空链表
    def __init__(self):
        self._head = None

    def is_empty(self):
        # 如果head指向None代表为空链表
        return self._head is None

    def prepend(self, elem):
        # 将新的节点指向首节点的head部分,更新原首节点的head指向新节点
        self._head = Node(elem, self._head)

    def append(self, elem):
        # 在链表的最后加入一个新节点
        if not self._head:  # 判断是否为空表
            self._head = Node(elem)
            return
        p = self._head
        while p.next:
            p = p.next
        p.next = Node(elem)
        return

    def pop(self, index=None):
        """
        pop: 默认删除尾部节点,index可以指明删除位置,当前只有0弹出首位元素
        """
        if index is None:  # index=None默认弹出最后一个节点
            if not self._head:  # 空表
                return
            p = self._head
            if p.next is None:  # 表中只有一个元素 让表头指向空
                e = p.elem
                self._head = None
                return e
            while p.next.next:  # 最后节点要找到最后一个的前面那个 也就是p.next.next不能为空
                p = p.next
            e = p.next.elem
            p.next = None
            return e
        elif index == 0:  # 弹出首节点
            if not self._head:  # 空表 异常可以后续写
                raise ValueError('The Structure Is Empty!')
            e = self._head.elem
            self._head = self._head.next
            return e
        else:
            raise ValueError('请传入正确参数')

    def printall(self):
        p = self._head
        while p:
            print(p.elem, end="")
            if p.next:
                print(" ", end="")
            p = p.next
        print()

    def elements(self):
        """
        链表元素生成器
        """
        p = self._head
        while p:
            yield p.elem
            p = p.next

    def reverse(self):
        p = None
        while self._head is not None:
            q = self._head  # 先把头结点取下来
            self._head = q.next  # head已经指向下一位
            # 将q.next指向p
            q.next = p
            # 这个p从头结点开始往后排 顺序是None--head--head.next
            p = q
        # 最后更改head的指向为当前的p 这个时候的p指向了最后节点
        self._head = p

    def sort(self):
        p = self._head
        # 先最简单的只有一个元素和没有元素
        if (self._head is None) or (self._head.next is None):
            return
        # 从第二个元素开始
        rem = p.next
        p.next = None
        while rem is not None:
            p = self._head
            q = None
            # 开始插入排序的判断
            while (p is not None) and (p.elem <= rem.elem):
                q = p
                p = p.next
            if q is None:
                # 这里是处理 如果当前元素比表头的还要大的时候
                self._head = rem  # 表头指向rem
            else:
                # 另一个情况是 走到元素大于rem,或者走到最后
                # 这个时候rem要插入到q,p之间
                q.next = rem
            # 对排序段进行连接,并推进rem到下一位

            # 前面的排序结束之后 结果 应该是 ---rem指向第二个元素  ---  [有序端|q|rem|p|无序端]
            # q=rem 后移起点到rem,  rem后推一个 q.next指向p 达成q,p拼接的目的并将rem指向有序段的最后一个节点
            q = rem
            rem = rem.next
            q.next = p


# 加入指向尾结点的派生链表类
class LListRear(LList):
    """
    这个类加入了指向尾部元素的指针,在删除尾部元素速度更快.
    """

    def __init__(self):
        super(LListRear, self).__init__()
        self._rear = None

    def prepend(self, elem):
        if self._head is None:
            # 通过头结点是否为空,判断是否为空表 如果是 ,头结点指向新的节点对象,并且repr也指向这个对象
            self._head = Node(elem, self._head)
            self._rear = self._head
        else:
            # 如果不为空 则直接改变头节点的指向
            self._head = Node(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = Node(elem, self._head)
            self._rear = self._head
        else:
            # 如果不是空表,直接改变尾结点指向,
            self._rear.next = Node(elem)
            self._rear = self._rear.next

    def pop(self, index=None):
        if index == 0:
            # 如果是弹出首元素,则直接用父类方法
            return super(LListRear, self).pop(index)
        elif index == None:
            # 如果是弹出尾部元素,
            # 首先判断是否为空
            if self._head is None:
                raise ValueError("is empty")
            # 如果只有一个元素,
            p = self._head
            if p.next is None:
                e = p.elem
                self._head = self._rear = None
                return e
            # 扫描链表
            while p.next.next is not None:
                p = p.next
            # 跳出循环的时候代表 p.next.next 是NONE了,所以p.next就是尾结点.需要弹出p.next
            e = p.next.elem
            # 弹出的值取出后,需要将p.next指向None,并将_repr指向尾结点p
            p.next = None
            self._rear = p
            return e
        else:
            return

    def reverse(self):
        self._rear = self._head
        super(LListRear, self).reverse()


class LCList(object):
    """
    只有尾结点的循环单链表的实现方式
    """

    # 初始化直接将尾结点指向为none
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        # 在首位加入元素, 先判断是否空
        p = Node(elem)
        if self._rear is None:
            # 将插入节点的next指向本身
            p.next = p
            # 将链表尾结点指向p
            self._rear = p
        else:
            # 如果不是空,插入节点p的next域指向为原来的头结点  即self._rear.next指向的位置
            # 同时更新self._rear中next域的指向为当前的新节点p
            p.next = self._rear.next
            self._rear.next = p
        # print('self._rear.next',self._rear.next.elem)

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self, index=None):
        """
        弹出
        index=0 --首位
        index=None 末尾
        """
        # 先判断是否为空
        if self._rear is None:
            raise ValueError("is empty")
        # 需要判断是否只有一个元素
        elif self._rear.next is self._rear:
            e = self._rear.elem
            self._rear = None
            return e
        elif index == 0:
            # 弹出首位 当前last指向的是头结点, 首节点弹出需要改成指向last.next
            p = self._rear.next  # 这个是头结点
            e = p.elem  # 这个是弹出的元素
            self._rear.next = p.next  # 改变尾结点的next域指向
            return e
        elif index is None:
            # 弹出最后一位.
            # 找到头部结点
            p = self._rear.next
            # 遍历 如果下一个节点是尾结点
            while p.next is not self._rear:
                p = p.next
            # 退出循环的时候代表p指向是尾结点
            e = p.next.elem
            # 调整当前节点的next域指向原先的头结点位置 即self._rear.next
            p.next = self._rear.next
            # 调整尾结点的应用为当前的p位置
            self._rear = p
            return e

    def printall(self):
        if self._rear is None:
            return
        p = self._rear.next
        while True:
            print(p.elem, end=" ")
            if p is self._rear:
                break
            p = p.next
        print()

    # def reverse(self):
    #     p = None
    #     while self._head is not None:
    #         q = self._head  # 先把头结点取下来
    #         self._head = q.next  # head已经指向下一位
    #         # 将q.next指向p
    #         q.next = p
    #         # 这个p从头结点开始往后排 顺序是None--head--head.next
    #         p = q
    #     # 最后更改head的指向为当前的p 这个时候的p指向了最后节点
    #     self._head = p

    def reverse(self):
        if self._rear is None:
            pass
        else:
            p = self._rear
            head = self._rear.next  # 头结点
            # 尾结点
            # 当节点与其的next域指向不一致,代表还没到尾结点.
            while self._rear is not self._rear.next:
                # 首先要把头结点摘下来 这两步就是摘下了.
                h = self._rear.next
                self._rear.next = h.next
                # 将摘下来的头结点的next域指向已保存的头结点
                h.next = p
                p = h
            self._rear = head


# 带有头尾节点的循环单链表
class SClist(object):
    def __init__(self):
        self._head = None

    def prepend(self, elem):
        p = Node(elem)
        if self._head is None:
            p.next = p
            self._head = p
        p.next = self._head
        current = self._head
        # 移动到链表底部 修改最后的next指向
        while current.next is not self._head:
            current = current.next
        current.next = p
        self._head = p

    def printall(self):
        if self._head is None:
            return
        p = self._head
        while True:
            print(p.elem, end=" ")
            if p.next is self._head:
                break
            p = p.next
        print()

    def reverse1(self):
        # if list is empty
        if self._head is None:
            return

        # reverse procedure same as
        # reversing a singly linked list
        prev = None
        current = self._head

        next_ = current.next
        current.next = prev
        prev = current
        current = next_
        while (current != self._head):
            next_ = current.next
            current.next = prev
            prev = current
            current = next_

        # adjutsing the links so as to make the
        # last node po to the first node
        self._head.next = prev
        self._head = prev


if __name__ == '__main__':
# import random
#
# # 不重复的数
# random_list = random.sample(range(1, 2000000), 200)
# print("总长:%s,去重后%s" % (len(random_list), len(set(random_list))))
# # 可以重复的
# list1 = [random.choice(range(1,3000)) for _ in range(200)]
# print("总长:%s,去重后%s" % (len(list1), len(set(list1))))

# 单链表
# Llist = LListRepr()
# for i in range(6):
#     Llist.prepend(i)
# # for j in range(10, 18):
# #     Llist.append(j)
# Llist.printall()
# # print(Llist.pop())
# print(Llist.pop(0))
# print("-" * 30)
# for i in Llist.elements():
#     print(i, end=" ")
# LClist = LList()
# for i in range(6):
#     LClist.prepend(i)
#
# LClist.printall()
# # LClist.reverse1()
# LClist.sort()
# LClist.printall()
    print(1)