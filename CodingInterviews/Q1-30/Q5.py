# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier


"""
=================================================================================
【数组拼接】【重要】
=================================================================================
"""


def Solution(ori: list, num: int):
    res = []
    rows = len(ori)
    end_num = 0  # 记录已经去空的数组
    while True:
        for index in range(rows):
            if 0 < len(ori[index]) <= num:
                res.extend(ori[index])
                ori[index] = []
                end_num += 1
            else:
                res.extend(ori[index][:num])
                ori[index] = ori[index][num:]
        if end_num == rows:
            break
    return res


if __name__ == '__main__':
    s1 = "2,5,6,7,9,5,7"
    s2 = "1,7,4,3,4"
    ori_list = [s1.split(","), s2.split(",")]
    r = Solution(ori_list, num=3)
    print(r)
