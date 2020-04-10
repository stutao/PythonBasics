# -*- coding:utf-8 -*-
# /usr/anaconda3/bin/python3
# @ DATE: 2020/3/31
# @ Author: TomTao
# @ PRODUCT_NAME: PyCharm

# 使用两个栈来表示队列
# 栈--先进后出
# 队列 --先进先出

# 在push的时候  直接push到stack_1中
# 在pop的时候 首先判断stack_2是否有值 有就pop 如果没有就将stack_1的值pop到stack_2中


class MyQueue(object):
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, elem):
        # 直接给stack_1加入值
        self.stack_1.append(elem)

    def pop(self):
        # 如果都没有 直接返回
        if not self.stack_1 and not self.stack_2:
            return None
        # 如果stack_2中没有值.并且stack_1中有
        elif not self.stack_2:
            while self.stack_1:
                # 将stack_1中的值出栈弹出给stack_2
                self.stack_2.append(self.stack_1.pop())
        # 然后开始stack_2出栈,同时如果stack_2中有值就直接弹出.
        return self.stack_2.pop()

    def get_q(self):
        return self.stack_1


# 一直没有调试出来 ,原来是这个'__main__'外面需要包裹的是单引号,
# 在sublime中打的使用了双引号半天没动静
if __name__ == '__main__':
    q = MyQueue()
    for i in range(3):
        q.push(i)
    print(q.get_q())
    print(q.pop())
    print(q.pop())
    print(q.pop())
