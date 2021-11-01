from typing import List


class Solution:
    # 排序 + 优先队列 ==》 贪心算法
    # FIXME 超时
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        sorted_events = sorted(events, key=lambda x: (-1 * x[2], x[0], x[1]))
        n = len(events)

        ans = sorted_events[0][2]
        left = 0
        right = n - 1
        while left < n:
            x, y, v = sorted_events[left]
            right = left + 1
            while right < n:
                x1, y1, v1 = sorted_events[right]
                if y + 1 <= x1:
                    ans = max(ans, v + v1)
                    break
                right += 1
                

        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [[1, 5, 3], [1, 5, 1], [6, 6, 5]]
    sol.maxTwoEvents(nums)
