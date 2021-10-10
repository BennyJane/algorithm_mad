class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        count = 0
        for i in range(1, n + 1):
            count += i
            if count <= n:
                ans += 1
            else:
                break
        return ans

    def arrangeCoins2(self, n: int) -> int:
        return int((pow(8 * n + 1, 0.5) - 1) / 2)

    # 二分法
    #  n 枚硬币至少可以组成 1 个完整阶梯行，至多可以组成 n 个完整阶梯行（在 n = 1n=1 时得到）。
    def arrangeCoins3(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            # 先加1再除以2是为了让中间值靠右，因为在后序对右边的值处理是 right = mid - 1
            mid = (left + right + 1) // 2
            if mid * (mid + 1) <= 2 * n:
                left = mid
            else:
                right = mid - 1
        return left

