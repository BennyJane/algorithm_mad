from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed = sorted(changed, key = lambda x: x)
        _len = len(changed)
        if _len % 2 != 0:
            return []
        half = int(_len >> 1)
        ans = []
        visited = [0] * _len
        left = 0
        right = 1
        while left < _len:
            while left < _len and visited[left] == -1:
                left += 1
            if left >= _len:
                break
            l_val = changed[left]
            dou = l_val * 2
            right = max(left + 1, right)
            while right < _len and (changed[right] != dou or visited[right] < 0):
                right += 1
            if right >= _len:
                return []
            ans.append(l_val)
            visited[right] = -1
            visited[left] = -1
        if len(ans) != half:
            return []
        return ans

    def findOriginalArray2(self, changed: List[int]) -> List[int]:
        changed.sort()
        _len = len(changed)
        if _len % 2 != 0:
            return []
        half = int(_len >> 1)
        count = 0
        ans = []
        visited = [0] * _len
        for i in range(_len):
            cur = changed[i]
            if visited[i] < 0:
                continue
            double_val = changed[i] * 2
            if double_val not in changed:
                return []
            for j in range(i + 1, _len):
                if visited[j] < 0:
                    continue
                if double_val == changed[j]:
                    ans.append(cur)
                    visited[j] = -1
                    count += 1
                    break
        if count != half:
            return []
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [
        # 0, 0, 0, 0
        1, 3, 4, 2, 6, 8
        # 6, 3, 0, 1
    ]
    sol.findOriginalArray(nums)
