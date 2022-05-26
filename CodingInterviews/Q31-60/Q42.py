# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier


"""
====================================================================================
【最大值】
"""


def solution():
    s = input()
    array = s.split(" ")

    n = len(array)

    for i in range(n):
        for j in range(i + 1, n):
            a = array[i]
            b = array[j]
            if (a + b) < (b + a):
                array[i], array[j] = array[j], array[i]
    res = "".join(array)
    return res


if __name__ == '__main__':
    print(solution())
