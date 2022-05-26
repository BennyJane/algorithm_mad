# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
使用列表存储树结构： 索引1对应根节点，2*N索引存储左节点，2*N+1索引存储右节点，
求最小的节点值（不会存在相同值的情况）


二叉树
题目描述：
二叉树也可以用数组来存储，给定一个数组，树的根节点的值存储在下标1，
对于存储在下标N的节点，它的左子节点和右子节点分别存储在下标2N和2N+1，
并且我们用值 -1 代表一个节点为空。

给定一个数组存储的二叉树，试求从根节点到最小的叶子节点的路径，路径由节点的值组成。

输入描述
输入一行为数组的内容，数组的每个元素都是正整数，元素间用空格分隔。
注意第一个元素即为根节点的值，即数组的第N个元素对应下标N，下标0在树的表示中没有使用，所以我们省略了。
输入的树最多为7层。
输出描述
输出从根节点到最小叶子节点的路径上，各个节点的值，由空格分隔，用例保证最小叶子节点只有一个。

示例 1：
输入
3 5 7 -1 -1 2 4

输出
3 7 2

说明
最小叶子节点的路径为3 7 2

示例 2：
输入
5 9 8 -1 -1 7 -1 -1 -1 -1 -1 6

输出
5 8 7 6

说明
最小叶子节点的路径为5 8 7 6，注意数组仅存储至最后一个非空节点，故不包含节点“7”右子节点的-1

https://blog.csdn.net/weixin_44052055/article/details/124078351
"""


def Solution2(tree: str) -> str:
    # 首部插入0占位，将索引修改为从 1 起始
    array = [0]
    for c in tree.split(" "):
        array.append(int(c))
    n = len(array)

    min_val = float("inf")

    res = []

    def dfs(index, tmp):
        nonlocal min_val, res
        if index >= n:
            if tmp[-1] < min_val:
                min_val = tmp[-1]
                res = list(tmp)
            return
        cur = array[index]
        if cur == -1:
            if tmp[-1] < min_val:
                min_val = tmp[-1]
                res = list(tmp)
            return
        # TODO 回溯法
        tmp.append(cur)
        dfs(index * 2, tmp)
        dfs(index * 2 + 1, tmp)
        tmp.pop()

    dfs(1, [])
    return res


def Solution3(tree: str) -> str:
    # 首部插入0占位，将索引修改为从 1 起始
    array = [0] + [int(c) for c in tree.split(" ")]
    n, min_val = len(array), float("inf")
    res = []

    def dfs(index, tmp):
        nonlocal min_val, res
        # 同时处理，索引超出、空节点的情况
        node_val = array[index] if index < n else -1
        if node_val == -1:
            if tmp[-1] < min_val:
                min_val = tmp[-1]
                res = list(tmp)
            return
        # TODO 回溯法
        tmp.append(node_val)
        dfs(index * 2, tmp)
        dfs(index * 2 + 1, tmp)
        tmp.pop()

    dfs(1, [])
    return res


if __name__ == '__main__':
    print(Solution2("3 5 7 -1 -1 2 4"))
    print(Solution3("3 5 7 -1 -1 2 4"))
    print(Solution2("5 9 8 -1 -1 7 -1 -1 -1 -1 -1 6"))
    print(Solution3("5 9 8 -1 -1 7 -1 -1 -1 -1 -1 6"))
