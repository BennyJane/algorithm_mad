# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier


"""
====================================================================================
遍历一个字典， 将字典中的所有值转为字符类型，
例如， {"a": 1, "b":{"c": 2, "d": 15 } },转换后变为： {"a": "1", "b": {"c": "2", "d": "15"} }
"""


def Solution(d: dict) -> dict:
    def f(obj):
        if isinstance(obj, dict):
            for k in obj.keys():
                obj[k] = f(obj.get(k))
            return obj
        else:
            return str(obj)

    return f(d)


def Solution2(d: dict) -> dict:
    if isinstance(d, dict):
        for k in d.keys():
            d[k] = Solution2(d.get(k))
        return d
    else:
        return str(d)


if __name__ == '__main__':
    d = {"a": 1, "b": {"c": 2, "d": 15}}
    print(Solution(d))
    print(Solution2(d))

    d = {"a": 1, "b": {"c": {"e": 10, "w": 20}, "d": 15}}
    print(Solution(d), "\n[way 2]:\n", Solution2(d))
