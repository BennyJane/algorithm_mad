# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
=================================================================================
字符统计及重排【重要】
给出一个仅包含字母的字符串，不包含空格，统计字符串中各个字母（区分大小写）出现的次数，
并按照字母出现次数从大到小的顺序输出各个字母及其出现次数。如果次数相同，按照自然顺序进行排序，
且小写字母在大写字母之前。
=================================================================================
"""


def Solution(s: str):
    d = {}
    for w in s:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1

    def key_f(value):
        word = value[0]
        c = value[1]
        sort_keys = (c, word.islower())
        # sort_keys = (c, word.islower(), word) # 加入按照字母排序
        # print(sort_keys)
        return sort_keys

    # 修改为降序
    result = sorted(d.items(), key=key_f, reverse=True)
    return ";".join([":".join([str(i) for i in item]) for item in result])


if __name__ == '__main__':
    s = "xyxyXX"
    r = Solution(s)
    print(r)

    s2 = "abababb"
    print(Solution(s2))
    s3 = "yxyxXX"
    print(Solution(s3))
