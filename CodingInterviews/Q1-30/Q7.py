# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【猜数字】【重要】
https://leetcode-cn.com/problems/bulls-and-cows/


# 信息熵
https://zhuanlan.zhihu.com/p/128657483
https://www.kuniga.me/blog/2018/06/04/bulls-and-cows?redirected=1
=================================================================================
"""


def Solution(guess_list):
    _len = 4
    # 获取所有可能的4位数字
    origin = []
    for i in range(9999):
        if i <= 999:
            prefix = "0" * (_len - len(str(i)))
            origin.append(f"{prefix}{i}")
        else:
            origin.append(str(i))

    def analyse(secret, guess):
        # 计算位置与数值都正确的数值
        a = sum([secret[i] == guess[i] for i in range(_len)])
        b = 0
        l = list(secret)
        for n in guess:
            if n in l:
                l.remove(n)
                b += 1
        b -= a
        return f"{a}A{b}B"

    def filter(guess, result, data):
        # 获取满足条件的数值
        res = []
        for n in data:
            r_string = analyse(n, guess)
            if result == r_string:
                res.append(n)
        return res

    import copy
    target_list = copy.deepcopy(origin)
    for g in guess_list:
        guess, result = g.split()
        target_list = filter(guess, result, target_list)
        print(target_list)
    # print(target_list)
    if len(target_list) == 1:
        return target_list[0]
    return "NA"  # 不能确定


if __name__ == '__main__':
    s1 = [
        "4815 1A1B",
        "5716 0A1B",
        "7842 0A1B",
        "4901 0A0B",
        "8585 3A0B",
        "8555 2A1B",
    ]
    print(Solution(s1))
