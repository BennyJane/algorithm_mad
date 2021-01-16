# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【靠谱的车】
=================================================================================
"""


def Solution(end: int):
    _sum = 0
    skip = 0
    while _sum <= end:
        _sum += 1
        _sum_str = str(_sum)
        if "4" in _sum_str:
            position = len(_sum_str) - _sum_str.index("4") - 1
            incr = 10 ** position   # 只需要按照个 十 百位置增加即可
            skip += incr
            _sum += incr

    real = end - skip
    return real


if __name__ == '__main__':
    s1 = 5
    print(Solution(s1))

    s1 = 25
    print(Solution(s1))