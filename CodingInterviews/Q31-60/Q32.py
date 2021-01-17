# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
报数游戏
100个人围成一圈，每个人有一个编码，编号从1开始到100。
他们从1开始依次报数，报到为M的人自动退出圈圈，然后下一个人接着从1开始报数，直到剩余的人数小于M。
请问最后剩余的人在原先的编号为多少？
例如输入M=3时，输出为： “58,91” ，输入M=4时，输出为： “34,45,97”。
"""


def Solution(t: int, m=None):
    l = [i for i in range(1, t + 1)]
    cur_index = 0
    sign = 1
    while len(l) >= m:
        if sign == m:
            l.pop(cur_index)
            sign = 1
            # 删除一个元素后，索引不需要再加1
            continue
        cur_index += 1
        sign += 1
        if cur_index > len(l) - 1:
            cur_index -= len(l)
    return l


if __name__ == '__main__':
    t = 100
    m = 3
    m = 4
    print(Solution(t, m))
