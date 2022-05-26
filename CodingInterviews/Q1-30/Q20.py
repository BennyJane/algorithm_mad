# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【字符串统计】
=================================================================================
"""


def Solution(s: str):
    ori, used = s.split("@")
    ori = [item.split(":") for item in ori.split(",")]
    used = dict([item.split(":") for item in used.split(",")])

    res = []
    for key, value in ori:
        used_value = used.get(key, None)
        if used_value is not None:
            value = int(value) - int(used_value)
        if value != 0:
            word_str = f"{key}:{value}"
            res.append(word_str)
    return ",".join(res)


def Solution2(s: str):
    ori, used = s.split("@")
    ori = [item.split(":") for item in ori.split(",")]
    used = dict([item.split(":") for item in used.split(",")])

    res = []
    for key, value in ori:
        used_value = used.get(key, 0)
        value = int(value) - int(used_value)
        if value != 0:
            word_str = f"{key}:{value}"
            res.append(word_str)
    return ",".join(res)


if __name__ == '__main__':
    s = "a:3,b:5,c:2@a:1,b:2"
    print(Solution(s))
