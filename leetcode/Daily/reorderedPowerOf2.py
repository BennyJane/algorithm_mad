from typing import List


# 869. 重新排序得到 2 的幂
class Solution:
    # FIXME 超时
    def reorderedPowerOf2(self, n: int) -> bool:
        if n == 1:
            return True
        num = str(n)
        length = len(num)
        visited = [False for _ in range(length)]
        target = [2 ** i for i in range(32)]

        def dfs(cnt, pre: List[str]) -> bool:
            if cnt >= length:
                cur = int("".join(pre))
                if cur in target:
                    return True
                return False
            for i in range(0, length):
                if visited[i]:
                    continue
                if not pre and num[i] == '0':
                    continue
                pre.append(num[i])
                visited[i] = True
                if dfs(cnt + 1, pre):
                    return True
                pre.pop()
                visited[i] = False
            return False

        return dfs(0, [])


class Solution2:
    def reorderedPowerOf2(self, n: int) -> bool:
        nums = sorted(list(str(n)))
        m = len(nums)
        vis = [False] * m

        def isPowerOfTwo(n: int) -> bool:
            return (n & (n - 1)) == 0

        def backtrack(idx: int, num: int) -> bool:
            if idx == m:
                return isPowerOfTwo(num)
            for i, ch in enumerate(nums):
                # 不能有前导零
                if (num == 0 and ch == '0') or vis[i] or (i > 0 and not vis[i - 1] and ch == nums[i - 1]):
                    continue
                vis[i] = True
                if backtrack(idx + 1, num * 10 + ord(ch) - ord('0')):
                    return True
                vis[i] = False
            return False

        return backtrack(0, 0)


if __name__ == '__main__':
    sol = Solution()
    sol.reorderedPowerOf2(46)
