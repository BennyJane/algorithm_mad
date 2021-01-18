# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【字符串加密】

- 26个英文字母： string.ascii_lowercase; string.ascii_letters; string.ascii_uppercase
- list.index()
-
=================================================================================
"""


def Solution(ori: list):
    import string
    words = string.ascii_lowercase  # 需要记住
    _len = len(words)

    def move_n(k):  # 参考斐波那契数列
        s = [1, 2, 4]
        if k < 3:
            return s
        i = 3
        while i <= k:
            temp = s[i - 1] + s[i - 2] + s[i - 3]
            s.append(temp)
            i += 1
        return s

    str_length = len(ori)
    move_nums = move_n(str_length)
    res = []
    for index, w in enumerate(ori):
        move_num = move_nums[index]
        start_index = words.index(w)
        end_index = start_index + move_num
        end_word = words[(end_index % _len)]
        res.append(end_word)
    return "".join(res)


if __name__ == '__main__':
    s = "xy"
    print(Solution(s))

    s = "abcde"
    print(Solution(s))
