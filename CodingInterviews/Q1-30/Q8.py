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
    not_selected = "aeiour"
    s_l = s.split()
    for word in s_l:
        n = len(word)
        # TODO 只要存在子字符串包含相对开音节，就成立
        if word.isalpha() and n >= 4:
            print("该字符串为纯字母类型, 且长度需要大于4")
            rev = word[::-1]
            # rev_word = "".join(list(reversed(word)))
            for i in range(0, n - 3):
                if rev[i] not in special and rev[i + 1] in special \
                        and rev[i + 2] not in not_selected and rev[i + 3] == "e":
                    num += 1
    return num


def Solution2(s: str):
    num = 0
    two = {"a", "e", "i", "o", "e"}
    three = {"a", "e", "i", "o", "e", "r"}
    four = "e"
    words = s.split()
    for w in words:
        n = len(w)
        if not w.isalpha() or n < 4:
            continue
        rev = w[::-1]
        for i in range(3, n):
            if rev[i] == four and rev[i - 1] not in three and rev[i - 2] in two and rev not in two:
                num += 1
    return num


if __name__ == '__main__':
    s1 = "ekam a ekac"
    print(Solution2(s1))

    print("123".isascii())
    print("123".isdigit())
    print("123".isalpha())
    print("123benny".isalpha())
    print("123benny".isascii())
    print("benny".isalpha())
    print("benny".isalpha())
