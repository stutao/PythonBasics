# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
"""


class MyTest(object):
    def __init__(self,_value):
        self.value = _value

    def __str__(self):
        return f'This is value {self.value}'
    #
    def __repr__(self):
        return f'this is value {self.value}'

if __name__ == '__main__':
    mytest = MyTest(1)
    print(mytest)
    print(repr(mytest))