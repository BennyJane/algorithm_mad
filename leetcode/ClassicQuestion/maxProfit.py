from typing import List


# 122. 买卖股票的最佳时机 II
class Solution15:
    """
    动态规划
    贪心
    """

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        # 持有现金：即不持有股票状态
        cash = 0
        # 持有股票：
        hold = -1 * prices[0]

        # 记录上一个状态
        preCash = cash
        preHold = hold

        for i in range(1, n):
            # 当前索引位置：持有金额来源有两个
            # 不操作，与前一个相同； 执行卖出操作
            cash = max(preCash, preHold + prices[i])
            hold = max(preHold, preCash - prices[i])
            preCash = cash
            preHold = hold
        return cash

    # 贪心算法那
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        ans = 0
        for i in range(1, n):
            ans += max(prices[i] - prices[i - 1], 0)

        return ans


# 309. 最佳买卖股票时机含冷冻期 MIDDLE
class Solution16:
    def maxProfit(self, prices: List[int]) -> int:
        return 0


# 714. 买卖股票的最佳时机含手续费 MIDDLE
class Solution17:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
            return 0

        # 记录每个位置的状态：0 不持有股票 1 持有股票
        dp = [[0] * 2 for _ in range(n)]
        dp[0][1] = -1 * prices[0] - fee

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)

        return dp[n - 1][0]

    def maxProfit1(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
            return 0
        sell = 0
        buy = -prices[0]

        for i in range(1, n):
            sell = max(sell, buy + prices[i] - fee)
            # FIXME 可以通过测试用例，但逻辑上不正确，下一步计算时使用的sell，可能已经被修改过
            # 可以证明不影响结果：
            # sell >= buy + prices[i] - fee ==> sell 不变
            # sell < buy + prices[i] - fee ==> sell = buy + prices[i] - fee, 带入下一个不等式，结果选buy,不影响结果
            buy = max(buy, sell - prices[i])
        return sell

    def maxProfit3(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        sell, buy = 0, -prices[0]
        for i in range(1, n):
            sell, buy = max(sell, buy + prices[i] - fee), max(buy, sell - prices[i])
        return sell


# 123. 买卖股票的最佳时机 III HARD
class Solution18:
    """
    最多允许完成2笔交易
    分析不同状态后续操作的可能性
    初始状态：没有任何买入与卖出操作，可以进行任意操作
    第一笔买入状态：不操作 | 卖出
    第一笔卖出状态：不操作 | 买入
    第二笔买入状态：不操作 | 卖出
    第二笔卖出状态：不操作
    """

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        ans = 0
        dp = [[0, float("-inf"), float("-inf"), float("-inf"), 0] for _ in range(n)]
        dp[0][1] = -1 * prices[0]
        dp[0][3] = -1 * prices[0]
        for i in range(1, n):
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            ans = max(ans, dp[i][2])
            # FIXME 需要保证第一笔交易完成: 不需要保证这一条件
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
            ans = max(ans, dp[i][4])
        return ans

    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2


# 188. 买卖股票的最佳时机 IV HARD
class Solution19:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0] * (k * 2 + 1) for _ in range(n)]
        for i in range(1, k * 2 + 1):
            if i % 2 == 1:
                dp[0][i] = -1 * prices[0]

        ans = 0
        for i in range(1, n):
            for j in range(1, k * 2 + 1):
                if j % 2 == 1:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])
                    ans = max(ans, dp[i][j])
        return ans

    def maxProfit2(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        buy = [0] * (k + 1)
        sell = [0] * (k + 1)

        buy[0], sell[0] = -prices[0], 0
        for i in range(1, k + 1):
            buy[i] = sell[i] = float("-inf")

        for i in range(1, n):
            buy[0] = max(buy[0], sell[0] - prices[i])
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j] - prices[i])
                sell[j] = max(sell[j], buy[j - 1] + prices[i]);

        return max(sell)


# 689. 三个无重叠子数组的最大和
class Solution20:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 计算前缀和
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)

        dp = [list() for _ in range(n)]
        for i in range(n):
            # i 索引位置有4个状态：
            # 0：没有选取子数组 1: 选取一个子数组，且该子数组的末尾索引为i
            # 2: 选取2个子数组，且该子数组的末尾索引为i
            # 3: 选取3个子数组，且该子数组的末尾索引为i
            for j in range(4):
                # 索引i位置选择j个子数组的和，以及每个子数组的起始索引
                dp[i].append([0])

        ans = [0]
        for i in range(n):
            for j in range(1, 4):
                # 确保长度可以容纳
                if i + 1 < j * k:
                    break
                dp[i][j] = list(dp[i - 1][j])
                # 来源有两个
                # 当前索引作为第j个子数组的末尾索引
                res1 = dp[i - k][j - 1][0] + pre[i + 1] - pre[i - k + 1]
                # 前一个索引作为第j个子数组的末尾索引
                res2 = dp[i - 1][j][0]

                if res1 > res2 or (res1 == res2 and dp[i - 1][j][-1] > i - k + 1):
                    dp[i][j] = list(dp[i - k][j - 1])
                    dp[i][j][0] = res1
                    dp[i][j].append(i + 1 - k)
                if j == 3 and dp[i][j][0] > ans[0]:
                    ans = dp[i][j]

        return ans[1:]

    # 计算选取k个不相交子数组的最大和
    def maxSumOfThreeSubarrays2(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 计算前缀和
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)
        # 3个子数组
        ARRAY_NUM = 3
        dp = [[] for _ in range(n)]
        for i in range(n):
            # 每个索引位置有4个状态：表示已经选择的子数组个数0 1 2 3
            dp[i] = [0] * (ARRAY_NUM + 1)

        for i in range(n):
            for j in range(1, ARRAY_NUM + 1):
                if i + 1 < j * k:
                    break
                dp[i][j] = max(dp[i - 1][j], dp[i - k][j - 1] + pre[i + 1] - pre[i + 1 - k])
        return dp[n - 1][ARRAY_NUM]
