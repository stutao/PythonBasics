# -*- coding:utf-8 -*-
# /usr/anaconda3/bin/python3
# @ DATE: 2020/3/31
# @ Author: TomTao
# @ PRODUCT_NAME: PyCharm

#既然使用栈实现了队列 那么使用队列实现栈是否差不多?
# 栈--先进后出
# 队列--先进先出
class MyStack(object):
    def __init__(self):
        # 这里的队列简单使用列表来表示
        self.queue1 = []
        self.queue2 = []

    def push(self,elem):
        # 使用queue1来存放push进来的数据
        self.queue1.insert(0,elem)

    def pop(self):
        # 都没有数据的情况直接返回None
        if not self.queue1 and not self.queue2:
            return None
        # 如果queue2为空
        elif not self.queue2:
            while self.queue1:
                self.queue2.insert(0,self.queue1.pop())
        return self.queue2.pop()



if __name__ == '__main__':
    stack_ = MyStack()
    for i in range(3):
        stack_.push(i)
    print(stack_.pop())
    print(stack_.pop())
    print(stack_.pop())
