# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : algorithm_mad
# Time       ：2020/12/22 10:15
# Warning    ：The Hard Way Is Easier
import random

"""
桶排序：
利用序列最值，构造等长数组，再根据每个数值与最小值的差，
计算索引号，将数据填入数组，数组统计同位置的个数
"""


# TODO 只针对整数有效
def BucketSort(l: list):
    _max, _min = max(l), min(l)

    buckets = [0 for _ in range(_min, _max + 1)]
    for v in l:
        # v - _min : 计算索引的位置
        buckets[v - _min] += 1

    res = []
    for index, _count in enumerate(buckets):
        if _count != 0:
            # i + _min 计算原始数据的值
            res += [index + _min] * _count
    return res


if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    array_sort = BucketSort(array.copy())
    print('INPUT:\n%s' % ','.join([str(i) for i in array]))
    print('OUTPUT:\n%s' % ','.join([str(i) for i in array_sort]))
