# 5919. 所有子字符串中的元音
class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        special = ['a', 'e', 'i', 'o', 'u']

        total = 0
        count = n
        for i, c in enumerate(word):
            frep = count * (i + 1)
            count -= 1
            if c in special:
                total += frep
        return total

    # 前缀和
    def countVowels1(self, word: str) -> int:
        n = len(word)
        special = ['a', 'e', 'i', 'o', 'u']

        pre = [0] * (n + 1)

        count = 0
        for i, c in enumerate(word):
            if c in special:
                count += 1
            pre[i + 1] = count

        ans = 0
        for i in range(n):
            for j in range(i, n + 1):
                total = pre[j] - pre[i]
                ans += total
        return ans


if __name__ == '__main__':
    sol = Solution()
    sol.countVowels("noosabasboosa")
