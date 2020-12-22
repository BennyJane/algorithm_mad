# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : algorithm_mad
# Time       ：2020/12/22 11:06
# Warning    ：The Hard Way Is Easier
import random

"""
堆排序
"""
'''堆化'''


def heapify(array, length, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < length and array[largest] < array[left]:
        largest = left
    if right < length and array[largest] < array[right]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, length, largest)


'''堆排序'''


def HeapSort(array):
    length = len(array)
    for i in range(length, -1, -1):
        heapify(array, length, i)
    for i in range(length - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array


if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    array_sort = HeapSort(array.copy())
    print('INPUT:\n%s' % ','.join([str(i) for i in array]))
    print('OUTPUT:\n%s' % ','.join([str(i) for i in array_sort]))
