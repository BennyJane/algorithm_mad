# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : algorithm_mad
# Time       ：2020/12/22 11:26
# Warning    ：The Hard Way Is Easier

import random

"""
归并排序
....
"""


def merge(l1: list, l2: list):
    """数据合并"""
    result = []
    while l1 and l2:  # 同索引对比
        if l1[0] < l2[0]:
            result.append(l1.pop(0))
        else:
            result.append(l2.pop(0))
    if l1:  # 合并剩余的数据
        result.extend(l1)
    if l2:
        result.extend(l2)
    return result


def MergeSort(l: list):
    if len(l) < 2:
        return l
    pointer = len(l) // 2
    left = l[:pointer]
    right = l[pointer:]
    return merge(MergeSort(left), MergeSort(right))


if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    array_sort = MergeSort(array.copy())
    print('INPUT:\n%s' % ','.join([str(i) for i in array]))
    print('OUTPUT:\n%s' % ','.join([str(i) for i in array_sort]))
