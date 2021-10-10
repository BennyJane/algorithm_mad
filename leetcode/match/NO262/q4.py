# 5897. 将数组分成两个数组并最小化数组和的差
# https://leetcode-cn.com/contest/weekly-contest-262/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
from collections import defaultdict
from typing import List
import math
from functools import lru_cache


# FIXME 递归:超时
class Solution1:
    ans = math.pow(10, 10)
    total = 0

    def minimumDifference(self, nums: List[int]) -> int:
        self.total = sum(nums)
        self.dfs(nums, 0, 0, 0)
        return self.ans

    def dfs(self, nums, index, count, half):
        n = len(nums)
        if count >= len(nums) // 2:
            another = self.total - half
            self.ans = min(self.ans, abs(half - another))
            return
        if index >= n:
            return
        for i in range(index, len(nums)):
            cur = nums[i]
            # TODO 考虑两种情况
            self.dfs(nums, i + 1, count, half)
            self.dfs(nums, i + 1, count + 1, half + cur)


class Solution:
    # 折半搜索 + 状态压缩 + 二分法/双指针
    def minimumDifference(self, nums: List[int]) -> int:
        s = sum(nums)
        # target 不一定为正数
        target = s // 2
        n = len(nums) // 2
        # 等长切分数组
        a = nums[:n]
        b = nums[n:]

        # 记录不同长度的分组情况：对应的和
        dpa = defaultdict(set)
        dpb = defaultdict(set)
        dpa[0].add(0)
        dpb[0].add(0)
        # 状态压缩计算每个长度对应的不同计算结果
        # 子序列个数计算
        for i in range(1 << n):
            # 计算取多少个值
            cnt = bin(i).count('1')
            sa = 0
            sb = 0
            # 统计i对应的状态下，分组数据和
            for j in range(n):
                if i >> j & 1:
                    sa += a[j]
                    sb += b[j]
            # 记录不同状态分组和
            dpa[cnt].add(sa)
            dpb[cnt].add(sb)

        res = math.inf
        # 双指针
        for i in range(n + 1):
            # 防止一边为0，需要补0，排序后二分查找/双指针查找
            # 两个分组中取长度为n的数据
            # aa取最小值,ab取最大值
            aa = sorted(list(dpa[i]))
            ab = sorted(list(dpb[n - i]))
            i, j = 0, len(ab) - 1
            while i < len(aa) and j >= 0:
                if aa[i] + ab[j] == target:
                    return abs(target * 2 - s)
                elif i + 1 < len(aa) and aa[i] + ab[j] < target:
                    i += 1
                else:
                    j -= 1
                res = min(res, abs(s - 2 * (aa[i] + ab[j])))
        return res


if __name__ == '__main__':
    nums = [2, -1, 0, 4, -2, -9]
    nums = [-36, 36]
    nums = [0, 6, 11, 17, 18, 24]
    nums = [76, 8, 45, 20, 74, 84, 28, 1]
    sol = Solution()
    sol.minimumDifference(nums)
