# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
=================================================================================
【最长子字符串的长度（一）】【重要】
=================================================================================
"""


def Solution(s: str):
    l = s.split("o")  # 使用 o 分割
    l.append(l[0])
    if len(l) < 3:
        return len(s)
    result = 0
    for i in range(len(l) - 3):
        temp_l = l[i] + l[i + 1] + l[i + 2]
        if len(temp_l) > result:
            result = len(temp_l)
    return result + 2  # 加上两个o


if __name__ == '__main__':
    s = "alolobo"
    r = Solution(s)
    print(r)
