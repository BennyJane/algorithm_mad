# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【用户调度问题】
参考文章：https://www.cnblogs.com/ma6174/archive/2012/04/24/2468123.html

先将每个作业处理时间降序排列， 依次选择时间往机器上安排，
    - 每次安排在当前工作量总时间最小的机器上
=================================================================================
"""


def Solution(ori: list, k: int):

    return


if __name__ == '__main__':
    s = [5, 1, 1, 2, 2, 2]
    print(Solution(s, k=2))

    s = [5, 1, 1, 2, 2, 2, 4, 4, 5, 5, 1, 2, ]
    print(Solution(s, 7))
