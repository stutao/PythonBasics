# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
"""


class MyDict(object):

    def __init__(self, num=100):  # 指定列表大小
        self._num = num
        self._lst = []
        for _ in range(self._num):
            self._lst.append([])

    def update(self, key, value):  # 添加 key-value
        key_index = hash(key) % self._num
        for i, (k, v) in enumerate(self._lst[key_index]):
            if key == k:
                self._lst[key_index][i] = [key, value]
                break
        else:
            self._lst[key_index].append([key, value])

    def get(self, key):  # 根据指定的 key 弹出值
        key_index = hash(key) % self._num
        for k, v in self._lst[key_index]:
            if k == key:
                return v
            else:
                raise KeyError('No such {} key'.format(key))

    def pop(self, key):  # 根据 key 弹出元素 并且删除
        key_index = hash(key) % self._num
        for i, (k, v) in enumerate(self._lst[key_index]):
            if k == key:
                result = v
                self._lst.pop(i)
                return result
            else:
                raise KeyError('No such {} key'.format(key))

    def __getitem__(self, key):  # 可以通过下标[]方括号的方式来取值
        key_index = hash(key) % self._num
        for k, v in self._lst[key_index]:
            if k == key:
                return v
            else:
                raise KeyError('No such {} key'.format(key))

    def keys(self):  # 取得所有的key
        for index in range(self._num):
            for k, v in self._lst[index]:
                yield k

    def values(self):  # 取得所有的 value
        for index in range(self._num):
            for k, v in self._lst[index]:
                yield v

    def items(self):  # 取得所有的条目
        for index in range(self._num):
            for item in self._lst[index]:
                yield item

if __name__ == '__main__':
    mydict = MyDict()
    mydict.update(key='你好',value="3")
    r= mydict['你好']
    print(r)