# -*- coding:utf-8 -*-
"""
__author__ = "TomTao"
"""
'''
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，
即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。
但也存在特例，例如 4 不写做 IIII，而是 IV。
数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 :
输入: "III"
输出: 3

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
'''


# 看到题目想到的是用hash解决,最后还是参考了一下题解
# 解法参考了题解.
def roma_to_int(s: str) -> int:
    # 将罗马数字对应int存入一个hash表
    hash_roma = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    res = 0
    # 扫描这个字符串,从开始到倒数第二个
    # 如果当前字符值大于后面的字符值res+当前字符对应的值,
    # 如果当前字符值小于后面的字符值,res-当前字符对应的值
    for i in range(len(s) - 1):
        if hash_roma[s[i]] > hash_roma[s[i + 1]]:
            res += hash_roma[s[i]]
        else:
            res -= hash_roma[s[i]]
    return res + hash_roma[s[-1]]


# 方法二是将所有可能的组合都列入hash表 然后用正则匹配的方式?

def roma_to_int_re(s):
    import re
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }
    spacial = [d[c] for c in re.findall('IV|IX|XL|XC|CD|CM', s)]
    rest = [d[c] for c in re.sub('IV|IX|XL|XC|CD|CM', '', s)]
    return sum(spacial) + sum(rest)

# 应该还有一种方法 将所有特殊情况放入hash表,然后字符串截取出来去比较,
# 两个的不匹配就一个一个去取数,然后从这个位置开始从新来过.
if __name__ == '__main__':
    r = roma_to_int_re('MCMXCIV')
    print(r)

