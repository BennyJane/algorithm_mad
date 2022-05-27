"""
---------------------------------------------------------------------------
题目搜集

https://blog.csdn.net/weixin_44052055/article/details/123930856
---------------------------------------------------------------------------
"""
from heapq import heappop, heappush
from typing import List

"""
---------------
栈：100
---------------
"""


# 滑动窗口最大值

# 最大嵌套括号深度

# DNA序列
# TODO 滑动窗口：易错
def solution2(s, n):
    target = ["C", "G"]
    count = 0
    for i in range(n):
        if s[i] in target:
            count += 1
    # 长度一定，使用数量来表示最大值
    ratio = count
    left = 0
    start = 0

    length = len(s)
    for right in range(n, length):
        right_char = s[right]
        left_char = s[left]

        if right_char in target:
            count += 1
        if left_char in target:
            count -= 1
        if count > ratio:
            # FIXME left对应字符已经删除，起点从left+1开始
            start = left + 1
            ratio = count

        left += 1
    return s[start: start + n]


"""
---------------
数组
---------------
"""


# 最多团队 [ 100 / 中等 ]
# 排序后，使用双指针同时从两侧遍历，根据两数之和判断移动方向


# 猴子吃桃 [ 200 / 中等 ]
# TODO 经典：二分法测试答案
def solution4(s):
    array = list(map(int, s.split(" ")))
    h = array.pop()

    n = len(array)

    upper = max(array)
    lower = 1

    ans = upper
    while lower <= upper:
        k = (lower + upper) // 2

        cost = 0
        for c in array:
            if c <= k:
                cost += 1
            else:
                cost += (c + k - 1) // k
        if cost <= h:
            ans = min(ans, k)
            upper = k - 1
        else:
            lower = k + 1
    return ans


def solution4_1(s):
    array = list(map(int, s.split(" ")))
    h = array.pop()

    n = len(array)

    upper = max(array)
    lower = 1

    while lower < upper:
        k = (lower + upper) // 2
        cost = 0
        for c in array:
            if c <= k:
                cost += 1
            else:
                cost += (c + k - 1) // k
        if cost <= h:
            upper = k
        else:
            lower = k + 1
    return upper


# 停车场车辆统计 [ 100 / 简单 ]
# 考虑通过0分割字符串


# k 对元素最小值 [ 100 / 中等 ]
# TODO 经典题目
def Solution6(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    m, n = len(nums1), len(nums2)
    ans = []
    pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
    while pq and len(ans) < k:
        _, i, j = heappop(pq)
        ans.append([nums1[i], nums2[j]])
        if j + 1 < n:
            heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
    return ans


# 最大社交距离 [ 200 / 中等 ]
# TODO 有序数组

# 玩牌高手 [ 100 / 中等 ]

# 最大差 [ 200 / 中等 ]
# TODO 复杂
def solution7(s):
    data = s.split(";")

    # from decimal import Decimal

    signal_arr = data[-1].split(",")
    # target_arr = list(map(Decimal, data[-2].split(",")))
    target_arr = list(map(float, data[-2].split(",")))
    int_arr = list(map(int, data[-3].split(",")))

    m = len(signal_arr)
    n = len(int_arr)

    double_matrix = []
    for i in range(m):
        tmp = list(map(float, data[i].split(",")))
        double_matrix.append(tmp)

    final_arr = []

    # FIXME 索引必须对应
    for i in range(m):
        res = 0.0
        for j in range(n):
            res += double_matrix[i][j] * int_arr[j]
        final_arr.append(res)

    flag = True
    max_diff = float("-inf")
    for i in range(m):
        left_res = final_arr[i]
        right_res = target_arr[i]
        cmp = signal_arr[i]

        max_diff = max(left_res - right_res, max_diff)

        is_success = True
        if cmp == ">":
            is_success = left_res > right_res
        elif cmp == "<":
            is_success = left_res < right_res
        elif cmp == ">=":
            is_success = left_res >= right_res
        elif cmp == "<=":
            is_success = left_res <= right_res
        elif cmp == "=":
            is_success = left_res == right_res
        else:
            break
        # 只要有一个不成立，就直接退出
        if not is_success:
            flag = False
            break
    # 最小值取整
    max_diff = int(max_diff)
    return f"{flag} {max_diff}"


# 数组求和 [ 100 / 简单 ]


"""
---------------
动态规划
---------------
"""


# 高效的任务规划 [ 200 / 中等 ]
# https://blog.csdn.net/weixin_44052055/article/details/123996124?spm=1001.2014.3001.5501


# 机智的外卖员 [ 100 / 中等 ]
# TODO 递归 + 剪枝 超时
# 先电梯再向下，等效于 先向下再电梯向上
def solution9(n, m):
    if n >= m:
        return n - m
    # 初始化的时候，到N层以下需要的时间，都减去相应的楼层
    upper = 10 ** 5

    ans = m - n

    def dfs(index, count):
        nonlocal ans
        if index > upper or index <= 0:
            return
        # 剪枝
        if count >= ans:
            return
        if index == m:
            ans = min(ans, count)
            return
        # 每次有三种选择
        dfs(index * 2, count + 1)
        dfs(index - 1, count + 1)
        dfs(index + 1, count + 1)

    dfs(n, 0)
    return ans


def solution9_1(n, m):
    if n >= m:
        return n - m

    dp = [0] * (m + 1)
    # 初始化的时候，到N层以下需要的时间，都减去相应的楼层
    for i in range(n + 1):
        dp[i] = n - i
    for i in range(n + 1, m + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)
        else:
            pre = int((i + 1) / 2)
            # FIXME 只需要考虑 向上加一的情况
            dp[i] = min(dp[i - 1] + 1, dp[pre] + 2)

    return dp[m]


# 叠积木 [ 100 / 中等 ]
# TODO 允许翻转长宽，每组数据预处理，长在前，宽在后
# 动态规划 或 最长递增子序列


# 叠积木
"""
题目描述
积木宽高相等，长度不等，每层只能放一个或拼接多个积木，每层长度相等，求最大层数，最少2层。
输入
给定积木的长度，以空格分隔，例如:3 6 6 3。
输出
如果可以搭建，返回最大层数，如果不可以返回-1。

样例输入
3 6 6 3
样例输出
3

样例输入
3 5
样例输出
-1
原文链接：https://blog.csdn.net/m0_56229413/article/details/117779383
"""


# 数组二叉树


# TODO 排列组合


# 分发糖果
def solution10(s):
    array = list(map(int, s.split(" ")))

    total = sum(array)
    n = len(array)
    if total % 2 != 0 or n == 1:
        return -1
    half = total // 2

    dp = [[False for _ in range(n + 1)] for _ in range(half + 1)]
    # 任意数量都可以满足 0
    for i in range(n + 1):
        dp[i][0] = True

    for t in range(1, half + 1):
        for j in range(1, n + 1):
            cnt = array[j - 1]
            if t >= cnt:
                # 使用 或 不适用当前值
                dp[t][j] = dp[t - cnt][j] | dp[t][j - 1]
            else:
                dp[t][j] = dp[t][j - 1]

    # 从动态规划 统计数据
    tmp = []
    tail, N = half, n
    while tail > 0:
        print("----")
        for i in range(N, -1, -1):
            if dp[tail][i]:
                tmp.append(i - 1)
                tail = tail - array[i - 1]
                N = i - 1
                break
    one = []
    other = []
    for i, c in enumerate(array):
        if i in tmp:
            one.append(str(c))
        else:
            other.append(str(c))

    print(half)
    print(" ".join(one))
    print(" ".join(other))
    return ""


# 新员工考试
def solution11(target):
    ans = 0

    def dfs(index, score, error):
        nonlocal ans
        if index > 25 or error >= 3:
            if target == score:
                ans += 1
            return

        if score > target:
            return

        if index <= 10:
            dfs(index + 1, score + 2, error)
            dfs(index + 1, score, error + 1)
        elif index <= 20:
            dfs(index + 1, score + 4, error)
            dfs(index + 1, score, error + 1)
        else:
            dfs(index + 1, score + 8, error)
            dfs(index + 1, score, error + 1)

    dfs(1, 0, 0)
    return ans


if __name__ == '__main__':
    # print(solution2("AACTGTGCACGACCTGA", 5))

    # print(solution4("3 11 6 7 8"))
    # print(solution4_1("3 11 6 7 8"))

    # s7 = "2.36,3,6,7.1,6;1,30,8.6,2.5,21;0.3,69,5.3,6.6,7.8;1,13,2,17,5;340,67,300.6;<=,>=,<="
    # print(solution7(s7))

    # print(solution9(5, 17))
    # print(solution9_1(100, 5000))

    # print(solution10("7 4 5 3 3"))

    print(solution11(100))
    print(solution11(94))
