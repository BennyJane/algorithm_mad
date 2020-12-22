# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : algorithm_mad
# Time       ：2020/12/22 11:08
# Warning    ：The Hard Way Is Easier
import random

"""
插值排序:
第一轮： 排列 [0：1]
第二轮： 排列 [0：2]
第三轮： 排列 [0：3]
....
"""


def InsertionSort(array):
    length = len(array)
    for i in range(1, length):
        pointer, cur = i - 1, array[i]
        while pointer >= 0 and array[pointer] > cur:
            array[pointer + 1] = array[pointer]
            pointer -= 1
        array[pointer + 1] = cur
    return array


def insertSort(l: list):
    _len = len(l)
    for i in range(1, _len):
        for j in range(i):
            # 找到新增数值： l[i]的位置
            if l[i] < l[j]:
                l.insert(j, l[i])
                l.pop(i + 1)  # 引入l[i]插入前面，所有原来的值的位置变为 i+1
                break
    return l


'''test'''
if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    array_sort = InsertionSort(array.copy())
    print('INPUT:\n%s' % ','.join([str(i) for i in array]))
    print('OUTPUT:\n%s' % ','.join([str(i) for i in array_sort]))
