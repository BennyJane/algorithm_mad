from collections import defaultdict
from typing import List


class Solution1:
    # 1292. 元素和小于等于阈值的正方形的最大边长
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # 计算二维前缀和
        # 长宽+1
        prefixSum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # TODO：计算每个位置的前缀和：左 + 上 - 重合部分 + 当前位置的值
                prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + mat[i - 1][
                    j - 1]

        # 计算原数组任意子数组的元素和
        def getSubArea(x1, y1, x2, y2):
            # TODO：传入坐标是 映射为前缀和数组P中的坐标：大 - 左 - 上 + 重合部分
            return prefixSum[x2][y2] - prefixSum[x1 - 1][y2] - prefixSum[x2][y1 - 1] + prefixSum[x1 - 1][y1 - 1]

        ans = 0
        # 枚举所有矩形的左上角的位置
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 判断是否存在更大长度的正方形
                width = ans + 1
                while i + width - 1 <= m and j + width - 1 <= n and getSubArea(i, j, i + width - 1,
                                                                               j + width - 1) <= threshold:
                    ans = max(ans, width)
                    width += 1
        return ans

    # 二分法查找
    def maxSideLength2(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # 计算二位数狐族前缀和
        pS = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pS[i][j] = pS[i - 1][j] + pS[i][j - 1] - pS[i - 1][j - 1] + mat[i - 1][j - 1]

        def getRect(x1, y1, x2, y2):
            return pS[x2][y2] - pS[x1 - 1][y2] - pS[x2][y1 - 1] + pS[x1 - 1][y1 - 1]

        # 分析正方形边长取值范围[0, min(m, n)]
        l, r = 0, min(m, n)
        ans = 0
        while l <= r:
            # 正方向边长取 中间值 mid
            mid = (l + r) // 2
            isExist = False
            # 遍历所有矩形左上角点的可能范围
            # TODO 放在pS前缀和矩阵中讨论
            for x in range(1, m + 1 - (mid - 1)):
                for y in range(1, n + 1 - (mid - 1)):
                    if getRect(x, y, x + mid - 1, y + mid - 1) <= threshold:
                        ans = max(ans, mid)
                        isExist = True
                        break
            if isExist:
                l = mid + 1
            else:
                r = mid - 1
        return ans

    def maxSideLength3(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1]

        def getRect(x1, y1, x2, y2):
            return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]

        r, ans = min(m, n), 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for c in range(ans + 1, r + 1):
                    if i + c - 1 <= m and j + c - 1 <= n and getRect(i, j, i + c - 1, j + c - 1) <= threshold:
                        ans += 1
                    else:
                        break
        return ans


# 1477.找两个和为目标值且不重叠的子数组
class Solution2:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # 记录前缀和的索引：同一个前缀和，只记录最右侧索引，确保和为target的子数组长度最小 ==》记录最左侧索引，则可用来计算子数组最长值
        d = defaultdict(int)
        d[0] = -1

        n = len(arr)
        # dp[i]: 以i为结尾的和为target的数组，最短长度
        # TODO 记录作用
        dp = [float("inf")] * n

        ans = float("inf")
        pre = 0
        for i, c in enumerate(arr):
            pre += c
            # 先设置默认值，
            if i > 0:
                dp[i] = dp[i - 1]
            # 以当前i索引位置的子数组，可以构成和为target的连续子数组，需要更新dp[i]的值
            if pre - target in d.keys():
                left = d[pre - target]
                width = i - left
                # 假设取当前子数组，即其中一个子数组宽度为width，范围(left, i], left未取到
                # 此时，需要寻找[0, left]范围内，和为target的最短子数组，可能存在，也可能不存在
                if dp[left] != float("inf"):
                    ans = min(ans, width + dp[left])
                dp[i] = min(width, dp[i])
            # 覆盖前面出现过的同值前缀和的情况
            d[pre] = i
        return ans if ans != float("inf") else -1

    # 滑动窗口 + 动态规划
    def minSumOfLengths2(self, arr: List[int], target: int) -> int:
        n = len(arr)
        dp = [float("inf")] * (n + 1)
        ans = float("inf")

        l = win = 0
        for r in range(n):
            win += arr[r]
            while win > target:
                win -= arr[l]
                l += 1
            if win == target:
                width = r - l + 1
                ans = min(ans, dp[l] + width)
                dp[r + 1] = min(width, dp[r])
            else:
                dp[r + 1] = dp[r]

        return -1 if ans == float("inf") else ans
