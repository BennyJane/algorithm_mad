"""
---------------------------------------------------------------------------
OD专题
---------------------------------------------------------------------------
"""


# 51、素数之积

# 52、太阳能板最大面积


# 53、停车场车辆统计

# 54、统计射击比赛成绩


# 55、完全二叉树非叶子部分后序遍历

# 56、玩牌高手


# 57、相对开音节


# 58、消消乐游戏


# 59、寻找身高相近的小朋友


# 60、寻找相同子串


# 61、一种字符串压缩表示的解压


# 62、英文输入法
# TODO 暴力，字典树
def solution62(s, t):
    return


def solution62_2(s, t):


    return


# 62、用户调度问题
# TODO 基础动态规划、dfs
def solution62():
    matrix = [
        [15, 8, 17],
        [12, 20, 9],
        [11, 7, 5]
    ]
    n = len(matrix)
    m = 3

    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0] = list(matrix[0])

    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + matrix[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + matrix[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + matrix[i][2]
    return min(dp[n - 1])


# 63、用连续自然数之和来表达整数
# TODO 模拟法
def solution63(n):
    ans = [f"{n}={n}"]

    count = 2

    # 最小值不能为0， 数量count必然小于n
    while count < n:
        diff = sum(range(count))
        retain = n - diff
        if retain % count == 0 and retain > 0:
            start = retain // count
            tmp = [start + i for i in range(count)]
            res = "+".join(map(str, tmp))
            ans.append(f"{n}={res}")
        count += 1
    return ans


# 64、找车位
def solution64(s):
    array1 = list(map(int, s.split(",")))
    ans = 0
    pre = -1

    for i, c in enumerate(array1):
        if c == 1:
            w = i - pre
            ans = max(ans, w // 2)
            pre = i
    return ans


# 65、找出符合要求的字符串子串


# 66、找朋友
# TODO 单调栈

# 67、找终点
# TODO 预处理，从后往前标记次数

# 68、整数编码
# TODO 补码 ？？ 理解题目定义
def solution68():
    return


# 69、整数对最小和
# TODO ？？
def solution69(s1, s2, k):
    array1 = list(map(int, s1.split(" ")))
    array2 = list(map(int, s2.split(" ")))

    res = []
    for c1 in array1[:k]:
        for c2 in array2[:k]:
            res.append(c1 + c2)

    res.sort()
    return sum(res[:k])


# 70、整型数组按个位值排序

# 71、执行时长
# TODO 贪心思想
def solution71(m, n, s):
    array = list(map(int, s.split(" ")))

    time = 0
    # 剩余任务量
    retain = 0
    for i in range(n):
        tasks = array[i] + retain
        time += 1
        retain = max(0, tasks - m)

    time = time + (retain + m - 1) // m
    return time


# 72、字符串变换最小字符串
# TODO 暴力遍历、

# 73、字符串分割
# TODO 复杂逻辑


# 74、字符串加密

# 75、字符串筛选排序

# 76、字符串统计


# 77、字符串序列判定
# TODO 双指针遍历


# 78、字符统计及重排
# TODO 使用 array = [] * 256 存储，ord(c) 转数值
def solution78(s):
    d = {}

    for i, c in enumerate(s):
        is_upper = str(c).isupper()
        if c not in d.keys():
            d[c] = [-1, is_upper, c]
        else:
            d[c][0] -= 1

    array = sorted(d.values())

    res = ""
    for info in array:
        count, _, char = info
        res += f"{char}:{-1 * count};"
    return res


# 79、组成最大数
def solution79(s):
    array = list(s.split(","))
    from functools import cmp_to_key

    def compare(x, y):
        # return (y + x) > (x + y)
        return int(y + x) - int(x + y)

    res = sorted(array, key=cmp_to_key(compare))

    return "".join(res)


# 80、最大N个数与最小N个数的和


# 81、最大花费金额
# TODO dfs
def solution81(s, money):
    array = list(map(int, s.split(",")))
    n = len(array)

    used = [False] * n

    ans = -1

    def dfs(index, count, total):
        nonlocal ans
        if count == 3 and total <= money:
            ans = max(ans, total)
            return
        if index >= n or total > money:
            return

        for i in range(index, n):
            if used[i]:
                continue
            cost = array[i]
            used[i] = True
            dfs(i + 1, count + 1, total + cost)
            used[i] = False

    dfs(0, 0, 0)
    return ans


# 82、最大矩阵和
# TODO 经典动态规划
def solution82():
    matrix = [
        [-3, 5, -1, 5],
        [2, 4, -2, 4],
        [-1, 3, -1, 3]
    ]

    m = len(matrix)
    n = len(matrix[0])

    ans = 0
    for top in range(m):
        row = [0] * n
        for button in range(top, m):
            for k in range(n):
                row[k] += matrix[button][k]
            # 统计从top~button行之间，高度一致的子矩阵中最大面积
            pre = 0
            for c in row:
                pre = max(c, pre + c)
                ans = max(pre, ans)
    return ans


# 83、最大括号深度
# TODO 经典题目，动态规划、栈
def solution83(s):
    sk = []
    d = {"]": "[", "}": "{", ")": "("}

    depth = 0
    for c in s:
        if c in d.values():
            sk.append(c)
        else:
            left = d[c]
            if not sk or sk[-1] != left:
                return 0
            depth = max(depth, len(sk))
            sk.pop()
    return depth


# 84、最远足迹
# str.index("(") str.index(")", start) 一组一组数据获取
# 排除以0开头的所有坐标


# 85、最长连续子序列
# TODO 前缀和
def solution85(s, target):
    array = list(map(int, s.split(",")))

    # 统计前缀和
    pre_sum = [0]
    for i, c in enumerate(array):
        pre_sum.append(c + pre_sum[-1])

    n = len(array)
    width = -1
    # !! 记录出现过的前缀和：索引
    d = {0: 0}
    for i in range(1, n + 1):
        cur = pre_sum[i]
        other = target - cur

        if other in d:
            # FIXME  计算长度，不需要+1
            w = i - d[other]
            width = max(w, width)
        d[cur] = i + 1
    return width


# 86、最长元音子串的长度

# 87、最长子字符串的长度（一）
# 分割后删除两端长度较小一个区间


if __name__ == '__main__':
    print(solution85("1,2,3,4,2", 6))
    print(solution85("1,2,3,4,2", 20))

    test_84 = "ferg(3,10)a13fdsf3(3,4)f2r3rfasf(5,10)"

    print(test_84.index("("))
    print(test_84.index(")"))

    print(solution83("[]"))
    print(solution83("([]{()})"))
    print(solution83("(]"))
    print(solution83(")("))

    print(solution82())

    print(solution81("23,26,36,27", 78))
    print(solution81("23,30,40", 26))

    print(solution79("22,221"))
    print(solution79("4589,101,41425,9999"))

    print(solution78("xyxyXX"))
    print(solution78("abababb"))

    print(solution71(3, 5, "1 2 3 4 5"))
    print(solution71(4, 5, "5 4 1 1 1"))

    print(solution69("1 1 2", "1 2 3", 2))

    print(solution64("1,0,0,0,0,1,0,0,1,0,1"))

    print(solution63(9))
    print(solution63(10))

    print(solution62())
