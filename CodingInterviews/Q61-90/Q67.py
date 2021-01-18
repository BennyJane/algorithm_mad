# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
字符串排序
题目描述
编写一个程序，将输入字符串中的字符按如下规则排序。
规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
如，输入： Type 输出： epTy
规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
如，输入： BabA 输出： aABb
规则 3 ：非英文字母的其它字符保持原来的位置。
如，输入： By?e 输出： Be?y

注意有多组测试数据，即输入有多行，每一行单独处理（换行符隔开的表示不同行）

## 规则2使用默认排序逻辑即可，不需要特殊处理
"""


def Solution():
    while True:
        try:
            s = input()
            ori_s = s
            s = list(s)
            w_list = []
            _len = len(s)
            for i in range(_len):
                w = s[i]
                if w.isalpha():
                    w_list.append(w)
                    s[i] = "A"

            def k_f(x):
                return x.lower()

            w_list = sorted(w_list, key=k_f)
            for i in range(_len):
                w = s[i]
                if w == "A":
                    r = w_list.pop(0)
                    s[i] = r
            print("".join(s))
        except:
            break


if __name__ == '__main__':
    s = "A Famous Saying: Much Ado About Nothing (2012/8)."
    Solution()
