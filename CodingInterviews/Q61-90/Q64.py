# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
现在IPV4下用一个32位无符号整数来表示，
一般用点分方式来显示，点将IP地址分成4个部分，
每个部分为8位，表示成一个无符号整数（因此不需要用正号出现），
如10.137.17.1，是我们非常熟悉的IP地址，一个IP地址串中没有空格出现（因为要表示成一个32数字）。

现在需要你用程序来判断IP是否合法。

# 核心： 判断每个部分数值是否小于255
"""


def Solution(s: str):
    l = [int(i) for i in s.split(".")]
    for n in l:
        if n > 255 or n < 0:
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    t = "10.138.15.1"
    Solution(t)

    t = "255.0.0.255"
    Solution(t)

    t = "255.255.255.1000"
    Solution(t)
