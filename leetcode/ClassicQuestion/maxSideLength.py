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

        prefixSum = [[0] * (n + 1) for _ in range(m + 1)]


