from collections import defaultdict
from typing import List


class Solution1:
    def checkString(self, s: str) -> bool:
        ACnt = 0
        BCnt = 0
        for i, c in enumerate(s):
            if c == 'a':
                if BCnt > 0:
                    return False
                ACnt += 1
            else:
                BCnt += 1

        return True


class Solution2:
    def numberOfBeams(self, bank: List[str]) -> int:
        stack = []

        ans = 0
        for i, s in enumerate(bank):
            cnt = 0
            for c in s:
                if c == '1':
                    cnt += 1
            if stack:
                ans += stack[-1] * ans
            if cnt > 0:
                stack.append(cnt)

        return ans


class Solution3:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for c in asteroids:
            if mass >= c:
                mass += c
            else:
                return False

        return True


# 图： 求最长环
class Solution4:
    def maximumInvitations(self, favorite: List[int]) -> int:

        return 0

    def maximumInvitations2(self, favorite: List[int]) -> int:
        n = len(favorite)

        d = defaultdict(list)
        for i, c in enumerate(favorite):
            d[c].append(i)

        visited = [False] * n
        ans = 1
        for i in range(n):
            if visited[i]:
                continue
            start = i
            visited[i] = True
            nxt = favorite[i]
            temp = set()
            lastIndex = i
            temp.add(i)
            step = 1

            # 是否首尾相接
            isEnd = False
            while nxt not in temp and (
                    favorite[nxt] not in temp or lastIndex == favorite[nxt] or favorite[nxt] == start):
                if favorite[nxt] == start:
                    isEnd = True
                visited[nxt] = True
                temp.add(nxt)
                lastIndex = nxt

                nxt = favorite[nxt]
                step += 1
            if not isEnd:
                pass
            ans = max(ans, step)

        return ans


if __name__ == '__main__':
    sol = Solution4()
    # arr = [2, 2, 1, 2]
    # arr = [1, 2, 0]
    arr = [3, 0, 1, 4, 1]
    arr = [1, 0, 0, 2, 1, 4, 7, 8, 9, 6, 7, 10, 8]
    sol.maximumInvitations(arr)
