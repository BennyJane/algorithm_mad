import collections
from cmath import inf
# from linecache import cache
from functools import lru_cache
from typing import List
from collections import Counter
from collections import defaultdict


class Solution1:
    # 691. 贴纸拼词
    """

    满足条件：
    贴纸包含字符种类 >= target中的字符种类
    贴纸包含字符种类的数量 >= target中的字符种类的数量

    贴纸中不包含target中字符的直接排除
    """

    # 使用Counter方法
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(stickers)
        # 统计每个单词的字符数量
        d = [Counter(s) for s in stickers]

        # @cache
        @lru_cache(None)
        def dfs(t):
            if not t:
                return 0

            ans = inf  # 统计消耗贴纸数量
            cnt = Counter(t)
            for i in range(n):
                cs = d[i]
                # 判断模式串 与 目标串 是否有交集
                # 贴纸与target没有交集，直接跳过
                # & 同key非0，才会保留
                if cs & cnt:
                    # 假设使用该贴纸，计算target中剩余字符，并拼成单词，用于进一步处理
                    tmp = "".join(k * v for k, v in (cnt - cs).items())
                    ans = min(ans, dfs(tmp) + 1)
            return ans

        res = dfs(target)
        return res if res != inf else -1

    # 完全背包问题：物品数量不受限制
    def minStickers2(self, stickers: List[str], target: str) -> int:
        n = len(stickers)
        m = len(target)

        # 计算target所有子序列的数量
        total_status = 1 << m
        # dp[i]: 表示target的子序列，需要贴纸的最小数量
        # 子序列状态使用一个数值i表示，转化为二进制后，位置上为1表示包含target同位置上的字符
        dp = [-1] * total_status
        # dp = [float("inf")] * total_status
        dp[0] = 0  # 初始状态：不包含任意target中的字符
        for sticker in stickers:
            for status in range(total_status):
                # FIXME: 必须跳过-1，计算下一个状态的前提条件是，status已经被处理过
                if dp[status] == -1:
                    continue
                # cur_status: 转为二进制后表示选取target那些位置上的字符
                cur_status = status
                # 假设选择当前贴纸，将会修改当前状态：即 target中一些字符会被选择
                for c in sticker:
                    # 寻找到贴纸 存在与target中的字符，且没有被cur_state选中的字符
                    for j in range(m):
                        # 一个字符找到一个满足条件的即可
                        if c == target[j] and cur_status & (1 << j) == 0:
                            cur_status |= 1 << j
                            break
                # 选择当前贴纸后的状态，两种情况：
                # 没有被处理过
                # 已经出现过：表示有其他可能的组合，需要取最小
                if dp[cur_status] == -1:
                    dp[cur_status] = dp[status] + 1
                else:
                    dp[cur_status] = min(dp[cur_status], dp[status] + 1)
        # total_status - 1： 表示target所有字符全部选中的情况
        return dp[total_status - 1]


# 383. 赎金信
class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)


# 1220. 统计元音字母序列的数目
class Solution3:
    def countVowelPermutation2(self, n: int) -> int:
        # MOD = int(1e9) + 7
        MOD = 1000000007
        # 当长度为1时，结尾为不同元音字符时，每种情况的数量
        a, e, i, o, u = 1, 1, 1, 1, 1
        for k in range(2, n + 1):
            #
            nxt_a = (e + i + u) % MOD
            nxt_e = (a + i) % MOD
            nxt_i = (e + o) % MOD
            nxt_o = i % MOD
            nxt_u = (o + i) % MOD
            a, e, i, o, u = nxt_a, nxt_e, nxt_i, nxt_o, nxt_u
        return (a + e + i + o + u) % MOD

    def countVowelPermutation1(self, n: int) -> int:
        dp = (1, 1, 1, 1, 1)
        for _ in range(n - 1):
            dp = (
                (dp[1] + dp[2] + dp[4]) % 1000000007, (dp[0] + dp[2]) % 1000000007, (dp[1] + dp[3]) % 1000000007, dp[2],
                (dp[2] + dp[3]) % 1000000007)
        return sum(dp) % 1000000007

    def countVowelPermutation2(self, n: int) -> int:
        ans = 0

        def dfs(index, pre=None):
            nonlocal ans
            if index > n:
                ans += 1
            if pre is None:
                dfs(index + 1, 0)
                dfs(index + 1, 1)
                dfs(index + 1, 2)
                dfs(index + 1, 3)
                dfs(index + 1, 4)
            elif pre == 0:
                dfs(index + 1, 1)
            elif pre == 1:
                dfs(index + 1, 0)
                dfs(index + 1, 2)
            elif pre == 2:
                dfs(index + 1, 0)
                dfs(index + 1, 1)
                dfs(index + 1, 3)
                dfs(index + 1, 4)
            elif pre == 3:
                dfs(index + 1, 2)
                dfs(index + 1, 4)
            else:
                dfs(index + 1, 0)

        return ans


# 935.骑士拨号器
class Solution4:
    def knightDialer(self, n: int) -> int:
        d = {
            0: [4, 6],
            1: [8, 6],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [1, 7, 0],
            7: [2, 9],
            8: [1, 3],
            9: [4, 2]
        }
        mod = 10 ** 9 + 7
        dp = [1 for _ in range(10)]
        for i in range(2, n):
            nxt = [1 for _ in range(10)]
            for j in range(10):
                nxt[j] = sum(dp[pre] for pre in d[j]) % mod
            dp = nxt
        return sum(dp) % mod


# 1345.跳跃游戏IV
class Solution:
    # 广度优先搜索
    def minJumps(self, arr: List[int]) -> int:
        # 记录同值索引位置
        idxSameValue = defaultdict(list)
        for i, c in enumerate(arr):
            idxSameValue[c].append(i)

        # 记录已经访问的索引位置
        visitedIndex = set()
        q = collections.deque()
        # 出发点
        q.append([0, 0])
        visitedIndex.add(0)
        while q:
            idx, step = q.popleft()
            if idx == len(arr) - 1:
                # 访问到最后一个索引位置
                return step
            val = arr[idx]
            # step必然是最短路径
            step += 1
            # TODO 可以优先确认的是：同值的最短路径
            for i in idxSameValue[val]:
                if i not in visitedIndex:
                    visitedIndex.add(i)
                    q.append([i, step])
            # 同值数据，不需要再次处理
            del idxSameValue[val]
            # 处理当前索引位置左右两侧的情况
            if idx + 1 < len(arr) and (idx + 1) not in visitedIndex:
                visitedIndex.add(idx + 1)
                q.append([idx + 1, step])
            if idx - 1 >= 0 and (idx - 1) not in visitedIndex:
                visitedIndex.add(idx - 1)
                q.append([idx - 1, step])

    # 动态规划错误
    # ERROR：每个点的最短路径来源，还可能来自于后面的一个点，进而影响前一个点的最短路径，下面的代码没有考虑这种情况
    def minJumps2(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0] * n
        # 记录到达每个数值的最小步骤
        d = defaultdict(int)
        d[arr[0]] = 0

        for x in range(1, n):
            val = arr[x]
            dp[x] = dp[x - 1] + 1
            if val in d:
                dp[x] = min(dp[x], d[val] + 1)
                d[val] = min(dp[x], d[val])
            else:
                d[val] = dp[x]
            # 更新前一个位置的最小步骤
            for j in range(x, 1, -1):
                if dp[j] + 1 < dp[j - 1]:
                    dp[j - 1] = dp[j] + 1
                    d[arr[j - 1]] = min(dp[j - 1], d[arr[j - 1]])
                else:
                    break
        return dp[n - 1]


if __name__ == '__main__':
    # Counter支持加减操作
    c1 = Counter("aa")
    c2 = Counter("aab")
    print(c1)
    print(c2)
    # 两者同key的值相减；
    # 只在c1中存在的key，只有数量为负数，才会处理，即在c2中添加该key，数量为正
    print("计算交集： ", c2 & c1)
    print("计算并集： ", c2 | c1)
    print("计算加法： ", c2 + c1)
    print("计算减法： ", c2 - c1)
    print(not c1 - c2)
    print(not c1)

    # dict 不支持加减操作
    d1 = {"a": 5, "b": 3, "d": 8}
    d2 = {"a": 3, "b": 3, "c": 3}

    # print(d1 - d2)
    # print(d2 - d1)
    cur = [25, -28, -51, 61, -74, -51, -30, 58, 36, 68, -80, -64, 25, -30, -53, 36, -74, 61, -100, -30, -52]
