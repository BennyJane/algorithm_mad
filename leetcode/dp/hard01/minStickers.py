import collections
from cmath import inf
# from linecache import cache
from functools import lru_cache
from typing import List
from collections import Counter


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
        dp[0] = 0   # 初始状态：不包含任意target中的字符
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
