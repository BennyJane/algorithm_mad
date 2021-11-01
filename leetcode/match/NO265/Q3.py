from typing import List


# 广度优先算法
class Solution:
    ans = None

    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        self.ans = float("inf")
        self.dfs(nums, start, goal, 0)
        return self.ans

    def dfs(self, arr, num: int, goal, step):
        if num == goal:
            self.ans = min(self.ans, step)
        if num > 1000:
            return

        for i, val in enumerate(arr):
            self.dfs(arr, num + val, goal, step + 1)
            self.dfs(arr, num - val, goal, step + 1)
            self.dfs(arr, num ^ val, goal, step + 1)


class Solution1:
    ans = None

    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        stack = [start]
        visited = set()
        visited.add(start)
        step = 0
        while stack:
            temp = []
            for pre in stack:
                if pre == goal:
                    return step
                if pre > 1000 or pre < 0:
                    continue
                for n in nums:
                    next_start = pre + n
                    if next_start not in visited:
                        temp.append(next_start)
                        visited.add(next_start)
                    next_start = pre - n
                    if next_start not in visited:
                        temp.append(next_start)
                        visited.add(next_start)
                    next_start = pre ^ n
                    if next_start not in visited:
                        temp.append(next_start)
                        visited.add(next_start)
            stack = temp
            step += 1
        return -1


if __name__ == '__main__':
    sol = Solution1()
    # nums = [2, 4, 12]
    # start = 2
    # goal = 12

    nums = [-17]
    start = 96
    goal = 79
    sol.minimumOperations(nums, start, goal)


"""
[3,5,7]
0
-4

[-17]
96
79



"""