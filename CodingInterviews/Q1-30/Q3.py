# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
=================================================================================
【最长子字符串的长度（一）】【重要】

o 出现偶数次
=================================================================================
"""


# TODO 理解错误：o出现次数为偶数，而不是只有2个
def Solution(s: str):
    l = s.split("o")  # 使用 o 分割
    l.append(l[0])
    if len(l) < 3:
        return len(s)
    result = 0
    for i in range(len(l) - 3):
        temp_l = l[i] + l[i + 1] + l[i + 2]
        if len(temp_l) > result:
            result = len(temp_l)
    return result + 2  # 加上两个o


def Solution2(s: str):
    _count = s.count("o")
    if _count % 2 == 0:
        return len(s)
    left = 0
    for word in s:
        if word == 'o':
            left += 1
            break
        left += 1

    right = 0
    for index in range(len(s) - 1, -1, -1):
        if s[index] == 'o':
            right += 1
            break
        right += 1
    _min = min(left, right)
    return len(s) - _min


def Solution3(s: str):
    _count = s.count("o")
    if _count % 2 == 0:
        return len(s)
    l = s.split("o")
    # print(l)
    _min = min(len(l[0]), len(l[-1]))
    return len(s) - _min - 1


if __name__ == '__main__':
    s = "alolobo"
    print(Solution(s))

    s = "ooaloloskdjlo"
    print(Solution(s), "[第三种解法]", Solution3(s))

    s = "ooaloloskdjlo"
    print(Solution2(s), "[第三种解法]", Solution3(s))

    s = "aloloskdjlo"
    print(Solution2(s), "[第三种解法]", Solution3(s))

    s = "aloloskdjloo"
    print(Solution2(s), "[第三种解法]", Solution3(s))
