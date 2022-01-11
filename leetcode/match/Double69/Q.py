from typing import Optional, List
from collections import defaultdict


class Solution1:
    def capitalizeTitle(self, title: str) -> str:
        arr = title.split(" ")
        for i, c in enumerate(arr):
            if len(c) <= 2:
                arr[i] = c.lower()
            else:
                s = c[0].upper() + c[1:].lower()
                arr[i] = s
        return " ".join(arr)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution2:
    def pairSum(self, head: Optional[ListNode]) -> int:
        pre = head
        arr = []
        n = 0
        while pre:
            arr.append(pre.val)
            pre = pre.next
            n += 1

        limit = n // 2
        ans = 0
        for i in range(limit):
            ans = max(ans, arr[i] + arr[n - 1 - i])

        return ans


class Solution3:
    def longestPalindrome(self, words: List[str]) -> int:
        sameW = []
        cnt = 0
        d = defaultdict(int)

        for w in words:
            if w[0] == w[1]:
                sameW.append(w)
            if w not in d and w[::-1] not in d:
                d[w] += 1
            elif w[0] == w[1]:
                if d[w] != 0:
                    cnt += 1
                if d[w] > 0:
                    d[w] -= 1
                elif d[w] < 0:
                    d[w] += 1
                else:
                    d[w] += 1
            elif w in d:
                if d[w] < 0:
                    cnt += 1
                d[w] += 1
            elif w[::-1] in d:
                reverseW = w[::-1]
                if d[reverseW] > 0:
                    cnt += 1
                d[reverseW] -= 1
        ans = cnt * 4
        for s in sameW:
            if d[s] != 0:
                ans += 2
                break
        return ans


# https://leetcode-cn.com/problems/stamping-the-grid/
# 2132. 用邮票贴满网格图
class Solution:
    class Solution:
        def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
            m, n = len(grid), len(grid[0])
            sum = [[0] * (n + 1) for _ in range(m + 1)]
            for i, row in enumerate(grid):
                for j, v in enumerate(row):  # grid 的二维前缀和
                    sum[i + 1][j + 1] = sum[i + 1][j] + sum[i][j + 1] - sum[i][j] + v

            # 二维差分数组：向右，向下扩展一列、一行
            diff = [[0] * (n + 1) for _ in range(m + 1)]
            for i, row in enumerate(grid):
                for j, v in enumerate(row):
                    if v == 0:
                        x, y = i + stampHeight, j + stampWidth  # 注意这是矩形右下角横纵坐标都 +1 后的位置
                        if x <= m and y <= n and sum[x][y] - sum[x][j] - sum[i][y] + sum[i][j] == 0:
                            diff[i][j] += 1
                            diff[i][y] -= 1
                            diff[x][j] -= 1
                            diff[x][y] += 1  # 更新二维差分

            # 还原二维差分矩阵对应的计数矩阵，这里用滚动数组实现
            cnt, pre = [0] * (n + 1), [0] * (n + 1)
            for i, row in enumerate(grid):
                for j, v in enumerate(row):
                    cnt[j + 1] = cnt[j] + pre[j + 1] - pre[j] + diff[i][j]
                    if cnt[j + 1] == 0 and v == 0:
                        return False
                cnt, pre = pre, cnt
            return True

    def possibleToStamp2(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])

        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] \
                                   - prefix_sum[i - 1][j - 1] + grid[i - 1][j - 1]

        diff = [[0] * (n + 1) for _ in range(m + 1)]

        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 0:
                    x, y = i + stampHeight, j + stampWidth  # 注意这是矩形右下角横纵坐标都 +1 后的位置
                    if x <= m and y <= n and prefix_sum[x][y] - prefix_sum[x][j] - prefix_sum[i][y] + prefix_sum[i][j] == 0:
                        diff[i][j] += 1
                        diff[i][y] -= 1
                        diff[x][j] -= 1
                        diff[x][y] += 1  # 更新二维差分
        diff_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if grid[r - 1][c - 1] == 1:
                    continue
                diff_sum[r][c] = diff_sum[r - 1][c] + diff_sum[r][c - 1] - diff_sum[r - 1][c - 1] + diff[r-1][c-1]
                if diff_sum[r][c] == 0:
                    return False
        return True


if __name__ == '__main__':
    pass
