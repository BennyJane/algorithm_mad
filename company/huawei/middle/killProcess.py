from typing import List
import collections


# 582. 杀掉进程
# https://leetcode-cn.com/problems/kill-process/
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        n = len(pid)
        # 记录父子关系
        d = collections.defaultdict(list)
        for i in range(n):
            p = pid[i]
            pp = ppid[i]
            d[pp].append(p)

        ans = [kill]
        parents = [kill]
        while parents:
            temp = []
            for pp in parents:
                child = d.get(pp, [])
                ans.extend(child)
                temp.extend(child)
            parents = set(temp)
        if 0 in parents:
            pid.extend(ppid)
            ans = set(pid)
        return list(ans)


if __name__ == '__main__':
    sol = Solution()
    pid = [6, 1, 3, 9, 5, 8, 7, 4, 10]
    ppid = [5, 8, 4, 5, 10, 5, 3, 8, 0]
    sol.killProcess(pid, ppid, 10)
