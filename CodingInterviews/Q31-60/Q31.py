# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a**2 + b**2 = c。

只需要验证1-c的平方根的整数部分的区间
"""


def Solution(t: int):
    if int(t ** 0.5) == t ** 0.5:
        # 0 , t** 0.5
        return True
    end = int(t ** 0.5)
    start = 1
    while start <= end:
        a = start ** 2
        b = end ** 2
        if a + b > t:
            end -= 1
        elif a + b < t:
            start += 1
        elif a + b == t:
            # start end
            return True
    return False


if __name__ == '__main__':
    t = 120
    print(Solution(t))
