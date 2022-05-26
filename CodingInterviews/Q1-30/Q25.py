# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【找朋友】 ： 双指针
=================================================================================
"""


def Solution(ori: list):
    n = len(ori)
    res = [0] * n
    if len(ori) < 2:
        return res
    sk = [n - 1]
    for i in range(n - 2, -1, -1):
        h = ori[i]
        if h < ori[sk[-1]]:
            res[i] = sk[-1]
            sk.append(i)
            continue
        while sk and h >= ori[sk[-1]]:
            sk.pop()
        if sk:
            res[i] = sk[-1]
        sk.append(i)

    return res


def Solution2(ori: list):
    _len = len(ori)
    res = [0] * _len
    if _len < 2:
        return res
    for i in range(_len):
        cur_height = ori[i]
        for j in range(i + 1, _len):
            height = ori[j]
            if height > cur_height:
                res[i] = j
                break  # FIXME 只需要找到一个满足条件的对象
    return res


if __name__ == '__main__':
    s = [100, 95]
    print(Solution(s))
    print(Solution2(s))

    s = [100, 9, 100, 110, 52, 250]
    print(Solution(s))
    print(Solution2(s))
