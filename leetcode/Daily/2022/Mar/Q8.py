from typing import List


# 2055. 蜡烛之间的盘子
class Solution:
    # FIXME 超时
    def platesBetweenCandles2(self, s: str, queries: List[List[int]]) -> List[int]:
        if s.count("|") < 2:
            return 0
        n = len(s)
        cnt = [0] * (n + 1)
        for i, c in enumerate(s):
            if s[i] == '*':
                cnt[i + 1] = cnt[i] + 1
            else:
                cnt[i + 1] = cnt[i]

        ans = [0] * len(queries)
        # 重复计算每个*左右最近的蜡烛位置
        for i, query in enumerate(queries):
            l, r = query
            while l < r and s[l] == '*':
                l += 1
            while l < r and s[r] == '*':
                r -= 1
            if r - l <= 1:
                ans[i] = 0
            else:
                ans[i] = cnt[r + 1] - cnt[l]
        return ans

    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # 前缀和
        pre_sum = [0]
        for c in s:
            nxt = pre_sum[-1] + 1 if c == '*' else pre_sum[-1]
            pre_sum.append(nxt)

        # 查找每个位置左侧最近蜡烛的位置
        left_pos = [-1] * n
        pre_left = -1
        for i, c in enumerate(s):
            if c == '|':
                pre_left = i
            left_pos[i] = pre_left

        right_pos = [-1] * n
        pre_right = -1
        for i in range(n - 1, -1, -1):
            c = s[i]
            if c == '|':
                pre_right = i
            right_pos[i] = pre_right

        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            start, end = q
            l = right_pos[start]
            r = left_pos[end]
            # 需要跳过一侧没有蜡烛的情况
            if l == -1 or r == -1:
                continue
            if r - l >= 2:  # 需要取等号
                ans[i] = pre_sum[r + 1] - pre_sum[l]
        return ans
