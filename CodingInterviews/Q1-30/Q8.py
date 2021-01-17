# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【相对开音节】
结合正则表达式处理
=================================================================================
"""


def Solution(s: str):
    num = 0
    special = "aeiou"
    special2 = "aeiour"
    s_l = s.split()
    for word in s_l:
        if word.isalpha() and len(word) == 4:
            print("该字符串为纯字母类型")
            rev_word = "".join(list(reversed(word)))
            if rev_word[0] not in special and rev_word[1] in special and rev_word[2] not in special2 and rev_word[
                3] == "e":
                num += 1
    return num


if __name__ == '__main__':
    s1 = "ekam a ekac"
    print(Solution(s1))

    print("123".isascii())
    print("123".isdigit())
    print("123".isalpha())
    print("123benny".isalpha())
    print("123benny".isascii())
    print("benny".isalpha())
    print("benny".isalpha())
