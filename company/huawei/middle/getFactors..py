from typing import List


# 254. 因子的组合
# https://leetcode-cn.com/problems/factor-combinations/
class Solution:
    # S: 递归；去重；动态规划
    def getFactors(self, n: int) -> List[List[int]]:
        def dfs(n, l):
            res = []
            for i in range(l, int(sqrt(n)) + 1):
                if n % i == 0:
                    res.append([i, n // i])
                    for sub in dfs(n // i, i):
                        res.append(sub + [i])
            return res

        return dfs(n, 2)

    def getFactors2(self, n: int) -> List[List[int]]:
        import math
        if n == 1:
            return []

        def backtrace(m, start):
            for i in range(start, int(math.sqrt(m) + 1)):
                if m % i != 0:
                    continue
                path.append(i)
                res.append(path[:] + [m // i])
                backtrace(m // i, i)
                path.pop()

        path = []
        res = []
        backtrace(n, 2)
        return res


if __name__ == '__main__':
    print(3 // 9)
    print(6 // 9)
    print(5 // 2)
    sol = Solution()
    sol.getFactors(12)
    # print(sol.check(4))
