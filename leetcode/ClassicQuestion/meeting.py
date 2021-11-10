import heapq
from typing import List
from heapq import heappop
from heapq import heappush
from heapq import heapify
from heapq import heapreplace
from collections import defaultdict

"""
------------------------------------------------------------------
会议相关
------------------------------------------------------------------
"""


# 598. 范围求和 II
class Solution2_0:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n

        min_width = float("inf")
        min_height = float("inf")

        for w, h in ops:
            min_width = min(w, min_width)
            min_height = min(h, min_height)

        return min_width * min_height

    def maxCount2(self, m: int, n: int, ops: List[List[int]]) -> int:
        mina, minb = m, n
        for a, b in ops:
            mina = min(mina, a)
            minb = min(minb, b)
        return mina * minb


# 370. 区间加法
class Solution2_1:
    # 差分法 > 模拟法
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * (length + 1)
        # TODO 注意索引范围： end 对应索引也是包含在inc范围后，应该从后一个索引开始-inc
        for start, end, inc in updates:
            ans[start] += inc
            ans[end + 1] -= inc

        total = 0
        for i, v in enumerate(ans):
            total += v
            ans[i] = total
        return ans[:-1]


# 252. 会议室
# https://leetcode-cn.com/problems/meeting-rooms/
class Solution1:
    """
    因为前一个参加的会议最多只能有一个，所以使用常量维护即可
    按照开始时间升序遍历，使用最小堆维护会议结束时间的最小值，确保当前参与会议的开始时间 >= 前一个会议
    """

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        pre_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < pre_end:
                return False
            pre_end = end
        return True


# 53. 会议室 II
class Solution2:
    """
    对比：最长递增子序列，只能找到一个最长的安排方式，并不能确保整体所需会议室最少
    核心思想：
    按照会议召开时间从前往后遍历，添加第一个会议结束时间初始化(默认必须有一个会议室)；
    后续每个会议，需要检测是否存在一个会议已经结束(前面遍历会议的最小结束时间是否小于等于当前会议开始时间)，
    存在，即可共用一个会议室，否则，新增会议室。

    要点：只需要确认新增会议时，是否已经有会议结束，而不需要确认是哪个会议结束

    ==> 本质上也是模拟法
    """

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        # 堆存放结束时间，目的：找到最先结束的会议
        room = list()
        heappush(room, intervals[0][1])
        # FIXME 不能使用append添加数据，这样添加的数据，不是最小堆
        # room.append(intervals[0])

        for start, end in intervals[1:]:
            # 如果开始时间，仍然早于已占用会议室的最早结束时间，则需要新增会议室
            # FIXME 注意题目条件中，是否允许start == end 来使用
            if start < room[0]:  # 新会议召开时，没有会议结束，索引需要新能会议室
                heappush(room, end)
            else:
                heappop(room)
                heappush(room, end)
        return len(room)

    # 优化逻辑: 最小堆
    def minMeetingRooms1(self, intervals: List[List[int]]) -> int:
        # 默认就优先按照第一个元素排序 ==》 start时间升序
        intervals.sort()

        # 初始化最小堆
        room = list()
        # 添加第一个会议
        heappush(room, intervals[0][1])

        for start, end in intervals[1:]:
            # 如果会议开始时，前面有会议结束，需要弹出前一个会议
            if start >= room[0]:
                heappop(room)
            heappush(room, end)
        return len(room)

    # TODO 精彩的思路：
    # 类似差分法：开始时间，加1； 结束时间，减1，在最终求前缀和的过程中，出现的最大值，即所需要的会议室数量
    # 进一步理解：加锁，解锁的操作
    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        array = [0] * (10 ** 6 + 1)
        intervals.sort()

        for start, end in intervals:
            array[start] += 1
            array[end] -= 1

        ans = 0
        total = 0
        for i in array:
            total += i
            ans = max(ans, total)

        return ans

    # 差分法：使用字典
    def minMeetingRooms3(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        d = defaultdict(int)

        for start, end in intervals:
            d[start] += 1
            d[end] -= 1

        # 默认按照首个数值排序，升序
        array = sorted(d.items())

        ans = 0
        total = 0
        for _, count in array:
            total += count
            ans = max(ans, total)

        return ans

    def minMeetingRooms3_1(self, intervals: List[List[int]]) -> int:
        # ==> 直接使用数组存储索引，以及加锁、解锁数量
        up_down = []
        for start, end in intervals:
            up_down.append((start, 1))
            up_down.append((end, -1))
        up_down.sort()
        res = 0
        room = 0
        for _, n in up_down:
            room += n
            res = max(room, res)
        return res

    # 使用双指针，避免再次排序
    def minMeetingRooms4(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        # 分离开始时间，结束时间，并按照升序进行排列
        start_timings = sorted([item[0] for item in intervals])
        end_timings = sorted([item[1] for item in intervals])

        n = len(intervals)

        used_rooms = 0
        # 使用双指针
        start_pointer = 0
        end_pointer = 0

        while start_pointer < n:  # 终止条件，所有会议均已召开
            # 根据释放的会议室，减少会议室数量
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                used_rooms -= 1
                end_pointer += 1
            # 假设每个会议需要一个新的会议室
            used_rooms += 1
            start_pointer += 1

        return used_rooms


# 56. 合并区间
# https://leetcode-cn.com/problems/merge-intervals/
class Solution3:
    # 使用 差分思想处理 ==》 加锁 解锁操作, 当锁为0，表示合并后的的区间
    # FIXME 方向思考：当前区间开始坐标 需要小于等于 前一个区间的结束坐标，然后更新结束坐标(两者之间的较大值)
    # 当前区间的开始坐标 大于 前一个区间的结束坐标，表示前边的区间可以合并；当前区间开始值作为新区间开始值
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return list()
        start_arr = sorted([item[0] for item in intervals])
        end_arr = sorted([item[1] for item in intervals])

        ans = list()

        start_point = 0
        end_point = 0

        n = len(intervals)
        pre_start = 0
        while start_point < n:
            if start_arr[start_point] <= end_arr[end_point]:
                if end_arr[start_point] >= end_arr[end_point]:
                    end_point = start_point
            else:
                temp = [start_arr[pre_start], end_arr[end_point]]
                ans.append(temp)

                pre_start = start_point
                end_point += 1
            start_point += 1
        temp = [start_arr[pre_start], end_arr[end_point]]
        ans.append(temp)
        return ans

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        # 先冒泡将序列按照区间开头数值大小升序排列
        # right = 1
        # _len = len(intervals)
        # while right <= (_len - 1):
        #     for i in range(_len - right):
        #         if intervals[i][0] > intervals[i+1][0]:
        #             intervals[i], intervals[i+1] = intervals[i+1], intervals[i]
        #     right += 1
        # intervals = sorted(intervals, key=lambda x: x[0])
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for gap in intervals[1:]:
            if res[-1][1] < gap[0]:
                res.append(gap)
            elif res[-1][1] < gap[1]:
                res[-1][1] = gap[1]
        return res

    def merge3(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


# 57. 插入区间
# https://leetcode-cn.com/problems/insert-interval/
class Solution4:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return intervals.append(newInterval)
        ans = list()

        pre = newInterval

        for arr in intervals:
            if pre[0] > arr[1]:  # 两者不相交
                ans.append(arr)
            elif pre[1] < arr[0]:
                if pre is not None:
                    ans.append(pre)
                    pre = None
                ans.append(arr)
            else:
                pre = [min(pre[0], arr[0]), max(pre[1], arr[1])]

        return ans


# 715. Range 模块 HARD
# https://leetcode-cn.com/problems/range-module/


# 1094. 拼车
class Solution5:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        up_down = list()
        for cnt, start, end in trips:
            up_down.append(start, cnt)
            up_down.append(end, -1 * cnt)

        up_down.sort()
        total = 0
        for _, inc in up_down:
            total += inc
            if total > capacity:
                return False

        return True

    def carPooling2(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        off_dist = []
        count = 0
        for i in range(len(trips)):
            dist = trips[i][1]
            while off_dist and dist >= off_dist[0][0]:
                _, passenger = heapq.heappop(off_dist)
                count -= passenger
            count += trips[i][0]
            if count > capacity:
                return False
            heapq.heappush(off_dist, [trips[i][-1], trips[i][0]])
        return True


# 1751. 最多可以参加的会议数目 II HARD
class Solution6:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        return 0


# 2054. 两个最好的不重叠活动 middle
# https://leetcode-cn.com/problems/two-best-non-overlapping-events/
class Solution7:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        return 0


if __name__ == '__main__':
    sol = Solution3()
    nums = [[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]
    sol.merge(nums)
