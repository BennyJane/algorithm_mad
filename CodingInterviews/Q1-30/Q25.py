# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【找朋友】 ： 双指针
=================================================================================
"""


def Solution(ori: list):
    length = len(ori)
    if len(ori) < 2:
        return [0]
    res = [0 for _ in ori]
    for i in range(0, length - 1):
        left = ori[i]
        j = i + 1   # 第二个指针
        while j < length:
            right = ori[j]
            if right > left:
                res[i] = j
                break   # 及时终止
            else:
                j += 1
    return res


if __name__ == '__main__':
    s = [100, 95]
    print(Solution(s))

    s = [100, 9, 100, 110, 52, 250]
    print(Solution(s))

