# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
=================================================================================
【喊7的次数重排】【重点】
N个人围成一圈，按照顺时针从1到N编号，编号为1的人开始喊数，从1到7，当喊道7的倍数或数字本身含有7的话，
不能把这个数字直接喊出来，而是要喊 过 ；

=================================================================================
"""


# FIXME 没有考虑包含数字7的情况， 只考虑7的倍数的情况
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


def Solution2(s: str):
    """使用哈希表记录7的倍数或者包含7的数字在各个位置上出现的频率"""
    l = [int(i) for i in s.split()]  # 需要先将数据转为数值类型
    _count = len(l)  # 总长度： 圆圈的长度，总人数
    d = dict([(i, 0) for i in range(len(l))])  # 用各个索引作为键
    sum_count = sum(l)  # 求总共出现了多少 ‘过’
    current_count = 0  # 记录满足7倍数以及包含7的出现次数
    for n in range(1, 201):
        if '7' in str(n) or n % 7 == 0:
            position = n % _count - 1  # 余数转索引
            d[position] += 1
            current_count += 1
        if current_count >= sum_count:
            break
    for key, value in d.items():
        l[key] = value
    return l


def Solution3(s: str):
    l = list(map(int, s.split()))
    n = len(l)  # N
    cnt = sum(l)
    d = [0 for _ in range(n)]  # 记录每个位置喊 过 的次数

    start = 1
    while cnt > 0:  # 出现的次数为限制条件
        if start % 7 == 0 or '7' in str(start):
            index = start % n - 1  # FIXME 数值转列表索引需要减去1
            d[index] += 1
            cnt -= 1
        start += 1
    return " ".join(map(str, d))


if __name__ == '__main__':
    # ori = '0 1 0'
    # ori = '0 1 1'
    # print(Solution(ori))
    #
    # ori2 = '0 1 1'
    # print(Solution2(ori2))
    # ori2 = '0 1 2'
    # print(Solution2(ori2))

    # ori2 = '0 1 2'
    ori2 = '1 0 0'
    print(Solution3(ori2))
