from typing import List


# 325. 和等于 k 的最长子数组长度
# https://leetcode-cn.com/problems/maximum-size-subarray-sum-equals-k/
class Solution:
    # 前缀和
    # FIXME 超时：不能排序, 没有顺序
    # ？？？pre2 - pre1 = k ==> pre2 - k = pre1 ==> 遍历每个前缀和，判断pre1是否出现过

    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0

        d = dict()
        d[0] = -1

        pre = 0
        for i, v in enumerate(nums):
            pre += v
            if pre not in d:
                d[pre] = i
            if pre - k in d:
                left = d[pre - k]
                ans = max(ans, i - left)
        return ans

    def maxSubArrayLen1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0

        d = dict()  # 记录每个前缀和的索引
        # 初始化起始值：长度为0的结果
        d[0] = 0
        # 前缀和： TODO 可以只使用一个常量
        pre = [0 for _ in range(n + 1)]
        for i in range(n):
            preSum = pre[i] + nums[i]
            pre[i + 1] = preSum
            # FIXME：统一使用前缀和数组索引，相同前缀和，只能取最左侧的索引，即 只取第一个出现的值
            # d[preSum] = min(i + 1, d.get(preSum, 10 ** 6))
            if preSum not in d:
                d[preSum] = i + 1
            target = preSum - k
            if target in d:
                left = d[target]
                ans = max(ans, i - left)

        # 下列代码可以合并到上面
        # for i, p in enumerate(pre):
        #     target = p - k
        #     if target in d:
        #         left = d[target]
        #         ans = max(ans, i - left)
        return ans

    def maxSubArrayLen2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0 for _ in range(n + 1)]
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        ans = 0
        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                temp = pre[j] - pre[i]
                if temp == k:
                    ans = max(ans, j - i)

        return ans


if __name__ == '__main__':
    sol = Solution()
    nusm = [1, -1, 5, -2, 3]
    sol.maxSubArrayLen(nusm, k=3)
