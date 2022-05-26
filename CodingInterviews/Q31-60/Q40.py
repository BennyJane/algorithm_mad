# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier


"""
====================================================================================
【书籍叠放】 ==> 叠罗汉
"""
from typing import List


def solution1(books: List[List]) -> int:
    # A 升序 B降序，寻找B的最长递增子序列
    books.sort(key=lambda x: (x[0], -x[1]))

    # sk 严格递增
    sk = []
    n = len(books)
    for i in range(n):
        b = books[i][1]
        if not sk:
            sk.append(b)
            continue
        if b > sk[-1]:
            sk.append(b)
            continue
        for j in range(len(sk) - 1, -1, -1):
            pre = sk[j]
            if pre > b:
                sk[j + 1] = b
    res = len(sk)
    return res


def solution2(books: List[List]) -> int:
    # A 升序 B降序，寻找B的最长递增子序列
    books.sort(key=lambda x: (x[0], -x[1]))

    sk = []
    n = len(books)
    for i in range(n):
        b = books[i][1]
        if not sk:
            sk.append(b)
            continue
        if b > sk[-1]:
            sk.append(b)
            continue
        left, right = 0, len(sk) - 1
        while left < right:
            mid = (left + right) / 2
            if sk[mid] >= b:
                right = mid - 1
            else:
                left = mid
        sk[left] = b
    res = len(sk)
    return res


if __name__ == '__main__':
    info = [
        [20, 16],
        [15, 11],
        [10, 10],
        [9, 10],
    ]
    print(solution1(info))
    print(solution2(info))
