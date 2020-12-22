# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : algorithm_mad
# Time       ：2020/12/22 17:27
# Warning    ：The Hard Way Is Easier
import random

"""
希尔排序
"""


def ShellSort(l: list):
    length = len(array)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            j, cur = i, array[i]
            while (j - gap >= 0) and (cur < array[j - gap]):
                array[j] = array[j - gap]
                j = j - gap
            array[j] = cur
        gap = gap // 2
    return array


if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    array_sort = ShellSort(array.copy())
    print('INPUT:\n%s' % ','.join([str(i) for i in array]))
    print('OUTPUT:\n%s' % ','.join([str(i) for i in array_sort]))
