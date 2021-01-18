# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【寻找相同子串】
规则字符串的下标从1开始
=================================================================================
"""


def Solution(t: str, p: str):
    p_length = len(p)
    for i in range(len(t)):
        t_temp = t[i: i + p_length]
        if t_temp == p:
            return i + 1
    return "No"


if __name__ == '__main__':
    s1 = "AVERDXIVYERDIAN"
    s2 = "RDXI"
    r = Solution(s1, s2)
    print(r)

