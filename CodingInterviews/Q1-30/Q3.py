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
        left += 1
        if word == 'o':
            break

    right = 0
    for index in range(len(s) - 1, -1, -1):
        right += 1
        if s[index] == 'o':
            break
    _min = min(left, right)
    return len(s) - _min


def Solution3(s: str):
    cnt = s.count("o")
    # 0 或 偶数 都可以直接返回
    if cnt % 2 == 0:
        return len(s)
    l = s.split("o")
    # print(l)
    # 直接删除 最左侧的o以及左侧的字符串、或者最右侧o及右侧字符串
    # Java中 s.index("0")  s.lastIndex("0")
    _min = min(len(l[0]), len(l[-1]))
    return len(s) - _min - 1


if __name__ == '__main__':
    s = "ooaloloskdjlo"
    print(Solution(s))
    print(Solution2(s))

    s = "ooaloloskdjlo"
    print(Solution(s), "[01]", Solution3(s))

    s = "ooaloloskdjlo"
    print(Solution2(s), "[02]", Solution3(s))

    s = "aloloskdjlo"
    print(Solution2(s), "[03]", Solution3(s))

    s = "aloloskdjloo"
    print(Solution2(s), "[04]", Solution3(s))
