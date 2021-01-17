# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
重复字符排序
题目描述：找出输入字符串中的重复字符，再根据ASCII码把重复的字符从小到大排序。

例如：输入ABCABCdd，输出ABCd。

# ord() 获取ASCII码
"""


def Solution(s: str):
    d = {}
    for w in s:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    res = [item[0] for item in d.items() if item[1] > 1]
    res.sort(key=lambda x: ord(x))
    return "".join(res)


def Solution2(s: str):
    from collections import Counter
    d = dict(Counter(s))
    res = [item[0] for item in d.items() if item[1] > 1]
    res.sort(key=lambda x: ord(x))
    return "".join(res)


if __name__ == '__main__':
    t = "ABCABCdd"
    print(Solution(t))

    t = "ABCABCdd"
    print(Solution2(t))
