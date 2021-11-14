from typing import List


class Solution:
    """
    分情況討論：任务的最小值 t 与 体力最大值的关系 w
    t >= w ==> 药丸给工人体力最大的人
    t < m

    """

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        ans = 0

        if workers[0] >= tasks[-1]:
            return min(len(tasks), len(workers))

        if tasks[0] > workers[-1]:
            for i in range(pills):
                if workers[-1 * (pills - i)] + strength >= tasks[i]:
                    ans += 1
            return ans

        return 0
