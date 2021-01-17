# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【素数之积】
=================================================================================
"""


def Solution(n: int):
    def is_prime(a):
        # 判断是否时素数
        return a > 1 and all(a % i for i in range(2, int(a ** 0.5) + 1))

    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            s = int(n / i)
            if is_prime(s):
                return f"{i} {s}"
    return -1


if __name__ == '__main__':
    s = 15
    print(Solution(s))
