# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
计算两个正整数的最小公倍数
两个数的乘积 / 最大公约数
"""


def Solution(a: int, b: int):
    m, n = a, b
    while b != 0:  # 检测余数是否为零： 当余数为0时，上一个除数b（即现在的a）就是公约数
        b, a = a % b, b
    # 最后a就是两个数的最大公约数
    print(a, b)
    # 如果a==1，表示两个数互为质数
    return int(m * n / a)


# 判断两个数值是否互为质数
def gcd(a, b) -> bool:
    """默认a,b 都是正整数"""
    while b != 0:
        # 连续用除数/余数，直到余数为0，跳出循环
        a, b = b, a % b
    if a == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    a, b = 5, 10
    a, b = 10, 5
    print(Solution(a, b))

    a, b = 7, 5
    print(Solution(a, b))
    a, b = 328, 7751
    print(Solution(a, b))
