# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
"""


class Preson(object):
    from collections import Iterator, Iterable
    class MyIterator(Iterator):
        def __init__(self, _lst):
            self.lst_ = _lst
            self.index = 0

        def __next__(self):
            while True:
                try:
                    elem = self.lst_[self.index]
                except IndexError:
                    raise StopIteration
                else:
                    self.index += 1
                    return elem

    def __init__(self, lst=None):
        self.lst = lst

    def __iter__(self):
        return self.MyIterator(self.lst)


if __name__ == '__main__':
    p = Preson(lst=[1, 2, 3, 4, 5])
    p =iter(p)
    print(next(p)) # 1
    print(next(p)) # 2
    print(next(p))

