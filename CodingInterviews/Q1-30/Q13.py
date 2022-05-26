# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【靠谱的车】
-  模拟数值增长
=================================================================================
"""


def Solution(end: int):
    _sum = 0
    skip = 0
    while _sum <= end:
        _sum += 1
        _sum_str = str(_sum)
        if "4" in _sum_str:
            # len(l) - (index + 1)
            position = len(_sum_str) - _sum_str.index("4") - 1
            incr = 10 ** position  # 只需要按照个 十 百位置增加即可
            skip += incr
            _sum += incr

    real = end - skip
    return real


def Solution2(end: int):
    cur_num = 0
    skip = 0
    while cur_num < end:
        cur_num += 1
        cur_num_str = str(cur_num)
        if "4" in cur_num_str:
            position = len(cur_num_str) - (cur_num_str.index("4") + 1)
            incr = 10 ** position
            skip += incr
            cur_num += incr
    return end - skip


def Solution3(end: int):
    cur_num = 0
    real_cost = 0
    while cur_num < end:
        cur_num += 1
        real_cost += 1
        cur_num_str = str(cur_num)
        if "4" in cur_num_str:
            num = str(cur_num).replace("4", "5")
            cur_num = int(num)
    return real_cost


if __name__ == '__main__':
    s1 = 5
    print(Solution(s1))
    print(Solution3(s1))

    s1 = 25
    print(Solution(s1))
    print(Solution3(s1))
