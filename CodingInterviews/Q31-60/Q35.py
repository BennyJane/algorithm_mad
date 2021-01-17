# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
重复字符最长串
题目描述：给定一串字符，里面有些字符有连续出现的特点，
请寻找这些连续出现字符中最长的串，
如果最长的串有多个，请输出字符ASCII码最小的那一串。

例如：输入aaabbbbbcccccccczzzzzzzz，输出cccccccc。
"""


def Solution(s: str):
    d = {}
    cur_word = {}
    for w in s:
        if w in cur_word:
            cur_word[w] += 1
        else:
            if w not in d:
                d.update(cur_word)
            else:
                if cur_word[w] > d[w]:
                    d.update(cur_word)
            # 重置cur_word
            cur_word.clear()
            cur_word[w] = 1
    l = sorted(d.items(), key=lambda x: (x[1], -1 * ord(x[0])))
    target_str = l[-1][0] * l[-1][1]
    return target_str


if __name__ == '__main__':
    t = "aaabbbbbcccccccczzzzzzzz"
    print(Solution(t))
