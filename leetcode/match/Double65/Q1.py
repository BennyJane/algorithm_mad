class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        from collections import defaultdict

        allKeys = set()

        m = defaultdict(int)
        for c in word1:
            m[c] += 1
            allKeys.add(c)

        n = defaultdict(int)
        for c in word2:
            n[c] += 1
            allKeys.add(c)

        for k in allKeys:
            if abs(m[k] - n[k]) > 3:
                return False

        return True
