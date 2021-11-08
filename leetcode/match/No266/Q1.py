# 5918. 统计字符串中的元音子字符串
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        from collections import defaultdict
        s = ['a', 'e', 'i', 'o', 'u']

        def check(d: dict):
            for char in s:
                if d[char] == 0:
                    return False
            return True

        ans = 0
        n = len(word)

        for start in range(n):
            c = word[start]
            if c not in s:
                continue
            d = defaultdict(int)
            d[c] += 1
            for end in range(start+1, n):
                next_c = word[end]
                if next_c not in s:
                    break
                d[next_c] += 1
                if check(d):
                    ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = "cuaieuouac"
    sol.countVowelSubstrings()
