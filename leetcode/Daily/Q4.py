# 650. 只有两个键的键盘
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0 for _ in range(1001)]
        dp[1] = 0
        for i in range(2, n + 1):
            if i % 2 == 0:
                dp[i] += dp[i >> 1] + 2
            else:
                max_val = 1
                # 求最大因数
                for j in range(i - 1, 1, -1):
                    if i % j == 0:
                        max_val = j
                        break
                if max_val == 1:
                    dp[i] = i
                else:
                    dp[i] = dp[max_val] + (i / max_val)

        return dp[n]


if __name__ == '__main__':
    sol = Solution()
    sol.minSteps(15)
