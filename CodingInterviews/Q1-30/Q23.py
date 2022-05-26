# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【来自异国的客人】
参考文章： https://blog.csdn.net/qq_27283619/article/details/86647109
连续商/余数，保存余数，然后余数反向排序
=================================================================================
"""


def Solution(k: int, n: int, m: int):
    nums_sign = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                 "A", "b", "C", "D", "E", "F"]
    ori_k = k
    res = []
    while True:
        k, y = divmod(k, m)
        res.append(y)
        if k == 0:
            break
    # 获取转换进制后数值字符串
    m_k = list(reversed(res))
    print(f"[{ori_k}的{m}进制表示]:", "".join([str(nums_sign[i]) for i in m_k]))

    # FIXME n长度可能大于1
    target_list = [i for i in res if i == n]
    return len(target_list)


def Solution2(num, luck, x):
    cnt = 0
    # 实现进制转换
    while num > 0:
        num, retain = divmod(num, x)
        if luck == retain:
            cnt += 1
    return cnt


if __name__ == '__main__':
    k = 10
    n, m = 2, 4
    print(Solution(k, n, m))
    print(Solution2(k, n, m))

    k = 10
    n, m = "A", 11
    print(Solution(k, n, m))
    print(Solution2(k, n, m))

    k = 28
    n, m = 0, 7
    print(Solution(k, n, m))
    print(Solution2(k, n, m))
