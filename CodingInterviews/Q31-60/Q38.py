# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
数字排列
"""


def Solution(s: str):
    data = s.split(",")
    n = len(data)

    # TODO 去重操作
    result = set()
    used = [False] * n

    def dfs(index, num):
        if index >= n:
            if num != "":
                result.add(num)
            return
        # 不取任何值
        dfs(index + 1, num)
        # 每次从剩余可用字符中选择一个字符，一定会使用当前值
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            c = data[i]
            if c in ["2", "5"]:
                dfs(index + 1, num + "2")
                dfs(index + 1, num + "5")
            elif c in ["6", "9"]:
                dfs(index + 1, num + "6")
                dfs(index + 1, num + "9")
            else:
                dfs(index + 1, num + c)
            used[i] = False

    dfs(0, "")
    res = list(result)
    # 需要根据值排序
    res.sort(key=lambda x: int(x))
    return res


# FIXME 不需要保证相对顺序
def SolutionError(s: str):
    data = s.split(",")
    n = len(data)

    result = []

    def dfs(index, num):
        if index >= n:
            if num != "":
                result.append(num)
            return

        c = data[index]
        dfs(index + 1, num)
        if c in ["2", "5"]:
            dfs(index + 1, num + "2")
            dfs(index + 1, num + "5")

        elif c in ["6", "9"]:
            dfs(index + 1, num + "6")
            dfs(index + 1, num + "9")
        else:
            dfs(index + 1, num + c)

    dfs(0, "")
    result.sort()
    return result


if __name__ == '__main__':
    print(Solution("1,4,8"))
