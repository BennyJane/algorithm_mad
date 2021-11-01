from typing import List
from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        for s in arr:
            if count.get(s) == 1:
                k -= 1
                if k == 0:
                    return s
        return ""

if __name__ == '__main__':
    sol = Solution()
    sol.kthDistinct(["a","b","a"], 3)

