# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【字符串统计】
=================================================================================
"""


def Solution(ori: list, k: int):
    d = {}
    for n in ori:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    type_num = len(d.keys())  # 手机种类
    type_count = [value for value in d.values()]
    type_count.sort(reverse=True)
    for _count in type_count:
        k -= _count
        if k >= 0:
            type_num -= 1
        else:
            break
    return type_num


if __name__ == '__main__':
    s = [5, 1, 1, 2, 2, 2]
    print(Solution(s, k=2))

    s = [5, 1, 1, 2, 2, 2, 4, 4, 5, 5, 1, 2, ]
    print(Solution(s, 7))
