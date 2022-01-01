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


# 53.最大子数组和
class Solution2:
    # 动态规划：每个位置处最大值来源有两种，当前值 + 前面的和 or 只取当前值
    # 统计索引i为结尾的连续子数组的最大值
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i]: 以i结尾的 连续子数组的最大和
        # 默认值：子数组长度为1的情况
        dp = list(nums)

        ans = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i], dp[i - 1] + nums[i])
            ans = max(ans, dp[i])
        return ans

    def maxSubArray1(self, nums: List[int]) -> int:
        pre = 0
        ans = nums[0]
        for c in nums:
            # TODO 当前值必须取
            pre = max(pre + c, c)
            ans = max(ans, pre)
        return ans

    # 前缀和
    def maxSubArray2(self, nums: List[int]) -> int:
        n = len(nums)
        # 先计算前缀和
        pre = [0]
        for c in nums:
            pre.append(pre[-1] + c)

        ans = float("-inf")
        # 每个索引位置处的前缀和 - 之前的最小前缀和
        preMin = 0
        for i in range(1, n + 1):
            ans = max(ans, pre[i] - preMin)
            preMin = min(preMin, pre[i])

        return ans

    def maxSubArray21(self, nums: List[int]) -> int:
        ans = float("-inf")
        # 先计算前缀和
        preMin = 0
        pre = 0
        for c in nums:
            pre += c
            # 每个索引位置处的前缀和 - 之前的最小前缀和
            ans = max(ans, pre - preMin)
            preMin = min(preMin, pre)
        return ans

    def maxSubArray3(self, nums: List[int]) -> int:
        r = 0
        windows = float("-inf")
        ans = float("-inf")

        n = len(nums)
        while r < n:
            if windows > 0:
                windows += nums[r]
            else:
                windows = nums[r]
            r += 1
            ans = max(ans, windows)
        return ans

    # 分治算法
    def maxSubArray4(self, nums: List[int]) -> int:

        class Status:
            def __init__(self, lSum, rSum, mSum, iSum):
                self.lSum = lSum
                self.rSum = rSum
                self.mSum = mSum
                self.iSum = iSum

        # 寻找区间[left : right], 两个端点都可以取到
        def getInfo(left, right):
            # 区间长度为1，特殊处理
            if left == right:
                return Status(nums[left], nums[left], nums[left], nums[left])
            mid = (left + right) // 2
            lStatus = getInfo(left, mid)
            rStatus = getInfo(mid + 1, right)
            return pushUp(lStatus, rStatus)

        def pushUp(leftStatus: Status, rightStatus: Status):
            lSum = max(leftStatus.lSum, leftStatus.iSum + rightStatus.lSum)
            rSum = max(rightStatus.rSum, rightStatus.iSum + leftStatus.rSum)
            mSum = max(leftStatus.mSum, rightStatus.mSum, leftStatus.rSum + rightStatus.lSum)
            iSum = leftStatus.iSum + rightStatus.iSum
            return Status(lSum, rSum, mSum, iSum)

        return getInfo(0, len(nums) - 1).mSum


if __name__ == '__main__':
    sol = Solution()
    nusm = [1, -1, 5, -2, 3]
    sol.maxSubArrayLen(nusm, k=3)
