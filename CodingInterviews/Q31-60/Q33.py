# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
在字符串中找出连续最长的数字串

请一个在字符串中找出连续最长的数字串，并把这个串的长度返回；
如果存在长度相同的连续数字串，返回最后一个连续数字串；

注意：数字串只需要是数字组成的就可以，并不要求顺序，比如数字串“1234”的长度就小于数字串“1359055”，
如果没有数字，则返回空字符串（“”）而不是NULL！（说明：不需要考虑负数）

输入
abcd12345ed125ss123058789
输出
123058789
9

# 遍历
# 正则匹配

"""


def Solution(s: str):
    _max = ""
    _cur_length = ""
    for w in s:
        if w.isdigit():
            _cur_length += w
        else:
            if len(_cur_length) > len(_max):
                _max = _cur_length
            if _cur_length != "":
                _cur_length = ""
    # 需要考虑末尾没有字母的情况
    if len(_cur_length) > len(_max):
        _max = _cur_length
    return _max, len(_max)


def Solution2(s: str):
    import re
    res = re.findall(r"\d*", s)
    if not res:
        return ""
    res.sort(key=lambda s: len(s))
    return res[-1], len(res[-1])


if __name__ == '__main__':
    t = "abcd12345ed125ss123058789"
    print(Solution(t))

    t = "abcd12345ed125ss123058789"
    print(Solution2(t))
