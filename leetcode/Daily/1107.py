from typing import List


# 598. 范围求和 II
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n

        min_width = float("inf")
        min_height = float("inf")

        for w, h in ops:
            min_width = min(w, min_width)
            min_height = min(h, min_height)

        return min_width * min_height

    def maxCount2(self, m: int, n: int, ops: List[List[int]]) -> int:
        mina, minb = m, n
        for a, b in ops:
            mina = min(mina, a)
            minb = min(minb, b)
        return mina * minb


# 370. 区间加法
class Solution1:
    # 差分法 > 模拟法
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * (length + 1)
        # TODO 注意索引范围： end 对应索引也是包含在inc范围后，应该从后一个索引开始-inc
        for start, end, inc in updates:
            ans[start] += inc
            ans[end + 1] -= inc

        total = 0
        for i, v in enumerate(ans):
            total += v
            ans[i] = total
        return ans[:-1]


# 520. 检测大写字母
class Solution2:
    def detectCapitalUse(self, word: str) -> bool:
        ori = word
        choices = [word.lower(), word.upper(), word[0].upper() + word[1:].lower()]

        return ori in choices

    def detectCapitalUse1(self, word: str) -> bool:
        # 若第 1 个字母为小写，则需额外判断第 2 个字母是否为小写
        if len(word) >= 2 and word[0].islower() and word[1].isupper():
            return False

        # 无论第 1 个字母是否大写，其他字母必须与第 2 个字母的大小写相同
        return all(word[i].islower() == word[1].islower() for i in range(2, len(word)))


# 677. 键值映射
# 可以使用字典树
# https://leetcode-cn.com/problems/map-sum-pairs/
class MapSum:

    def __init__(self):
        self.cache = dict()

    def insert(self, key: str, val: int) -> None:
        self.cache[key] = val

    def sum(self, prefix: str) -> int:
        ans = 0
        for key, val in self.cache.items():
            if str(key).startswith(prefix):
                ans += val
        return ans
