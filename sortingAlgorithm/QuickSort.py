# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : algorithm_mad
# Time       ：2020/12/22 11:37
# Warning    ：The Hard Way Is Easier
import random

"""
快排排序
"""


def QuickSort(l: list):
    if len(l) < 2:
        return l

    start = l[0]
    le_l = [i for i in l[1:] if i < start]
    gt_l = [i for i in l[1:] if i >= start]
    # return QuickSort(le_l + [start] + gt_l)
    return QuickSort(le_l) + [start] + QuickSort(gt_l)


def QuickSort2(array, left, right):
    if left >= right:
        return array
    pivot, i, j = array[left], left, right
    # 双指针
    while i < j:
        # 退出条件： array[j] < pivot
        while i < j and array[j] >= pivot:
            j -= 1
        array[i] = array[j]
        while i < j and array[i] <= pivot:
            i += 1
        array[j] = array[i]
    array[j] = pivot    # 最终退出while时，j的位置就pivot的位置
    QuickSort2(array, left, i - 1)
    QuickSort2(array, i + 1, right)
    return array


if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    array_sort = QuickSort2(array.copy(), 0, len(array)-1)
    # array_sort = QuickSort(array.copy())
    print('INPUT:\n%s' % ','.join([str(i) for i in array]))
    print('OUTPUT:\n%s' % ','.join([str(i) for i in array_sort]))
