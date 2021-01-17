# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
最大连续bit数
求一个byte数字对应的二进制数字中1的最大连续数，
例如3的二进制为00000011，最大连续2个1
"""


def Solution(n: int):
    # 十进制 ==》 二进制
    # n = bin(n).replace("0b", "")
    b = bin(n)[2:]

    # 倒叙迭代：最多有 len(b)个1
    for i in range(len(b), -1, -1):
        if "1" * i in b:
            return i
    # return 0  # 需要处理没有1的情况


def Solution2(n: int):
    if n == 0:
        return 0
    s, num = bin(n), 0
    _max = max(map(len, s.replace('0b', '').split("0")))
    return _max


def Solution3(n: int):
    if n == 0:
        return 0
    import re
    s, num = bin(int(n)), 0
    t_l = re.findall(r"1{1,}", str(s))
    _max = max(t_l, key=len)  # 返回原始数据，而不是 len的执行结果
    return len(_max)


def Solution4(n: int):
    try:
        s = bin(n)[2:]
        if s == "0":
            print(0)
        s_l = s.split("0")
        _max = max(s_l, key=len)
        print(_max)
    except Exception as e:
        pass
    return len(_max)


if __name__ == '__main__':
    t = 120
    print(Solution(t), "[02]", Solution2(t), "[03]", Solution3(t))

    t = 3
    print(Solution(t), "[02]", Solution2(t), "[03]", Solution3(t))

    t = 0
    print(Solution(t), "[02]", Solution2(t), "[03]", Solution3(t))

    print(Solution4(3))
