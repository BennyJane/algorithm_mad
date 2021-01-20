# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
先检测括号的排序是否正确，
然后统计括号嵌套的最大层数。

-- 栈：左括号入栈，右括号检测栈顶是否正确
"""


def Solution(s: str):
    d = {"]": "[", "}": "{", ")": "("}  # 括号转化，进行比对

    l = []
    _max = 0
    cur_length = 0
    for w in s:
        if w in d and len(l) > 0:
            w_left = d.get(w)
            if l[-1] != w_left:
                break
            else:
                # 需要在每次弹出栈元素时，检测栈长度
                if cur_length > _max:
                    _max = cur_length
                cur_length -= 1
                l.pop()
        elif w in d.values():
            cur_length += 1
            l.append(w)
        else:
            break

    if len(l) != 0:
        print(0)
    else:
        print(_max)


def Solution2(s: str):
    d = {"]": "[", "}": "{", ")": "("}  # 括号转化，进行比对

    l = []
    l_length = []  # 存储全过程的栈长度变化，最后取最大值
    for w in s:
        if w in d and len(l) > 0:   # 必须检测非空，排除 )(的异常 ==》 起始就是检测栈非空
            w_left = d.get(w)
            if l[-1] != w_left:
                break
            else:
                l.pop()
                l_length.append(len(l))
        elif w in d.values():
            l.append(w)
            l_length.append(len(l))
        else:
            break

    if len(l) != 0:
        print(0)
    else:
        print(max(l_length))


if __name__ == '__main__':
    # 正确情况检测
    s = '[()({})]'
    s = '([]{()})'
    s = '([]{}((())))'

    # 异常检测
    # s = '[]'
    # s = ')('
    # s = '([)]'
    # s = '[)'
    # s = '[]('
    # s ='([)]'
    Solution(s)
    Solution2(s)
