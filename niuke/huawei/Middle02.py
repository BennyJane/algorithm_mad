from traceback import format_exc

"""
叠积木
积木宽高相等，长度不等，每层只能放一个或拼接多个积木，
每层长度相等，求最大层数，最少2层。
输入
给定积木的长度，以空格分隔，例如:3 6 6 3。
输出
如果可以搭建，返回最大层数，如果不可以返回-1。


错误思路: 组合长度不一定为2
https://icode.best/i/69231947128806
"""


def solution1():
    while True:
        try:
            _input = input()
            # 降序排列
            blocks = sorted([int(c) for c in _input.split()], reverse=True)
            # 最大值
            max_block = blocks[0]
            total = sum(blocks)

            n = len(blocks)
            used = [False] * n

            result = [-1]
            # 最大遍历数字，取最大公因数
            # 积木长度可能默认值 > 1
            # 考虑每组长度范围[2, 总和的一半]
            for i in range(2, int(sum(blocks) / 2) + 1):
                # 判断每层长度为i时是否能搭建
                # 每层长度，必须大于等于 单个积木的最大长度
                # 总和 是 每组和的 整数倍
                if sum(blocks) % i == 0 and i >= max_block:
                    # 每一层的长度
                    target = i
                    group_count = total // target
                    if check(blocks, group_count, target, 0, used):
                        result.append(group_count)
            print(max(result))
            break
        except Exception as e:
            print(e, format_exc())
            break


def check(data: list, cnt: int, target: int, res: int, used: list):
    if cnt == 1:
        return True
    if res == target:
        return check(data, cnt - 1, target, 0, used)

    for i, c in enumerate(data):
        if i > 0 and data[i] == data[i - 1] and not data[i - 1]:
            continue
        if used[i]:
            continue
        if res + c > target:
            continue

        used[i] = True
        if check(data, cnt, target, res + c, used):
            return True
        used[i] = False
    return False


if __name__ == '__main__':
    solution1()
