# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : algorithm_mad
# Time       ：2020/12/22 10:51
# Warning    ：The Hard Way Is Easier
import random

"""
计数排序
"""

'''计数排序(假设都是0/正整数)'''


def CountingSort(array):
    length = len(array)
    max_value = max(array)
    count = [0 for _ in range(max_value + 1)]
    output = [0 for _ in range(length)]
    for i in range(length):
        count[array[i]] += 1
    for i in range(1, len(count)):
        # 通过累加，计算数值对应在 output数组中的位置
        count[i] += count[i - 1]
    for i in range(length):
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1  # 必须减去1， 相同大小的设置索引号要递减
    return output


'''test'''
if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    array_sort = CountingSort(array.copy())
    print('INPUT:\n%s' % ','.join([str(i) for i in array]))
    print('OUTPUT:\n%s' % ','.join([str(i) for i in array_sort]))
