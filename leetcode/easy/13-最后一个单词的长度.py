# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"

给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。
如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。


示例:

输入: "Hello World"
输出: 5
"""
# 才用了python内置的办法..其实改造成相对应的也是简单的,不过运行效率不够高.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 先看不存在的情况,要么s为空要么就全是空格?
        # 去空格的方式可以用strip,当然最好不用
        if not all([s,s.strip()]):
            return 0
        # 看下最后是不是空格开头？是的话就把他截断了
        while s.endswith(" "):
            s = s[:-1]
        # 从右往左找第一个空格.
        index = s.rfind(" ")
        return len(s) if index==-1 else len(s)-index-1











if __name__ == '__main__':
    s = Solution()
    # str1 = "Hello World "
    # i= str1.rfind("  ")
    # print(str1[i+1:])
    # if all([str1, str1.strip()]):
    #     print(1)
    print(s.lengthOfLastWord("b   a    "))
