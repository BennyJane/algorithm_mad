# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
import sys

"""
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。

例如，当输入5时，应该输出的三角形为：
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11

请注意本题含有多组样例输入。
"""


def Solution():
    n = int(sys.stdin.readline())
    left_col = []
    for i in range(1, n + 1):
        start_value = int((i - 1) * (i - 2) / 2 + i)
        left_col.append(start_value)
    print(left_col)
    for r_n in range(n, 0, -1):
        row_temp = []
        start_value = left_col[n - r_n]
        start_gap = (n - r_n) + 2

        row_temp.append(start_value)
        for c in range(1, r_n):
            next_value = row_temp[c - 1] + start_gap
            row_temp.append(next_value)
            start_gap += 1
        print(" ".join(map(str, row_temp)))


def Solution2():
    while True:
        try:
            import sys
            n = int(sys.stdin.readline())
            row_first_values = []

            for i in range(1, n + 1):
                first_value = int((i - 1) * (i - 2) / 2 + i)
                row_first_values.append(first_value)

            for r_n in range(n, 0, -1):
                row_temp = []
                row_index = n - r_n
                start_value = row_first_values[row_index]
                _gap = row_index + 2

                row_temp.append(start_value)
                for c in range(1, r_n):
                    next_value = row_temp[c - 1] + _gap
                    row_temp.append(next_value)
                    _gap += 1
                #             print(row_temp)
                print(" ".join(map(str, row_temp)))
        except:
            break


if __name__ == '__main__':
    # Solution()

    Solution2()
