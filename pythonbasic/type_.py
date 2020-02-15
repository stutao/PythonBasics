# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
"""

class Singeleton(type):
    def __init__(self,*args,**kwargs):
        print('init')
        self.__instance = None
        super(Singeleton, self).__init__(*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print("__call__")
        if self.__instance is None:
            self.__instance = super(Singeleton, self).__call__(*args, **kwargs)
        return self.__instance

class Foo(object,metaclass=Singeleton):
    def __init__(self):
        self._coo = 1
        self._cot = 2



if __name__ == '__main__':
    # type('类名',(父类1,父类2,可以为空),{属性名:属性值或方法})
    # def echo_int(key):
    #     return key
    # mytype = type('MyType',(),{'echo_int':echo_int})
    #
    # print(mytype.echo_int(1))

    foo1 = Foo()
    foo2 = Foo()
    print(foo1._cot)
    print(foo1 is foo2)