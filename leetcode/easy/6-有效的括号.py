# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
"""

'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
'''


# 想法:可以用栈的方式实现是否正确匹配,
# 当出现了反向括号的时候,弹出最后一个栈元素对比是否对应
# 准备参考大佬写法.
class Solution:
    def isValid(self,s: str) -> bool:
        left_ = ['(', '[', '{', ]
        right_ = [')', ']', '}']
        l_r_map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack_ = []
        # 遍历字符串,
        for word in s:
            #
            if word in left_:
                stack_.append(word)
            elif stack_ and (word in right_):
                if l_r_map.get(stack_.pop()) != word:
                    return False
            elif (word not in left_) and (word not in right_):
                continue
            else:
                return False

        return False if stack_ else True

    def isValid2(self,s):
        dic = {
            '(': ')',
            '[': ']',
            '{': '}',
            '?': '?'
        }

        stack_ = ['?']
        for c in s:
            # 字典的key可以直接用in判断.本题也就是左括号.
            if c in dic:
                stack_.append(c)
            elif dic.get(stack_.pop()) != c:
                return False
        return len(stack_) == 1
    # 这个方法确实猛,针对当前题目是真滴强
    def isValid3(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''


if __name__ == '__main__':
    r = Solution()
    print(r.isValid2("{{{[[[((()))]]]}}}"))
