# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

import math

"""
====================================================================================
【信道分配】
"""


def solution(r, s, d):
    # 单个信道大小 >= d 的数量
    base = 0

    # 统计剩余信道总量大小
    total = 0
    # 记录每个信道的大小、数量
    array = []
    for i, c in enumerate(s.split(" ")):
        cnt = int(c)
        vol = math.pow(2, i)
        if vol >= d:
            base += cnt
        else:
            total += vol * cnt
            array.append([vol, cnt])

    if total < d:
        return base

    # 排序
    array.sort(reverse=True)
    n = len(array)

    ans = 0

    limit = total // d

    def dfs(t, count, res):
        """
        :param t: 剩余信道总大小
        :param count: 可分配用户数量
        :param res: 当前信道总量
        :return:
        """
        nonlocal ans
        if t < d:
            ans = max(ans, count)
            return

        for k in range(n):
            volume, retain = array[k]
            if retain == 0:
                continue
            if d % volume == 0:
                vol_cnt = d // volume
                asc_count = retain // vol_cnt

                array[k] = [volume, retain - asc_count * vol_cnt]
                dfs(t - asc_count * d, count + asc_count, 0)
                array[k] = [volume, retain]
            else:
                array[k] = [volume, retain - 1]
                nxt = res + volume
                if nxt >= d:
                    dfs(t - volume, count + 1, 0)
                else:
                    dfs(t - volume, count, nxt)
                array[k] = [volume, retain]
        return

    dfs(total, 0, 0)
    return ans + base


if __name__ == "__main__":
    res = solution(5, "10 5 0 1 3 2", 30)
    print(res)
