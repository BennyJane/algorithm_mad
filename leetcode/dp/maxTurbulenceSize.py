from typing import List


# 978. 最长湍流子数组
class Solution1:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        # 标注每个区间比较符号： >  1; < -1; = 0
        pre = [0] * (n - 1)
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                cur = 1
            elif arr[i] < arr[i - 1]:
                cur = -1
            else:
                cur = 0
            pre[i - 1] = cur
        # 求 满足相邻数字乘积为负数 的最大长度子数组
        # [1, 0, -1, 1, -1, 1, 0, -1, 0]
        ans = 0
        length = 0
        for i in range(0, n - 1):
            if pre[i] == 0:
                length = 0
            elif pre[i] * pre[i - 1] < 0:
                length += 1
            else:
                # 当前值不为0，前一个数为相同数值 或 0
                length = 1
            ans = max(ans, length + 1)
        return max(ans, 1)

    def maxTurbulenceSize2(self, arr: List[int]) -> int:
        n = len(arr)
        # 处理特例：虽然下面的代码可以处理这种情况；但直接返回，效率更高
        if n < 2:
            return n
        # length 统计：连续的满足条件的间隔数量
        ans = length = 0
        # 前一个间隔比较结果：默认值0，处理第一个间隔的length计算
        pre = 0  # 记录前一个比较结果： 正数 0 负数
        for i in range(1, n):
            diff = arr[i] - arr[i - 1]
            if diff == 0:  # 相等的情况需要直接跳过
                length = 0
            elif diff * pre < 0:  # 相邻两个间隔的比较结果相反
                length += 1
            else:  # 当前比较符号不为=情况
                length = 1
            pre = diff
            ans = max(ans, length + 1)
        # ans最小值为1
        return max(ans, 1)

    # 动态规划: dp[i][k] k = 2表示每个索引处，有两种状态：大于 小于
    def maxTurbulenceSize4(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[1, 1] for _ in range(n)]
        ans = 1
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                dp[i][0] = dp[i - 1][1] + 1
            elif arr[i - 1] < arr[i]:
                dp[i][1] = dp[i - 1][0] + 1
            ans = max(ans, dp[i][0], dp[i][1])
        return ans

    # 动态规划优化
    def maxTurbulenceSize5(self, arr: List[int]) -> int:
        n = len(arr)
        up = down = 1
        ans = 1
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                up = down + 1
                down = 1
            elif arr[i - 1] < arr[i]:
                down = up + 1
                up = 1
            else:
                down = up = 1
            ans = max(ans, up, down)
        return ans

    # 滑动窗口
    def maxTurbulenceSize6(self, arr: List[int]) -> int:
        n = len(arr)
        l = r = 0
        ans = 1

        while r < n - 1:
            if l == r:
                # FIXME 跳过相等的情况
                if arr[l] == arr[l + 1]:
                    l += 1
                r += 1
            else:
                if arr[r - 1] < arr[r] and arr[r] > arr[r + 1]:
                    r += 1
                elif arr[r - 1] > arr[r] and arr[r] < arr[r + 1]:
                    r += 1
                else:
                    l = r
            ans = max(ans, r - l + 1)
        return ans

    def maxTurbulenceSize3(self, A: List[int]) -> int:
        if len(A) == 1 or min(A) == max(A): return 1
        dp = [1] * len(A)
        for i in range(1, len(A) - 1):
            if A[i - 1] > A[i] < A[i + 1] or A[i - 1] < A[i] > A[i + 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp) + 1


if __name__ == '__main__':
    sol = Solution1()
    # arr = [37, 199, 60, 296, 257, 248, 115, 31, 273, 176]
    arr = [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]
    sol.maxTurbulenceSize(arr)
