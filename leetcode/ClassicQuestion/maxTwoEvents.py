from typing import List
from sortedcontainers import SortedList
import heapq


# 2054. 两个最好的不重叠活动
# https://leetcode-cn.com/problems/two-best-non-overlapping-events/
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        return 0

    # TODO 有序队列(SortedList|TreeSet-java)：利用内置有序集合，优化查询排序的效率
    # FIXME 超时
    def maxTwoEvents1(self, events: List[List[int]]) -> int:
        n = len(events)

        # 按照开始时间升序排列
        events.sort(key=lambda x: x[0])

        # 根据val降序排列
        sortedArr = SortedList(key=lambda x: -1 * x[2])

        ans = 0
        # 逐个任务考虑
        for i in range(n):
            start, end, value = events[i]
            temp = value
            for x, y, val in sortedArr:
                if y < start:
                    temp += val
                    break
            ans = max(ans, temp)
            sortedArr.add(events[i])
        return ans

    # TODO 优先队列(堆)
    # PY中headq默认未小根堆
    def maxTwoEvents3(self, events: List[List[int]]) -> int:
        # 按照开始时间升序排列
        events.sort(key=lambda x: x[0])
        # 初始化小根堆使用列表
        h = list()

        ans = 0
        # 记录已遍历数据中，最大val
        preMax = 0
        for x, y, v in events:
            # 遍历小根堆中，所有结束时间小于当前起始时间的数据
            # 并更新最大值
            while h and h[0] < x:  # h[0]获取小根堆顶部元素，不弹出(不是使用-1)
                preMax = max(preMax, heapq.heappop(h)[1])
            # TODO 最大值来源：当前val 与 位于当前任务左侧(x1 < y1 < x)的最大值
            ans = max(ans, preMax + v)
            # 小根堆排序条件：结束时间与value ==》 value更多是存储价值，避免重新查找
            heapq.heappush(h, [y, v])
        return ans

    # TODO 动态规划
    # 相似题目：https://leetcode-cn.com/problems/maximum-profit-in-job-scheduling/
    # 参考题目：https://leetcode-cn.com/problems/two-best-non-overlapping-events/solution/pai-xu-dong-tai-gui-hua-er-fen-by-verygo-ptd9/
    def maxTwoEvents4(self, events: List[List[int]]) -> int:
        n = len(events)

        # 按照结束时间排序
        events.sort(key=lambda x: x[1])
        """
        one[i]:
         在0~i范围内，选一个最大价值， one[i] = max(one[i -1], events[i][2])
        two[i]:
         在0~i范围内，选择两个的最大价值，two[i] = max(two[i-1], one[j] + events[i][2])
         即 不取当前值，最大值为two[i-1]; 取当前值，最大值为 [0:i]范围内最大one[j] + 当前值        
        """
        one = [0] * n
        two = [0] * n

        for i in range(n):
            # 找到 不重合(左侧y < 右侧x) 的最大索引位置 ==》 one数组中索引越大，值也就越大
            left, right = 0, i - 1
            while left <= right:
                mid = (left + right) >> 1
                if events[mid][1] >= events[i][0]:
                    right = mid - 1
                else:
                    left = mid + 1
            one[i] = events[i][2]

            if right > -1:
                two[i] = one[right] + events[i][2]
            if i > 0:
                one[i] = max(one[i], one[i - 1])
                two[i] = max(two[i], two[i - 1])

        return max(one[n - 1], two[n - 1])


class Event:
    def __init__(self, ts: int, op: int, val: int):
        self.ts = ts
        self.op = op
        self.val = val

    def __lt__(self, other: "Event") -> bool:
        return (self.ts, self.op) < (other.ts, other.op)


class Solution1:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        evs = list()
        for event in events:
            evs.append(Event(event[0], 0, event[2]))
            evs.append(Event(event[1], 1, event[2]))
        evs.sort()

        ans = bestFirst = 0
        for ev in evs:
            if ev.op == 0:
                ans = max(ans, ev.val + bestFirst)
            else:
                bestFirst = max(bestFirst, ev.val)

        return ans


if __name__ == '__main__':
    print(10 >> 1)
