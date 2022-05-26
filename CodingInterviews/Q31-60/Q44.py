# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier


"""
====================================================================================
【幻方修复2】
"""


def solution():
    n = int(input())
    array = []
    for _ in range(n):
        tmp = [int(c) for c in input().split(" ")]
        array.append(tmp)
    print(array)
    total = sum(range(1, n * n + 1)) // n
    print(total)

    error = []
    for i in range(n):
        row = array[i]
        if sum(row) != total:
            error.append(i)
    # 有两行和不正确
    if error == 2:
        r1, r2 = error
        sum1 = sum(array[r1])
        sum2 = sum(array[r2])
        diff = (sum1 - sum2) // 2
        for i in range(n):
            for j in range(n):
                if array[r1][i] - array[r2][j] == diff:
                    print(f"{r1} {i} {array[r1][i]}")
                    print(f"{r2} {j} {array[r2][j]}")
                    return
    print(error)
    # 从列考虑
    error = []
    error_diff = 0
    for i in range(n):
        col_sum = 0
        for j in range(n):
            col_sum += array[j][i]
        if col_sum != total:
            error.append(i)
            error_diff += col_sum if error_diff == 0 else -1 * col_sum

    c1, c2 = error
    diff = error_diff // 2
    for i in range(n):
        for j in range(n):
            if array[i][c1] - array[j][c2] == diff:
                print(f"{i} {j} {array[i][c1]}")
                print(f"{j} {c2} {array[j][c2]}")
                return


if __name__ == '__main__':
    print(solution())

"""
3
8 1 9
3 5 7
4 6 2

"""
