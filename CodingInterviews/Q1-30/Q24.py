# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【回文素数】
=================================================================================
"""


def Solution(end: int):
    res = []

    def is_prime(n):
        # 判断是否为素数
        return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))

    def reverse(x):  # 数值反转顺序
        return int(str(x)[::-1])

    def reverse2(x):  # 数值反转顺序
        rev_num = 0
        while x:
            rev_num = rev_num * 10 + x % 10
            x /= 10
        return rev_num

    for i in range(1, end + 1):
        if is_prime(i) and i == reverse(i):
            res.append(i)
    return len(res), res


if __name__ == '__main__':
    end = 50
    print(Solution(end))
