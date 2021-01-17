# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【最大N个数与最小N个数的和】
=================================================================================
"""


# 需要去重
def Solution(l: list, n: int):
    l = list(set(l))  # 去重
    if 2 * n > len(l):
        return -1
    l.sort()
    res = l[:n] + l[-1 * n:]
    return sum(res)


if __name__ == '__main__':
    s1 = [95, 88, 83, 64, 100]
    print(Solution(s1, 2))

