# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : algorithm_mad
# Time       ：2020/12/22 10:15
# Warning    ：The Hard Way Is Easier
import random

"""
冒泡算法：
"""


def BubbleSort(l: list) -> list:
    _len = len(l)
    for i in range(_len):
        for j in range(_len - i - 1):  # 多减去1
            if l[j] > l[j + 1]:  # 大值换位
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    array_sort = BubbleSort(array.copy())
    print('INPUT:\n%s' % ','.join([str(i) for i in array]))
    print('OUTPUT:\n%s' % ','.join([str(i) for i in array_sort]))
