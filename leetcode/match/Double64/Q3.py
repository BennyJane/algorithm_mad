from typing import List


class Solution:
    # TODO 转化为0与1
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        ans = []

        n = len(s)
        res = [0] * 10 * 5
        left = 0
        while left < n:
            val = 0 if s[left] == "|" else 1
            res[left] = val
            left += 1
        for x, y in queries:
            _sum = sum(res[x: y + 1])
            left = x
            while res[left] != 0:
                _sum -= 1
                left += 1
            right = y
            while res[right] != 0:
                _sum -= 1
                right -= 1
            _sum = 0 if _sum < 0 else _sum
            ans.append(_sum)
        return ans

    def platesBetweenCandles2(self, s: str, queries: List[List[int]]) -> List[int]:
        ans = []

        n = len(s)
        res = []
        left = 0
        while left < n:
            while left + 1 < n and not (s[left] == "|" and s[left + 1] == "*"):
                left += 1
            if left >= n:
                break
            right = left + 1
            count = 0
            while right < n and s[right] != "|":
                count += 1
                right += 1
            res.append((left, right, count))
            left = right
        for x, y in queries:
            temp = 0
            for x1, y1, c1 in res:
                if x1 > y:
                    break
                if x <= x1 and y >= y1:
                    temp += c1
            ans.append(temp)
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = "***|**|*****|**||**|*"
    queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]

    # s = "**|**|***|"
    # queries = [[2, 5], [5, 9]]
    sol.platesBetweenCandles(s, queries)
