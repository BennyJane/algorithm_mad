# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【按索引范围翻转文章片段】【重要】
=================================================================================
"""


def Solution(s: str, start: int, end: int):
    s_l = s.split()
    left = s_l[:start]
    mid = s_l[start: end + 1]
    right = s_l[end + 1:]
    # 数据倒排
    mid.reverse()
    #  reversed() 返回一个迭代器，需要转化为列表
    # mid = list(reversed(mid))
    # mid = mid[::-1]
    res = left + mid + right
    return " ".join(res)


if __name__ == '__main__':
    s1 = "I am a developer."
    print(Solution(s1, start=0, end=3))
