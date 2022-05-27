# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【计算面积】：
- 计算每个横坐标对应的实际y轴的值， 该值决定了到下个坐标轴之间的面积
- 利用横坐标分割多个区间，然后计算每个区间的面积
=================================================================================
"""
import math


def Solution(ori, e=None):
    axis = list(ori.keys())
    offsets = list(ori.values())
    bar_value = {}
    for index, x in enumerate(axis):
        bar_value[x] = sum(offsets[: index + 1])
    square = 0
    length = len(axis)
    for i in range(length):
        x = axis[i]
        if i == (length - 1):
            height = bar_value.get(x, 0)
            square += (e - x) * height
        else:
            next_x = axis[i + 1]
            height = bar_value.get(x, 0)
            square = square + (next_x - x) * height
    return square


def Solution2(moves, end):
    array = [0] * end
    y = 0
    for i in range(end):
        y = y + moves.get(i, 0)
        array[i] = y

    return sum([abs(c) for c in array])


def Solution3(moves, end):
    pre_x, pre_y, area = 0, 0, 0

    for x, y in moves.items():
        area += (x - pre_x) * abs(pre_y)

        pre_x = x
        pre_y += y

    # 处理末尾
    area += (end - pre_x) * abs(pre_y)
    return area


if __name__ == '__main__':
    s = {
        1: 1,
        2: 1,
        3: 1,
        4: -2,
    }
    print(Solution(s, e=10))
    print(Solution2(s, 10))

    s = {
        1: 1,
        2: 1,
        3: 1,
        4: -2,
        6: 4,
    }
    print(Solution(s, e=10))
    print(Solution2(s, 10))

    print(Solution3(s, end=10))
