# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : algorithm_mad
# Time       ：2020/12/22 17:22
# Warning    ：The Hard Way Is Easier
import random

"""
选择排序
"""


def SelectionSort(l: list):
    _len = len(l)
    for i in range(_len - 1):
        index_min = 0
        for j in range(i, _len):
            if l[j] < l[index_min]:
                index_min = j
    l[i], l[index_min] = l[index_min], l[i]
    return l


if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    array_sort = SelectionSort(array.copy())
    print('INPUT:\n%s' % ','.join([str(i) for i in array]))
    print('OUTPUT:\n%s' % ','.join([str(i) for i in array_sort]))
