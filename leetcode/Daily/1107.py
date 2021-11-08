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
