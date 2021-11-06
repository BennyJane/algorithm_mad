from typing import List

from sortedcontainers import SortedList

"""
--------------------------------------------------------------------
单串： 最大子数组和系列
--------------------------------------------------------------------
"""


# 最大子序和 SIMPLE ==》 Kanada算法
class Solution1:
    # 前缀和 + 暴力遍历
    # TODO 超时
    def maxSubArray1(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        ans = nums[0]
        for i in range(n + 1):
            for j in range(i + 1, n + 1):  # FIXME 反向，向前遍历 ==》 自底向上
                temp = pre[j] - pre[i]
                ans = max(ans, temp)
                if temp <= 0:
                    break
        return ans

    def maxSubArray2(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        # dp[i]: 以i结尾的 连续子数组的最大和
        # 默认值：子数组长度为1的情况
        dp = list(nums)

        ans = nums[0]
        for i in range(i + 1, n):
            dp[i] = max(dp[i], dp[i - 1] + nums[i])
            ans = max(ans, dp[i])
        return ans

    def maxSubArray(self, nums: List[int]) -> int:
        _max = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
            _max = max(_max, nums[i])
        return _max

    # TODO 分治算法


# 乘积最大子组数
# 得到了一个结论：当前位置的最优解未必是由前一个位置的最优解转移得到的。
class Solution2:
    def maxProduct1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]
        # 初始化：区别正数、负数、零
        for i, num in enumerate(nums):
            if num == 0:
                dp[i] = [0, 0]
            elif num > 0:
                # FIXME 负数的初始值也设置为1，避免影响原数据的正负性
                dp[i] = [num, 1]
            else:
                dp[i] = [1, num]

        ans = max(nums)
        for i in range(1, n):
            if nums[i - 1] != 0:
                cur = nums[i]
                if cur >= 0:
                    dp[i][0] = max(cur, dp[i - 1][0] * nums[i])
                    dp[i][1] = min(dp[i][1], dp[i - 1][1] * nums[i])
                else:
                    dp[i][0] = max(dp[i][0], dp[i - 1][1] * nums[i])
                    dp[i][1] = min(cur, dp[i - 1][0] * nums[i])
                ans = max(ans, dp[i][0])
        return ans

    # TODO 优化空间 ==》 只使用两个常量
    def maxProduct2(self, nums: List[int]) -> int:
        n = len(nums)
        # 设置两个dp，存储两种不同状态
        pre_max = list(nums)  # 维护正数乘积最大值
        pre_min = list(nums)  # 维护负数乘积最小值

        for i in range(1, n):
            cur = nums[i]
            if cur >= 0:
                pre_max[i] = max(cur, pre_max[i - 1] * cur)
                pre_min[i] = min(cur, pre_min[i - 1] * cur)
            else:
                pre_max[i] = max(cur, pre_min[i - 1] * cur)
                pre_min[i] = min(cur, pre_max[i - 1] * cur)

        return max(pre_max)

    # FIXME 错误： 没有考虑负数情况
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = list(nums)

        for i in range(1, n):
            if nums[i - 1] != 0:
                # 不能直接取最大值
                dp[i] = max(dp[i], dp[i - 1] * nums[i])
        return max(dp)


# 环形子数组的最大和
# FIXME 题目没有说明，但确实按照连续数组处理（不连续的话，没有意义，直接将所有正数相加即可）
class Solution3:
    """
    --------------------------------------------------------
    主要分两种情况：
    - 最大子数组位于数组内部：等效于 题目：最大连续子数组
    - 最大子数组位于两端 =》即分布在头尾 等效：计算最小的连续子数组(反向思考)
    --------------------------------------------------------
    """

    def maxSubarraySumCircular(self, nums: List[int]) -> float:
        s = nums[0]
        pre_max = list(nums)
        pre_min = list(nums)

        n = len(nums)
        for i in range(1, n):
            pre_max[i] = max(nums[i], pre_max[i - 1] + nums[i])
            pre_min[i] = min(nums[i], pre_min[i - 1] + nums[i])
            s += nums[i]

        ans = float("-inf")
        # FIXME 当所有数都为负数时，最小连续子数组等于原数组 ==》 此时，最大值等于原数组最大值
        # 其他情况下：分布头尾的最大连续子数组 = 数组总和 - 最小连续子数组
        if min(pre_min) == s:
            ans = max(ans, max(nums))
        else:
            ans = max(ans, s - min(pre_min))
        return max(ans, max(pre_max))

    # FIXME 模拟法：暴力 JAVA可通过 PY无法通过
    def maxSubarraySumCircular1(self, nums: List[int]) -> float:
        n = len(nums)

        left = 0
        ans = float("-inf")
        while left < n:
            temp = nums[left]
            max_value = nums[left]
            right = left + 1
            while right <= n - 1 + left and temp + nums[right % n] > 0:
                temp += nums[right % n]
                max_value = max(temp, max_value)
                right += 1
            ans = max(ans, max_value)
            left += 1

        return ans


# 矩形区域不超过 K 的最大数值和 HARD
class Solution:
    # 有序集合
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = float("-inf")
        m, n = len(matrix), len(matrix[0])

        for i in range(m):  # 枚举上边界
            total = [0] * n
            for j in range(i, m):  # 枚举下边界：矩形起始行
                # 计算竖向累计和
                for c in range(n):
                    total[c] += matrix[j][c]  # 更新每列的元素和
                # 初始化有序队列
                totalSet = SortedList([0])
                # 逐层讨论可能性
                s = 0   # 计算不同宽度矩形和
                for v in total:
                    s += v
                    # 二分法查找最接近 s -k值的索引
                    # lb索引对应值，必须 >= s -k ,过小则会导致矩形和超过k
                    lb = totalSet.bisect_left(s - k)
                    if lb != len(totalSet):
                        ans = max(ans, s - totalSet[lb])
                    totalSet.add(s)

        return ans


if __name__ == '__main__':
    # sol = Solution1()
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # sol.maxSubArray1(nums)

    sol = Solution2()
    nums = [2, 3, -2, 4]
    sol.maxProduct1(nums)
