# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
=================================================================================
【喊7的次数重排】【重点】
=================================================================================
"""


def Solution(s: str):
    l = s.split()
    _len = len(l)
    res = [0 for _ in l]
    for i in l:
        i = int(i)
        # 先计算总计数，然后获取余数; 最后确定索引位置一定要再减去1
        position = i * 7 % _len - 1
        res[position] = i
    return " ".join([str(i) for i in res])


if __name__ == '__main__':
    ori = '0 1 0'
    res = Solution(ori)
    print(res)
