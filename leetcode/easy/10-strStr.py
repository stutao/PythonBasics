# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"

实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，
在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1

当needle为空,返回0
"""


# 感觉就是子串查找吧.学习一手kmp
# 先用个暴力的方法试试
# 提交错误 未考虑到haystack为空
# 提交成功  接下去参考KMP写法
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if not haystack and not needle:
#             return 0
#         n = len(needle)
#         for i in range(len(haystack)):
#             if haystack[i:i + n] == needle:
#                 return i
#         return -1

# 学习kmp
# 详细可以看这两个--具体实现采用的是<<数据结构与算法-python语言描述>>中的内容
# 1,https://www.cnblogs.com/dusf/p/kmp.html
# 2,https://blog.csdn.net/sb985/article/details/79735488
def normal_gen_next1(p):
    '''正常版本的next数组生成思路'''
    j, k, n = 0, -1, len(p)
    pnext = [-1] * n
    while j < n - 1:
        if k == -1 or p[j] == p[k]:
            j, k = j + 1, k + 1
            pnext[j] = k
        else:
            k = pnext[k]

    return pnext


def improve_gen_next(p):
    j, k, n = 0, -1, len(p)
    pnext = [-1] * n
    while j < n - 1:
        if k == -1 or p[j] == p[k]:
            k, j = k + 1, j + 1
            if p[j] == p[k]:
                pnext[j] = pnext[k]
            else:
                pnext[j] = k
        else:
            k = pnext[k]

    return pnext


def strStr(haystack: str, needle: str) -> int:
    # 两个指针位置,一个母串,一个子串
    i, j = 0, 0
    n, m = len(haystack), len(needle)
    # 计算needle的next数组
    pnext = normal_gen_next1(needle)
    while i < n and j < m:
        if j == -1 or haystack[i] == needle[j]:
            i, j = i + 1, j + 1
        else:
            j = pnext[j]
    # 当j指向与结尾,代表匹配结束
    if j == m:
        # 母串的位置是i,减去子串的长度j,这样就是子串在母串中起始的位置
        return i - j
    return -1


if __name__ == '__main__':
    # s = Solution()
    # x = strStr(haystack="hello", needle="ll")
    x = normal_gen_next1('abbcabcaabbcaa')
    # y = improve_gen_next('abbcabcaabbcaa')
    print(x)