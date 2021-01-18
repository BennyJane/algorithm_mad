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
        # 判断是否时素数： 判断范围[2, int(n**0.5) + 1 ]
        return a > 1 and all(a % i for i in range(2, int(a ** 0.5) + 1))

    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            s = int(n / i)  # FIXME 必须使用int，避免出现小数点参数
            if is_prime(s):
                return f"{i} {s}"
    return -1


if __name__ == '__main__':
    s = 15
    print(Solution(s))
