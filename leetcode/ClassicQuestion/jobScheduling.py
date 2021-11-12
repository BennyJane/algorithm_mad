import heapq
from typing import List


# 1235. 规划兼职工作
# https://leetcode-cn.com/problems/maximum-profit-in-job-scheduling/
class Solution1:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        array = list()
        for i in range(n):
            job = startTime[i], endTime[i], profit[i]  # PY 根据逗号，自动封装为元祖
            array.append(job)
        # 结束时间升序 ==》 可以针对结束时间，进行二分法搜索
        array.sort(key=lambda x: x[1])

        # 每个工作，只有选或不选，不需要使用 n + 1的长度
        dp = [0] * n
        dp[0] = array[0][2]

        for i in range(1, n):
            # 最大值来源：前一个 or 只取当前工作
            dp[i] = max(dp[i - 1], array[i][2])
            # 选择当前工作兼职的前提下：
            # 需要找到一个工作结束时间小于当前工作的开始时间，且索引最大（距离当前兼职最近）
            left, right = 0, i - 1  # right = i -1 i索引默认被取
            # 结束时间升序排列，所以可以使用二分法搜索
            # TODO 找到小于or等于目标值target，的最大索引
            while left < right:
                # TODO 核心细节：二分法计算中点的方式, 下面两种方式等效； 必须补加1， 否则无法跳出循环
                # mid = (right + left) // 2 ==> 计算结果为中间偏左(奇数长度为中心，偶数偏左侧)
                # mid = (right + left) // 2 + 1 ==> 计算结果为中间偏右(奇数长度不是中心，而是中心偏右，偶数偏右侧) ==》 优先判断中心偏右，较大值是否满足 小于等于 条件
                mid = (right - left) // 2 + left + 1
                # mid = (right + left) // 2 + 1
                if array[mid][1] <= array[i][0]:
                    left = mid
                else:
                    right = mid - 1
            # 检测退出条件的合理性
            # 可以相等
            if array[left][1] <= array[i][0]:
                dp[i] = max(dp[i], dp[left] + array[i][2])
        return dp[n - 1]

    def jobScheduling2(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        events = []
        for i in range(n):
            events.append((startTime[i], endTime[i], profit[i]))

        # 小根堆
        heapq.heapify(events)
        # 当前的最大收益
        max_profix = 0
        while events:
            # 每次弹出 开始时间最早的任务
            e = heapq.heappop(events)
            if e[1] > 0:
                # 该任务结束那天，可能的最大收益是max_profix加上当前任务的收益
                heapq.heappush(events, (e[1], 0, max_profix + e[2]))
            else:
                # 判断做这个任务是否能带来更多收益
                max_profix = max(max_profix, e[2])
        return max_profix


# 1751. 最多可以参加的会议数目 II
# https://leetcode-cn.com/problems/maximum-number-of-events-that-can-be-attended-ii/
class Solution2:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        # 根据结束时间升序排列
        events.sort(key=lambda x: x[1])
        # 状态方程： 选 or 不选 + 选取数量 k
        # TODO 考虑长度不加1，调换位置
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, val = events[i - 1]
            # 寻找第i件事件前，与i件事件不冲突的事件
            # TODO 优化使用二分法查询
            pre = 0
            for p in range(i - 1, 0, -1):
                s, e, v = events[p - 1]
                if e < start:  # 不能相等
                    pre = p
                    break

            # 考虑不同数量的取值
            for j in range(1, k + 1):
                dp[i][j] = max(dp[i - 1][j], dp[pre][j - 1] + val)

        return dp[n][k]


if __name__ == '__main__':
    sol = Solution1()
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    # sol.jobScheduling(startTime, endTime, profit)
    # sol.jobScheduling2(startTime, endTime, profit)

    sol2 = Solution2()
    nums = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
    sol2.maxValue(nums, 3)
