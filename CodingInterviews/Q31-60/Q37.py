# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
【没有回文串】

生成等长的所有字符串，排除回文，然后排序后，取字典序小于输入值 ==》 充分剪枝

下一个字典序？？
"""
import string


def Solution(s: str):
    char_arr = string.ascii_lowercase
    n = len(s)
    array = []

    def dfs(index, res):
        if index >= n:
            if res != res[::-1]:
                array.append(res)
            return
        prefix = s[:index + 1]

        for char in char_arr[:n]:
            nxt_res = res + char
            if nxt_res >= prefix:
                dfs(index + 1, nxt_res)

    dfs(0, "")
    array.sort(reverse=True)
    index = array.index(s)
    if index + 1 < len(array):
        return array[index + 1]
    return "NO"


if __name__ == '__main__':
    print(Solution("cab"))
    print(Solution("abc"))
