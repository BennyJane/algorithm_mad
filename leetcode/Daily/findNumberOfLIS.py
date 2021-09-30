from typing import List


class Solution:
    max_count = 0
    max_len = 0

    def findNumberOfLIS(self, nums: List[int]) -> int:
        self.dfs(nums, 0, [])
        return self.max_count

    def dfs(self, nums, index, res):
        if index >= len(nums):
            if len(res) > self.max_len:
                self.max_len = len(res)
                self.max_count = 1
            elif len(res) == self.max_len:
                self.max_count += 1
            return

        c = 0
        for i in range(index, len(nums)):
            cur = nums[i]
            if len(res) == 0:
                c += 1
                res.append(cur)
                self.dfs(nums, i + 1, list(res))
                res = res[:-1]
                continue
            elif nums[i] > res[-1]:
                c += 1
                res.append(cur)
                self.dfs(nums, i + 1, list(res))
                res = res[:-1]
        if c == 0:
            self.dfs(nums, len(nums), res)

if __name__ == '__main__':
    sol = Solution()
    l = [1, 3, 5, 4, 7]
    l = [2, 2, 2, 2, 2]
    sol.findNumberOfLIS(l)
