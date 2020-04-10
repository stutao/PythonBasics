# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
"""
'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"


示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
'''


# 1,第一想法,暴力法,一个一个比较.
# 2 ...

# 方式一,暴力法 执行实现40ms
# 时间复杂度估计是o(n^2)?遍历列表,然后遍历字符串?我算不怎么来..尴尬
def longestCommonPrefix(strs) -> str:
    if len(strs) <= 1:
        return strs

    else:
        count_li = []
        for i in range(1, len(strs)):
            j = 0
            while True:
                try:
                    if strs[0][j] == strs[i][j]:
                        j += 1
                    else:
                        count_li.append(j)
                        break
                except:
                    count_li.append(j)
                    break
        return strs[0][:min(count_li)]


# 参考大佬解法
'''
python两种让你拍大腿的解法，时间复杂度你想象不到，短小精悍。
 1、利用python的max()和min()，在Python里字符串是可以比较的，按照ascII值排，
 举例abb， aba，abac，最大为abb，最小为aba。
 所以只需要比较最大最小的公共前缀就是整个数组的公共前缀
 2、利用python的zip函数，把str看成list然后把输入看成二维数组，
 左对齐纵向压缩，然后把每项利用集合去重，
 之后遍历list中找到元素长度大于1之前的就是公共前缀
'''


# 方法1
# 有点疑问,不知道问题在哪.
# min max py3中比较字符串是按位进行比较的,使用ascII码.
# 如'abc'>'efg' 顺位比较,其中一个小就小.
def longestCommonPrefix2(strs):
    if not strs: return ""
    s1 = min(strs)
    s2 = max(strs)
    for i, x in enumerate(s1):
        if x != s2[i]:
            return s2[:i]
    return s1


# 方法2
def longestCommonPrefix3(strs):
    if not strs: return ""
    ss = list(map(set, zip(*strs)))
    res = ""
    for i, x in enumerate(ss):
        x = list(x)
        if len(x) > 1:
            break
        res = res + x[0]
    return res


'''
zip压缩
假如传入的是['abc','abd','abcd',]

zip之后结果是[a,a,a],[b,b,b],[c,d,c],很巧,他又会顺序进行下去.
又经过set去重,成为{a},{b},{c,d}
那么长度大于1的肯定不是相同的.
'''

if __name__ == '__main__':
    print(longestCommonPrefix(['aba', 'abb', 'abac']))
    print(longestCommonPrefix2(['aba', 'abb', 'abac']))
    print(longestCommonPrefix3(['aba', 'abb', 'abac']))
