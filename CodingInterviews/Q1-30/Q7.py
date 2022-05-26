# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【猜数字】【重要】
https://leetcode-cn.com/problems/bulls-and-cows/
解决： 如何根据 secret guess 输出提示文本

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
        if i <= 999:  # 包含 999； 需要前置位置补0
            prefix = "0" * (_len - len(str(i)))
            origin.append(f"{prefix}{i}")
        else:
            origin.append(str(i))

    # 计算任意两个数值的XAYB表达式
    def analyse(ori, other):
        # 计算位置与数值都正确的数值
        # a = sum([secret[i] == guess[i] for i in range(_len)]) # 等效写法
        a = sum([s == g for s, g in zip(ori, other)])
        b = -1 * a  # 先去除 位置与数值都正确的情况
        l = list(ori)  # 不可变对象（字符串） ==》 转为可变对象（列表）
        for n in other:
            if n in l:
                l.remove(n)
                b += 1
        return f"{a}A{b}B"

    def getHint(num, other):
        arr1 = [int(c) for c in num]
        arr2 = [int(c) for c in other]

        same = 0
        cnt1 = [0] * 10
        cnt2 = [0] * 10
        for a, b in zip(arr1, arr2):
            if a == b:
                same += 1
            else:
                cnt1[a] += 1
                cnt2[b] += 1
        diff = sum([min(a, b) for a, b in zip(cnt1, cnt2)])
        return f"{same}A{diff}B"

    def _filter(guess, result, data):
        # 获取满足条件的数值
        res = []
        for n in data:
            r_string = analyse(n, guess)
            if result == r_string:
                res.append(n)
        return res

    import copy
    target_list = copy.deepcopy(origin)  # 动态修改 target_list； 不断缩小范围
    for g in guess_list:
        guess, result = g.split()
        target_list = _filter(guess, result, target_list)
        print(target_list)
    # print(target_list)
    return "NA" if len(target_list) > 1 else target_list[0]  # 不能确定


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
